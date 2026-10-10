# -*- coding: utf-8 -*-
"""把第三、四篇的小黑配图插入 paid-content 完整版正文。
插入点：第一个 `## ` 标题之前（引言段之后），保证试读版保留段也能看到。
"""
import os

BASE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "paid-content")

JOBS = [
    ("第三篇-完整版/index.md", "第三篇-完整版/images/00-hei-intro.png",
     "一只小黑蹲在地上，把散落的拼图拼成一张完整的图", "本篇"),
    ("第三篇-完整版/第 22 章 打造 Skill：将书和视频蒸馏为可执行 Skill/index.md",
     "第三篇-完整版/第 22 章 打造 Skill：将书和视频蒸馏为可执行 Skill/images/22-hei-skill.png",
     "一只小黑坐在书前，把书里的精华蒸馏进一个小瓶子", "本章"),
    ("第三篇-完整版/第 23 章 其他用法补充：WorkBuddy 实操案例集/index.md",
     "第三篇-完整版/第 23 章 其他用法补充：WorkBuddy 实操案例集/images/23-hei-cases.png",
     "一只小黑同时抛接着好几张任务卡", "本章"),
    ("第三篇-完整版/第 24 章 如何进行多 Agent 系统设计/index.md",
     "第三篇-完整版/第 24 章 如何进行多 Agent 系统设计/images/24-hei-multiagent.png",
     "一只小黑像指挥家一样指挥一排色块整齐行动", "本章"),
    ("第三篇-完整版/第 25 章 自动化工作流的可靠性/index.md",
     "第三篇-完整版/第 25 章 自动化工作流的可靠性/images/25-hei-reliability.png",
     "一只小黑盯着屏幕上的心跳曲线，手里拿着检查清单", "本章"),
    ("第四篇-完整版/index.md", "第四篇-完整版/images/00-hei-intro.png",
     "一只小黑推开一扇门，走进一座纸做的办公城市", "本篇"),
    ("第四篇-完整版/第 26 章 岗位路线图：不同岗位如何把 WorkBuddy 用深/index.md",
     "第四篇-完整版/第 26 章 岗位路线图：不同岗位如何把 WorkBuddy 用深/images/26-hei-role.png",
     "一只小黑站在岔路口，旁边堆着几顶不同的岗位帽子", "本章"),
    ("第四篇-完整版/第 27 章 行业路线图：从通用能力到行业工作流/index.md",
     "第四篇-完整版/第 27 章 行业路线图：从通用能力到行业工作流/images/27-hei-industry.png",
     "一只小黑把刻着行业图标的积木垒成一座塔", "本章"),
    ("第四篇-完整版/第 28 章 组建你的 AI 团队/index.md",
     "第四篇-完整版/第 28 章 组建你的 AI 团队/images/28-hei-team.png",
     "一只小黑举着一面小旗，面前是一排等待队友的空基座", "本章"),
]

for rel, img, alt, scope in JOBS:
    path = os.path.join(BASE, rel)
    with open(path, encoding="utf-8") as f:
        text = f.read()
    if img.split("/")[-1] in text:
        print("skip (already has image):", rel)
        continue
    block = (f"\n![{alt}](./{img})\n\n"
             f"*配图为示意插画，用于帮助理解{scope}主题，与实际软件界面无关。*\n")
    # 插在第一个 ## 标题之前
    idx = text.find("\n## ")
    if idx == -1:
        print("!! no H2 found:", rel)
        continue
    text = text[:idx] + "\n" + block.lstrip("\n") + text[idx:].lstrip("\n")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print("inserted:", rel)
