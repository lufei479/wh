# -*- coding: utf-8 -*-
"""把"逛"图标作为新字形加入 iconfont.ttf，同时更新 woff/woff2/css/json"""
import math, os, shutil, json
from fontTools.ttLib import TTFont, newTable
from fontTools.pens.ttGlyphPen import TTGlyphPen

FONT_DIR = r"D:\gjwy\fond\download\font_5244711_tki2w4uia8"
SRC_TTF = os.path.join(FONT_DIR, "iconfont.ttf")
NEW_UNI = 0xe608          # 选一个未占用的码位
NEW_CLS = "guang"          # CSS 类名后缀 -> icon-guang
NEW_NAME = "逛"

# ---------- 1. 用多边形近似圆角矩形，返回顶点列表 ----------
def rounded_rect_points(cx, cy, w, h, r, n=12):
    """返回顺时针方向的圆角矩形顶点（含四角圆弧）。坐标系 y 向上。"""
    x0, y0 = cx - w/2, cy - h/2
    x1, y1 = cx + w/2, cy + h/2
    pts = []
    corners = [
        (x1-r, y1-r, 0, 90),      # 右上
        (x0+r, y1-r, 90, 180),    # 左上
        (x0+r, y0+r, 180, 270),   # 左下
        (x1-r, y0+r, 270, 360),   # 右下
    ]
    for (ccx, ccy, a0, a1) in corners:
        for i in range(n+1):
            a = math.radians(a0 + (a1-a0)*i/n)
            pts.append((ccx + r*math.cos(a), ccy + r*math.sin(a)))
    return pts

def circle_points(cx, cy, r, n=20):
    return [(cx + r*math.cos(2*math.pi*i/n), cy + r*math.sin(2*math.pi*i/n)) for i in range(n)]

# ---------- 2. 组装字形 ----------
# 逛图标：一个圆角 blob 轮廓（外轮廓+内孔），左上有个小耳朵，两只圆眼睛，一个微笑
pen = TTGlyphPen(None)

# 外轮廓（顺时针）：圆角 blob 主体
outer = rounded_rect_points(cx=512, cy=500, w=620, h=480, r=130, n=10)
# 在左上角加一个小耳朵：在外轮廓顶部左侧插入一个小凸起
# 简单做法：直接在外轮廓上，把顶部左侧的点改成带耳朵的形状。
# 这里用一个近似：在外轮廓顶部（y~740），x=350 附近加一个半圆耳朵。
# 为简化，我们直接画外轮廓，再单独画耳朵填充。

# 画外轮廓
pen.moveTo(outer[0])
for p in outer[1:]:
    pen.lineTo(p)
pen.closePath()

# 内轮廓（逆时针 = 反孔）：稍微缩小一点，形成 ~70 的描边厚度
inner = rounded_rect_points(cx=512, cy=500, w=620-140, h=480-140, r=90, n=10)
inner = inner[::-1]   # 反向，变成顺时针外轮廓的反面 = 镂空孔
pen.moveTo(inner[0])
for p in inner[1:]:
    pen.lineTo(p)
pen.closePath()

# 耳朵：左上角一个小半圆凸起（填充的小椭圆，连在外轮廓上）
ear = circle_points(cx=330, cy=700, r=55, n=12)
# 只取上半部分做个小凸起——简化成小椭圆
pen.moveTo(ear[0])
for p in ear[1:]:
    pen.lineTo(p)
pen.closePath()

# 左眼
pen.moveTo((410, 510))
for p in circle_points(410, 510, 22, n=12):
    pen.lineTo(p)
pen.closePath()

# 右眼
pen.moveTo((610, 510))
for p in circle_points(610, 510, 22, n=12):
    pen.lineTo(p)
pen.closePath()

# 微笑：一个小月牙形（用两个圆弧近似的填充条）
smile_outer = circle_points(512, 560, 50, n=12)
pen.moveTo(smile_outer[0])
for p in smile_outer[1:]:
    pen.lineTo(p)
pen.closePath()

glyph = pen.glyph()

# ---------- 3. 写入 TTF ----------
font = TTFont(SRC_TTF)
glyf = font["glyf"]
hmtx = font["hmtx"]

glyph_name = "guang"
# 添加到 glyf
glyf[glyph_name] = glyph
# 添加字形顺序
order = font.getGlyphOrder()
if glyph_name not in order:
    order.append(glyph_name)
font.setGlyphOrder(order)
# 设置水平度量
glyph.recalcBounds(glyf)
hmtx[glyph_name] = (1024, 100)

# 加 cmap 映射
for table in font["cmap"].tables:
    if table.isUnicode():
        table.cmap[NEW_UNI] = glyph_name

font.save(SRC_TTF)
print("TTF saved, glyph:", glyph_name, "bounds:", glyph.xMin, glyph.yMin, glyph.xMax, glyph.yMax)

# ---------- 4. 转 woff / woff2 ----------
font.flavor = "woff2"
font.save(os.path.join(FONT_DIR, "iconfont.woff2"))
font.flavor = "woff"
font.save(os.path.join(FONT_DIR, "iconfont.woff"))
font.flavor = None
print("woff/woff2 saved")
