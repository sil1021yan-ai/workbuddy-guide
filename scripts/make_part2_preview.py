# -*- coding: utf-8 -*-
"""把第二篇公开章节切成试读版。

规则：
- 本篇导读（篇目录 index.md）：保留全文，仅页首加 banner。
- 第 11-21 章：保留 frontmatter + 引言 + 小黑图 + 一/二 框架段，
  从「## 三、」起替换为 <Paywall> 购买引导（第 13 章从「## 四、」）。
完整版原文已备份到 paid-content/（gitignored，仅本地）。
"""
import os
import re

BASE = "docs/bluebook/第二篇 案例篇：从一项任务到一支 AI 团队"

BANNER = '<Paywall part="2" variant="banner" />\n\n'
CTA = (
    "\n<Paywall part=\"2\" />\n\n"
    "*—— 以上试读到此为止。第二篇共 11 章，完整版 PDF 包含全部实操内容。——*\n"
)

# 特殊章节：切分标题不同
CUT_RULES = {
    "第 13 章": re.compile(r"^## 四、", re.M),
}
DEFAULT_CUT = re.compile(r"^## 三、", re.M)


def add_banner_after_quote(text: str) -> str:
    """在第一个 "> " 引用块之后插入页首试读提示条。"""
    lines = text.split("\n")
    out = []
    inserted = False
    for line in lines:
        out.append(line)
        if not inserted and line.startswith("> "):
            out.append("")
            out.append(BANNER.rstrip("\n"))
            inserted = True
    if not inserted:
        # 没找到引用块，就插在第一个 H1 之后
        text2 = "\n".join(out)
        return re.sub(r"(^# .+$)", r"\1\n\n" + BANNER.rstrip("\n"), text2,
                      count=1, flags=re.M)
    return "\n".join(out)


for entry in sorted(os.listdir(BASE)):
    dirpath = os.path.join(BASE, entry)
    if os.path.isfile(dirpath):
        continue  # 篇目录里的 index.md 单独处理
    path = os.path.join(dirpath, "index.md")
    if not os.path.isfile(path):
        continue

    with open(path, encoding="utf-8") as f:
        text = f.read()

    if text.startswith("<Paywall"):
        print("skip (already converted):", entry)
        continue

    rule = None
    for key, r in CUT_RULES.items():
        if entry.startswith(key):
            rule = r
            break
    if rule is None:
        rule = DEFAULT_CUT

    m = rule.search(text)
    if not m:
        print("!! NO CUT POINT:", entry)
        continue

    kept = text[: m.start()].rstrip() + "\n"
    kept = add_banner_after_quote(kept)
    new_text = kept + "\n" + CTA

    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(new_text)
    print("converted:", entry, f"(kept {len(kept)} chars of {len(text)})")

# 篇目录导读：保留全文，仅加 banner
root_index = os.path.join(BASE, "index.md")
if os.path.isfile(root_index):
    with open(root_index, encoding="utf-8") as f:
        text = f.read()
    if "<Paywall" not in text:
        text = add_banner_after_quote(text)
        # 导读结尾追加一张完整购买卡
        text = text.rstrip() + "\n\n" + CTA
        with open(root_index, "w", encoding="utf-8", newline="\n") as f:
            f.write(text)
        print("banner added to 本篇导读")
