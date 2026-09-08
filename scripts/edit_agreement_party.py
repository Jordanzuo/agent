#!/usr/bin/env python3
"""Replace 乙方 name and ID number on the 解除劳动合同协议书 scan."""

import os

import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

SRC = "/home/ubuntu/.cursor/projects/workspace/assets/bf0ce1bd-a67f-433d-ac9d-0a51967f5c75.jpg"
OUT = "/workspace/output/解除劳动合同协议书_万莹莹.jpg"
CJK_FONT = "/tmp/fonts/NotoSerifCJKsc-Regular.otf"
LATIN_FONT = "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf"

NAME = "万莹莹"
ID_NO = "51300119870129006X"

# Measured from the scan. The printed line rises to the right by ~2.5 deg.
NAME_BOX = (260, 238, 316, 264)
ID_BOX = (442, 228, 608, 254)
NAME_X, LINE_TOP = 264, 245          # glyph top of the name at its left edge
ID_X, ID_WIDTH = 446, 158            # original digits span
TILT_DEG = 2.5
INK = (30, 30, 28, 255)


def render_digits(text, height_px, width_px):
    font = ImageFont.truetype(LATIN_FONT, 20)
    bbox = font.getbbox(text)
    img = Image.new("RGBA", (bbox[2] + 4, bbox[3] + 4), (0, 0, 0, 0))
    ImageDraw.Draw(img).text((2 - bbox[0], 2 - bbox[1]), text, font=font, fill=INK)
    img = img.crop(img.getbbox())
    return img.resize((width_px, height_px), Image.LANCZOS)


def main():
    os.makedirs(os.path.dirname(OUT), exist_ok=True)

    bgr = cv2.imread(SRC)
    gray = cv2.cvtColor(bgr, cv2.COLOR_BGR2GRAY)
    mask = np.zeros(gray.shape, np.uint8)
    for x0, y0, x1, y1 in (NAME_BOX, ID_BOX):
        mask[y0:y1, x0:x1] = (gray[y0:y1, x0:x1] < 135).astype(np.uint8) * 255
    mask = cv2.dilate(mask, np.ones((5, 5), np.uint8))
    clean = cv2.inpaint(bgr, mask, 4, cv2.INPAINT_TELEA)
    base = Image.fromarray(cv2.cvtColor(clean, cv2.COLOR_BGR2RGB)).convert("RGBA")

    # Typeset on a horizontal baseline, then rotate to follow the scan's tilt.
    layer = Image.new("RGBA", base.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(layer)
    cjk = ImageFont.truetype(CJK_FONT, 17)
    draw.text((NAME_X, LINE_TOP - cjk.getbbox("左贤清")[1]), NAME, font=cjk, fill=INK)
    digits = render_digits(ID_NO, height_px=14, width_px=ID_WIDTH)
    layer.alpha_composite(digits, (ID_X, LINE_TOP))
    layer = layer.rotate(TILT_DEG, resample=Image.BICUBIC, center=(NAME_X, LINE_TOP))
    layer = layer.filter(ImageFilter.GaussianBlur(0.5))

    base.alpha_composite(layer)
    base.convert("RGB").save(OUT, "JPEG", quality=95)
    print(f"Saved: {OUT}")


if __name__ == "__main__":
    main()
