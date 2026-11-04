# -*- coding: utf-8 -*-
"""用 iconfont.cn 官方导出的 SVG 直接生成 iconfont 字体（TTF/WOFF/WOFF2）+ CSS + SVG symbol 脚本
源：D:\\icon_jwh9mzb4ub_svg\\icon_2arja7vs4ve\\（home/sousuo/faxian/wode/fabu.svg）"""
import os
import re
from fontTools.fontBuilder import FontBuilder
from fontTools.pens.ttGlyphPen import TTGlyphPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.cu2quPen import Cu2QuPen
from fontTools.misc.transform import Transform
from fontTools.svgLib.path import SVGPath
from fontTools.ttLib import TTFont

BASE = r"D:\html\cdn\iconfont"
SRC = r"D:\icon_jwh9mzb4ub_svg\icon_2arja7vs4ve"
SVG_DIR = os.path.join(BASE, "svg")
ICONS = ["home", "sousuo", "faxian", "wode", "fabu"]  # 依次映射 E600..E604
UPEM = 1024

os.makedirs(SVG_DIR, exist_ok=True)

def extract_paths(svg_text):
    """提取 SVG 中所有 <path d="..."> 的 d 数据（一个图标可能含多个 path）"""
    return re.findall(r'<path\s+d="([^"]+)"', svg_text)

# ---------- 1. 读取官方 SVG，提取路径 ----------
icon_paths = {}
for name in ICONS:
    with open(os.path.join(SRC, name + ".svg"), encoding="utf-8") as f:
        text = f.read()
    ds = extract_paths(text)
    assert ds, "未找到 path: " + name
    icon_paths[name] = ds
    # 同步更新 svg/ 目录下的单文件版本（去掉 fill 属性，统一用 currentColor）
    paths_xml = "".join('<path d="%s"/>' % d for d in ds)
    with open(os.path.join(SVG_DIR, name + ".svg"), "w", encoding="utf-8") as f:
        f.write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d">%s</svg>'
                % (UPEM, UPEM, paths_xml))
    print("%-8s %d 个 path" % (name, len(ds)))

# ---------- 2. 构建字形（多 path 合并为一个字形） ----------
glyphs = {}
for i, name in enumerate(ICONS):
    code = 0xE600 + i
    pen = TTGlyphPen(None)
    cu2qu = Cu2QuPen(pen, max_err=0.5)
    # SVG y 轴向下，字体 y 轴向上：翻转 y 并平移
    tpen = TransformPen(cu2qu, Transform(1, 0, 0, -1, 0, UPEM))
    for d in icon_paths[name]:
        SVGPath.fromstring('<path d="%s"/>' % d).draw(tpen)
    glyphs["uni%04X" % code] = pen.glyph()

# .notdef 空字形（必须排在 glyphOrder 首位）
glyphs[".notdef"] = TTGlyphPen(None).glyph()
glyphs = {".notdef": glyphs.pop(".notdef"), **glyphs}

# ---------- 3. 组装字体 ----------
fb = FontBuilder(unitsPerEm=UPEM, isTTF=True)
glyph_order = list(glyphs.keys())
fb.setupGlyphOrder(glyph_order)
fb.setupCharacterMap({0xE600 + i: "uni%04X" % (0xE600 + i) for i in range(len(ICONS))})
fb.setupGlyf(glyphs)
fb.setupHorizontalMetrics({g: (UPEM, 0) for g in glyph_order})
fb.setupHorizontalHeader(ascent=896, descent=-128)
fb.setupNameTable({
    "familyName": "iconfont",
    "styleName": "Regular",
    "uniqueFontIdentifier": "iconfont-Regular",
    "fullName": "iconfont",
    "psName": "iconfont",
    "version": "Version 1.000",
})
fb.setupOS2(
    sTypoAscender=896, sTypoDescender=-128, sTypoLineGap=0,
    usWinAscent=896, usWinDescent=128,
    usWeightClass=400, usWidthClass=5,
)
fb.setupPost()
fb.save(os.path.join(BASE, "iconfont.ttf"))
print("iconfont.ttf 已生成")

# ---------- 4. 生成 WOFF / WOFF2 ----------
for flavor, fname in (("woff", "iconfont.woff"), ("woff2", "iconfont.woff2")):
    font = TTFont(os.path.join(BASE, "iconfont.ttf"))
    font.flavor = flavor
    font.save(os.path.join(BASE, fname))
    print(fname, "已生成")

# ---------- 5. 生成 iconfont.css（class 方式）----------
css = """@font-face {
  font-family: "iconfont";
  src: url('iconfont.woff2') format('woff2'),
       url('iconfont.woff') format('woff'),
       url('iconfont.ttf') format('truetype');
}

.iconfont {
  font-family: "iconfont" !important;
  font-size: 16px;
  font-style: normal;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
"""
for i, name in enumerate(ICONS):
    css += "\n.icon-%s:before { content: \"\\e%03x\"; }\n" % (name, 0x600 + i)
with open(os.path.join(BASE, "iconfont.css"), "w", encoding="utf-8") as f:
    f.write(css)
print("iconfont.css 已生成")

# ---------- 6. 生成 iconfont.js（SVG symbol 方式，fill 交给 currentColor）----------
symbols = []
for name in ICONS:
    paths_xml = "".join('<path d="%s"/>' % d for d in icon_paths[name])
    symbols.append(
        '<symbol id="icon-%s" viewBox="0 0 %d %d">%s</symbol>'
        % (name, UPEM, UPEM, paths_xml)
    )
sprite = ('<svg xmlns="http://www.w3.org/2000/svg" '
          'style="position:absolute;width:0;height:0;overflow:hidden" aria-hidden="true">'
          + "".join(symbols) + "</svg>")
sprite_js = "'" + sprite.replace("'", "\\'") + "'"

js = """(function (doc, win) {
  var sprite = %(sprite)s;
  var css = '.icon { width: 1em; height: 1em; vertical-align: -0.15em; fill: currentColor; overflow: hidden; }';
  function inject() {
    var style = doc.createElement('style');
    style.type = 'text/css';
    style.appendChild(doc.createTextNode(css));
    doc.head.appendChild(style);
    var div = doc.createElement('div');
    div.innerHTML = sprite;
    doc.body.appendChild(div.firstChild);
  }
  if (doc.readyState === 'loading') {
    doc.addEventListener('DOMContentLoaded', inject);
  } else {
    inject();
  }
})(document, window);
""" % {"sprite": sprite_js}
with open(os.path.join(BASE, "iconfont.js"), "w", encoding="utf-8") as f:
    f.write(js)
print("iconfont.js 已生成")
print("全部完成")
