# -*- coding: utf-8 -*-
"""把第三、四篇完整版拼装成飞书 Markdown 导入文件（_feishu/part3.md、part4.md）。

- CWD = paid-content，图片改写为 ![alt](<@./<src>/.../images/x.png>) 形式
- 篇导言的 H1 去掉（标题用 --title 传入），章节 H1 保留
- 表格填空线 ____ 转义为 \_\_\_\_
"""
import os
import re

BASE = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "paid-content")

PARTS = [
    {
        "out": "_feishu/part3.md",
        "title": "WorkBuddy 小白实战指南 · 第三篇 进阶篇：把案例变成自己的工作系统（完整版）",
        "src": "第三篇-完整版",
        "chapters": [
            "第 22 章 打造 Skill：将书和视频蒸馏为可执行 Skill",
            "第 23 章 其他用法补充：WorkBuddy 实操案例集",
            "第 24 章 如何进行多 Agent 系统设计",
            "第 25 章 自动化工作流的可靠性",
        ],
    },
    {
        "out": "_feishu/part4.md",
        "title": "WorkBuddy 小白实战指南 · 第四篇 岗位与行业落地（完整版）",
        "src": "第四篇-完整版",
        "chapters": [
            "第 26 章 岗位路线图：不同岗位如何把 WorkBuddy 用深",
            "第 27 章 行业路线图：从通用能力到行业工作流",
            "第 28 章 组建你的 AI 团队",
        ],
    },
]

IMG_RE = re.compile(r"\]\(\./images/([^)]+)\)")


def rewrite_images(text: str, prefix: str) -> str:
    # ](./images/x.png) -> ](<@./prefix/images/x.png>)，路径含空格用尖括号
    return IMG_RE.sub(lambda m: f"](<@./{prefix}/images/{m.group(1)}>)", text)


for cfg in PARTS:
    src = cfg["src"]
    out_parts = []

    # 篇导言（去掉 H1，标题走 --title）
    with open(os.path.join(BASE, src, "index.md"), encoding="utf-8") as f:
        intro = f.read()
    intro = re.sub(r"^---\n.*?\n---\n", "", intro, count=1, flags=re.S)
    intro = re.sub(r"^\s*# .+\n", "", intro, count=1)
    intro = rewrite_images(intro, src)
    out_parts.append(intro.strip())

    for ch in cfg["chapters"]:
        with open(os.path.join(BASE, src, ch, "index.md"), encoding="utf-8") as f:
            ch_md = f.read()
        ch_md = re.sub(r"^---\n.*?\n---\n", "", ch_md, count=1, flags=re.S)
        ch_md = rewrite_images(ch_md, f"{src}/{ch}")
        ch_md = ch_md.replace("____", r"\_\_\_\_")
        out_parts.append("---\n\n" + ch_md.strip())

    os.makedirs(os.path.join(BASE, "_feishu"), exist_ok=True)
    out_path = os.path.join(BASE, cfg["out"])
    content = "\n\n".join(out_parts) + "\n"
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)

    print(f"written: {cfg['out']} ({len(content)} chars)")
    bad = re.findall(r"\]\(\./images/", content)
    imgs = re.findall(r"<@\.(/[^)>]+)>", content)
    print(f"  残留未改写引用: {len(bad)} / 改写后引用: {len(imgs)}")
    for i in imgs:
        p = os.path.join(BASE, i.lstrip("/"))
        if not os.path.isfile(p):
            print(f"  !! 图片不存在: {i}")
    print("  图片存在性检查完成")
