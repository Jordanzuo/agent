#!/usr/bin/env python3
"""Modify 离职证明 by inpainting and redrawing updated fields on the original scan."""

import os

import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

SRC = "/home/ubuntu/.cursor/projects/workspace/assets/45c7420e-9cbd-471e-b07e-605a623f59c3.png"
OUT = "/workspace/output/离职证明_万莹莹.png"
FONT_PATH = "/usr/share/fonts/truetype/wqy/wqy-microhei.ttc"


def draw_underlined(draw, x, y, text, font, width=None):
    draw.text((x, y), text, font=font, fill=(8, 8, 8))
    bbox = draw.textbbox((0, 0), text, font=font)
    tw = bbox[2] - bbox[0]
    uw = width if width else tw + 8
    draw.line([(x, y + 24), (x + uw, y + 24)], fill=(8, 8, 8), width=1)
    return x + uw


def main():
    os.makedirs(os.path.dirname(OUT), exist_ok=True)

    img_bgr = cv2.imread(SRC)
    mask = np.zeros(img_bgr.shape[:2], np.uint8)
    for x0, y0, x1, y1 in [(128, 204, 848, 238), (196, 236, 345, 268)]:
        mask[y0:y1, x0:x1] = 255

    inpainted = cv2.inpaint(img_bgr, mask, 3, cv2.INPAINT_TELEA)
    img = Image.fromarray(cv2.cvtColor(inpainted, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(img)

    f21 = ImageFont.truetype(FONT_PATH, 21)
    f18 = ImageFont.truetype(FONT_PATH, 18)

    y = 208
    x = 78
    draw.text((x, y), "兹证明", font=f21, fill=(8, 8, 8))
    x = 150
    x = draw_underlined(draw, x, y, "万莹莹", f21, 72) + 6
    draw.text((x, y), "女士", font=f21, fill=(8, 8, 8))
    x += 48
    draw.text((x, y), "（身份证号码：", font=f21, fill=(8, 8, 8))
    x += 148
    x = draw_underlined(draw, x, y, "51300119870129006X", f18, 228) + 4
    draw.text((x, y), "），于", font=f21, fill=(8, 8, 8))
    x += 58
    draw.text((x, y), "【2023】年【12】月【1】", font=f21, fill=(8, 8, 8))
    draw.text((x + 198, y), "日起在本公司任职", font=f21, fill=(8, 8, 8))

    draw_underlined(draw, 198, 240, "游戏客服", f21, 96)

    img.save(OUT, "PNG")
    print(f"Saved: {OUT}")


if __name__ == "__main__":
    main()
