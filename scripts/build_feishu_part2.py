"""生成第二篇飞书导入文件。

处理要点：
- 去掉每章frontmatter（标题由--title 或 H1 提供）
- 图片路径改为 `<@./第二篇-完整版/.../images/x.png>`（含空格用尖括号）
- 转义 `____` 填空线（避免被解析成加粗）
- 章标题降为 H1（飞书正文层级）
"""
import os
import re

BASE = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "paid-content"
)
SRC = "第二篇-完整版"
OUT = os.path.join(BASE, "_feishu", "part2.md")

IMG_RE = re.compile(r"\]\(\./images/([^/)]+\.png)\)")


def rewrite_images(text: str, chapter_dir: str) -> str:
    # 只替换路径部分，保留 ![alt] 里的 alt 文本：
    # ![alt](./images/x.png)  ->  ![alt](<@./第二篇-完整版/<chapter>/images/x.png>)
    return IMG_RE.sub(lambda m: f"](<@./{SRC}/{chapter_dir}/images/{m.group(1)}>)", text)


def clean(text: str) -> str:
    # 去掉 frontmatter
    text = re.sub(r"^---\n.*?\n---\n", "", text, count=1, flags=re.S)
    # 转义填空线
    text = text.replace("____", "\\_\\_\\_\\_")
    return text


chapters = sorted(
    d for d in os.listdir(os.path.join(BASE, SRC))
    if os.path.isdir(os.path.join(BASE, SRC, d)) and d != "images"
)

parts = []
# 篇导言
intro = clean(open(os.path.join(BASE, SRC, "index.md"), encoding="utf-8").read())
intro = re.sub(r"^# .+\n", "", intro, count=1)
parts.append(intro.strip())

for ch in chapters:
    path = os.path.join(BASE, SRC, ch, "index.md")
    if not os.path.exists(path):
        continue
    body = clean(open(path, encoding="utf-8").read())
    body = rewrite_images(body, ch)
    parts.append(body.strip())

os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, "w", encoding="utf-8", newline="\n") as f:
    f.write("\n\n---\n\n".join(parts) + "\n")

n_img = len(IMG_RE.findall("\n\n".join(parts)))
print(f"chapters: {len(chapters)}")
print(f"images referenced: {n_img}")
print(f"-> {OUT}  ({os.path.getsize(OUT)} bytes)")