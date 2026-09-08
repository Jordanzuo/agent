#!/usr/bin/env python3
"""Re-typeset 离职证明 on the original scan.

All body text is removed from the scan (paper texture, watermark, header and
seal are preserved), then every line is redrawn with one consistent font so
edited fields are indistinguishable from the rest of the document.
"""

import os

import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

SRC = "/home/ubuntu/.cursor/projects/workspace/assets/45c7420e-9cbd-471e-b07e-605a623f59c3.png"
OUT = "/workspace/output/离职证明_万莹莹.png"
FONT_PATH = "/usr/share/fonts/truetype/wqy/wqy-microhei.ttc"

INK = (22, 22, 20, 255)
BODY_TOP = 190  # header (logo, rule, title) above this line is kept as-is

NAME = "万莹莹"
TITLE = "女士"
ID_NO = "51300119870129006X"
START = "【2023】年【12】月【1】"
POSITION = "游戏客服"


def extract_seal(rgb):
    r, g, b = [rgb[:, :, i].astype(int) for i in range(3)]
    redness = np.clip((r - np.maximum(g, b) - 12) / 50.0, 0, 1)
    redness[:680, :] = 0
    alpha = (redness * 255).astype(np.uint8)
    layer = np.dstack([rgb, alpha])
    return Image.fromarray(layer, "RGBA"), redness


def clear_text(rgb, redness):
    r, g, b = [rgb[:, :, i].astype(int) for i in range(3)]
    lum = (r * 299 + g * 587 + b * 114) // 1000
    mask = (lum < 112) & (redness < 0.25)
    mask[:BODY_TOP, :] = False
    mask[:, :55] = False
    mask[:, 1090:] = False
    mask = mask.astype(np.uint8) * 255
    mask = cv2.dilate(mask, np.ones((5, 5), np.uint8), iterations=1)
    bgr = cv2.cvtColor(rgb, cv2.COLOR_RGB2BGR)
    clean = cv2.inpaint(bgr, mask, 4, cv2.INPAINT_TELEA)
    return cv2.cvtColor(clean, cv2.COLOR_BGR2RGB)


class Typesetter:
    def __init__(self, layer):
        self.draw = ImageDraw.Draw(layer)

    def text_width(self, text, font):
        return self.draw.textlength(text, font=font)

    def ink_offset(self, font):
        return font.getbbox("兹证明国")[1]

    def run(self, x, top, text, font):
        self.draw.text((x, top - self.ink_offset(font)), text, font=font, fill=INK)
        return x + self.text_width(text, font)

    def field(self, x, top, text, font, width, gap_below=3):
        tw = self.text_width(text, font)
        self.run(x + (width - tw) / 2, top, text, font)
        uy = top - self.ink_offset(font) + font.size + gap_below
        self.draw.line([(x, uy), (x + width, uy)], fill=INK, width=1)
        return x + width

    def right(self, x_right, top, text, font):
        self.run(x_right - self.text_width(text, font), top, text, font)


def main():
    os.makedirs(os.path.dirname(OUT), exist_ok=True)

    rgb = np.array(Image.open(SRC).convert("RGB"))
    seal, redness = extract_seal(rgb)
    background = Image.fromarray(clear_text(rgb, redness))

    layer = Image.new("RGBA", background.size, (0, 0, 0, 0))
    ts = Typesetter(layer)
    body = ImageFont.truetype(FONT_PATH, 23)
    note = ImageFont.truetype(FONT_PATH, 19)
    foot = ImageFont.truetype(FONT_PATH, 20)

    # Paragraph (line tops measured from the original scan)
    x = ts.run(76, 208, "兹证明", body) + 6
    x = ts.field(x, 208, NAME, body, 80) + 4
    x = ts.run(x, 208, TITLE + "（身份证号码：", body) + 4
    x = ts.field(x, 208, ID_NO, body, 236) + 4
    ts.run(x, 208, "）于" + START + "日起", body)

    x = ts.run(73, 244, "在本公司任职", body) + 2
    x = ts.field(x, 244, POSITION, body, 98)
    ts.run(x, 244, "，于【2026】年【8】月【25】日解除（终止）劳动关系，所有离职手", body)

    ts.run(72, 283, "续已经办理完毕。", body)
    ts.run(116, 317, "离职原因：因公司解散非本人意愿终止，协商一致解除劳动合同。", body)
    ts.run(115, 356, "特此证明。", body)

    # Notes
    ts.run(71, 414, "注：1、如员工档案存在公司，离职后需转出档案。自离职之日起，公司停止为其交纳存档费。", note)
    ts.run(109, 461, "2、离职之日起，不得再以本公司名义对外从事任何活动。", note)
    ts.run(109, 505, "3、该员工已与本公司签订《解除劳动合同协议书》，本公司按协议支付解除劳动合同补偿金。", note)
    ts.run(108, 550, "4、该员工已与本公司签订《商业秘密保密协议》（协议名称以实际为准），离职之日起该员工仍应履行该协", note)
    ts.run(110, 582, "议，不得侵犯本公司商业秘密，不得在离职后唆使其他员工接受竞争对手聘用，侵夺甲方客户或引诱其他员", note)
    ts.run(113, 615, "工离职，否则本公司有权追究其法律责任。若造成严重损害的，本公司保留追究其刑事责任的权利。", note)
    ts.run(116, 648, "5、自离职之日起，本公司不要求该员工履行竞业义务。", note)

    # Footer (right-aligned to the original text edge)
    ts.right(1012, 721, "成都辛克普雷科技有限公司", foot)
    ts.right(1012, 751, "【2026】年【8】月【25】日", foot)

    # Soften rendered text slightly so it matches the scan's optics
    layer = layer.filter(ImageFilter.GaussianBlur(0.55))

    result = background.convert("RGBA")
    result.alpha_composite(layer)
    result.alpha_composite(seal)
    result.convert("RGB").save(OUT, "PNG")
    print(f"Saved: {OUT}")


if __name__ == "__main__":
    main()
