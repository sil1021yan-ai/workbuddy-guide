import os
from PIL import Image, ImageDraw, ImageFont

OUT_DIR = "docs/.vitepress/theme/assets"
os.makedirs(OUT_DIR, exist_ok=True)
OUT = os.path.join(OUT_DIR, "wechat-wikiai-yan.png")

# 暖色纸感主题色板（与站点 token 对齐）
BG = (246, 241, 231)        # --wb-bg #F6F1E7
CARD = (251, 248, 241)      # --wb-bg-card #FBF8F1
INK = (42, 32, 24)          # --wb-ink #2A2018
ACCENT = (194, 87, 27)      # --wb-accent #C2571B
MUTED = (138, 122, 100)     # --wb-muted #8A7A64

W, H = 640, 200

# 字体（Windows 系统字体）
latin_font_path = "C:/Windows/Fonts/arial.ttf"
cjk_font_path = "C:/Windows/Fonts/msyh.ttc"
f_id = ImageFont.truetype(latin_font_path, 46)
f_label = ImageFont.truetype(cjk_font_path, 22)
f_note = ImageFont.truetype(cjk_font_path, 18)

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

# 卡片
d.rounded_rectangle([16, 16, W - 16, H - 16], radius=16, fill=CARD,
                    outline=ACCENT, width=3)

# 左侧竖条
d.rectangle([16, 16, 40, H - 16], fill=ACCENT)

# 文本
d.text((64, 46), "我的微信", font=f_label, fill=MUTED)
d.text((62, 74), "Wikiai_Yan", font=f_id, fill=INK)
d.text((64, 150), "备注：WorkBuddy 指南 · 付费完整版 PDF", font=f_note, fill=MUTED)

img.save(OUT, "PNG")
print("saved", OUT, os.path.getsize(OUT), "bytes")
