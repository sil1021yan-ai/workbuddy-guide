# -*- coding: utf-8 -*-
"""把第三、四篇完整版复制到公开站并切成试读版。

切分规则（保留框架/开篇，实操段起替换为购买引导）：
- 第三篇：22章切于 ## 三、；23章切于 ## 案例二｜（案例一留作免费样品）；
  24章切于 ## 四、；25章切于 ## 三、
- 第四篇：26章切于 ## 二、（岗位一留作免费样品）；27章切于 ## 三、；
  28章切于 ## 二、
- 篇导读：保留全文，仅加 banner + 末尾购买卡。
"""
import os
import re
import shutil

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAID = os.path.join(ROOT, "paid-content")
PUB = os.path.join(ROOT, "docs", "bluebook")

PARTS = {
    "3": {
        "src": "第三篇-完整版",
        "dst": "第三篇 进阶篇：把案例变成自己的工作系统",
        "cta": "*—— 以上试读到此为止。第三篇共 4 章，完整版（飞书文档）包含全部实操内容。——*",
        "cuts": {
            "第 22 章": re.compile(r"^## 三、", re.M),
            "第 23 章": re.compile(r"^## 案例二｜", re.M),
            "第 24 章": re.compile(r"^## 四、", re.M),
            "第 25 章": re.compile(r"^## 三、", re.M),
        },
    },
    "4": {
        "src": "第四篇-完整版",
        "dst": "第四篇 岗位与行业落地",
        "cta": "*—— 以上试读到此为止。第四篇共 3 章，完整版（飞书文档）包含全部实操内容。——*",
        "cuts": {
            "第 26 章": re.compile(r"^## 二、", re.M),
            "第 27 章": re.compile(r"^## 三、", re.M),
            "第 28 章": re.compile(r"^## 二、", re.M),
        },
    },
}


def add_banner_after_quote(text: str, part: str) -> str:
    lines = text.split("\n")
    out, inserted = [], False
    for line in lines:
        out.append(line)
        if not inserted and line.startswith("> "):
            out += ["", f'<Paywall part="{part}" variant="banner" />']
            inserted = True
    text2 = "\n".join(out)
    if not inserted:
        text2 = re.sub(r"(^# .+$)", r"\1\n\n" + f'<Paywall part="{part}" variant="banner" />',
                       text2, count=1, flags=re.M)
    return text2


for part, cfg in PARTS.items():
    src_dir = os.path.join(PAID, cfg["src"])
    dst_dir = os.path.join(PUB, cfg["dst"])

    # 1) 复制完整版（index.md + 各章目录）到公开站
    shutil.copy2(os.path.join(src_dir, "index.md"), os.path.join(dst_dir, "index.md"))
    for entry in sorted(os.listdir(src_dir)):
        cdir = os.path.join(src_dir, entry)
        if not os.path.isdir(cdir) or entry == "images":
            continue
        target = os.path.join(dst_dir, entry)
        if os.path.isdir(target):
            shutil.rmtree(target)
        shutil.copytree(cdir, target)
    # 篇级配图目录（导言插图）
    part_img_src = os.path.join(src_dir, "images")
    part_img_dst = os.path.join(dst_dir, "images")
    if os.path.isdir(part_img_dst):
        shutil.rmtree(part_img_dst)
    shutil.copytree(part_img_src, part_img_dst)
    print(f"[Part {part}] copied {cfg['src']} -> {cfg['dst']}")

    # 2) 逐章切试读
    for entry in sorted(os.listdir(dst_dir)):
        cdir = os.path.join(dst_dir, entry)
        if not os.path.isdir(cdir) or entry == "images":
            continue
        path = os.path.join(cdir, "index.md")
        with open(path, encoding="utf-8") as f:
            text = f.read()

        rule = None
        for key, r in cfg["cuts"].items():
            if entry.startswith(key):
                rule = r
                break
        if rule is None:
            print(f"  !! no cut rule for {entry}")
            continue
        m = rule.search(text)
        if not m:
            print(f"  !! NO CUT POINT: {entry}")
            continue

        kept = text[: m.start()].rstrip() + "\n"
        kept = add_banner_after_quote(kept, part)
        cta = (f'\n<Paywall part="{part}" />\n\n' + cfg["cta"] + "\n")
        with open(path, "w", encoding="utf-8", newline="\n") as f:
            f.write(kept + "\n" + cta)
        print(f"  converted: {entry} (kept {len(kept)}/{len(text)} chars)")

    # 3) 篇导读：banner + 末尾购买卡
    root_index = os.path.join(dst_dir, "index.md")
    with open(root_index, encoding="utf-8") as f:
        text = f.read()
    text = add_banner_after_quote(text, part)
    cta = f'\n<Paywall part="{part}" />\n\n' + cfg["cta"] + "\n"
    with open(root_index, "w", encoding="utf-8", newline="\n") as f:
        f.write(text.rstrip() + "\n\n" + cta)
    print(f"[Part {part}] banner+CTA added to 导读")
