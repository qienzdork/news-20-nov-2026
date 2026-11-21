#!/usr/bin/env python3
"""Draw the 20 November 2026 front page: THE WORLD TODAY.

Renders a 1024x1024 newspaper front page summing up Friday 20 November
2026 world news, verified against live reporting. Every story on the page
happened, or was first reported, on 20 November 2026; the DATE CHECK footer
names the big nearby stories that are NOT from that day.
"""
import os

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")

PAPER = (248, 244, 233)
INK = (22, 21, 19)
RED = (158, 27, 27)
NAVY = (22, 50, 79)
STEEL = (58, 84, 112)
GOLD = (184, 138, 29)
GREY = (90, 86, 78)
LIGHT = (233, 227, 211)
SKY = (16, 34, 58)
FIRE = (232, 122, 26)

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width):
    """Greedy word wrap to a pixel width; returns a list of lines."""
    lines, cur = [], ""
    for word in text.split(" "):
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def text_block(draw, x, y, text, fnt, fill=INK, width=600, leading=1.25):
    """Draw wrapped text; returns the y just below the last line."""
    size = fnt.size
    for line in wrap(draw, text, fnt, width):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += int(size * leading)
    return y


def rule(draw, x0, y, x1, width=2, fill=INK):
    draw.line([(x0, y), (x1, y)], fill=fill, width=width)


def centre(draw, y, text, fnt, fill=INK, cx=W // 2):
    w = draw.textlength(text, font=fnt)
    draw.text((cx - w / 2, y), text, font=fnt, fill=fill)
    return y + fnt.size


img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)
d.rectangle([0, 0, W - 1, H - 1], outline=INK, width=4)

# ---- Masthead ------------------------------------------------------------
rule(d, 14, 12, W - 14, width=5, fill=INK)
rule(d, 14, 20, W - 14, width=2, fill=RED)
centre(d, 28, "THE WORLD TODAY", font(SERIF_B, 62), INK)
centre(d, 96, "FRIDAY, 20 NOVEMBER 2026", font(SANS_B, 25), RED)
d.text((30, 100), "ONE DAY. THE WHOLE WORLD.", font=font(SANS_B, 14), fill=GREY)
right = "WORLD CHILDREN'S DAY"
d.text((W - 30 - d.textlength(right, font=font(SANS_B, 14)), 100),
       right, font=font(SANS_B, 14), fill=GREY)
rule(d, 14, 132, W - 14, width=3, fill=INK)

# ---- Headline story: Russian missiles land in Poland ---------------------
d.text((30, 146), "EUROPE  •  WAR IN UKRAINE", font=font(SANS_B, 16), fill=RED)
d.text((30, 168), "RUSSIAN MISSILES", font=font(SERIF_B, 46), fill=INK)
d.text((30, 216), "LAND IN POLAND", font=font(SERIF_B, 46), fill=INK)
d.text((30, 268), "Deadly barrage hits Kyiv; NATO calls it a grave violation",
       font=font(SANS, 18), fill=GREY)

# Drawn scene: night sky, missile trails, blast over a town silhouette.
SX, SY, SW, SH = 30, 296, 596, 148
d.rectangle([SX, SY, SX + SW, SY + SH], fill=SKY)
for px, py, r in [(70, 310, 2), (150, 322, 1), (240, 308, 2), (330, 320, 1),
                  (420, 312, 2), (500, 324, 1), (570, 310, 2), (110, 336, 1),
                  (290, 334, 1), (470, 338, 1)]:
    d.ellipse([px - r, py - r, px + r, py + r], fill=(220, 225, 235))
# two missile trails arcing down to the blast
d.line([(120, 300), (300, 392), (470, 428)], fill=(255, 205, 120), width=3)
d.line([(520, 300), (480, 380), (460, 424)], fill=(255, 205, 120), width=3)
for cx, cy, r, col in [(470, 428, 26, FIRE), (470, 428, 16, (255, 190, 60)),
                       (470, 428, 8, (255, 240, 160))]:
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=col)
# town silhouette
for bx, bw, bh in [(40, 60, 26), (110, 44, 34), (170, 70, 22), (500, 56, 30),
                   (566, 50, 24)]:
    d.rectangle([SX + bx, SY + SH - bh, SX + bx + bw, SY + SH], fill=(8, 18, 32))
d.polygon([(SX + 110, SY + SH - 34), (SX + 132, SY + SH - 48),
           (SX + 154, SY + SH - 34)], fill=(8, 18, 32))
d.text((SX + 8, SY + SH - 22), "POLAND", font=font(SANS_B, 13),
       fill=(255, 240, 200))

# Summary column beside the scene.
bx = 648
y = text_block(d, bx, 296,
               "Two Russian missiles and a drone came down in Polish fields "
               "during a huge overnight barrage on Ukraine.",
               font(SANS, 16), width=346, leading=1.25)
y = text_block(d, bx, y + 6,
               "Three Kyiv bridges hit. Poland called it deliberate; NATO, "
               "a grave violation.",
               font(SANS, 16), width=346, leading=1.25)
text_block(d, bx, y + 6, "No one was hurt in Poland.",
           font(SANS_B, 16), width=346, leading=1.25)
rule(d, 14, 458, W - 14, width=2, fill=INK)

# ---- Stat strip: markets --------------------------------------------------
d.rectangle([14, 466, W - 14, 506], fill=NAVY)
d.text((28, 476), "MARKETS", font=font(SANS_B, 17), fill=(255, 205, 120))
stats = ("S&P 500  6,910  ▼3.7%      NIKKEI  ▼5.1%      BRENT  $89.87  ▲0.5%"
         "      NVIDIA  ▼14%")
d.text((150, 478), stats, font=font(SANS_B, 15), fill=(245, 244, 238))
centre(d, 514, "THE DAY IN PICTURES", font(SANS_B, 15), GREY)

# ---- Pictured stories: six drawn scenes -----------------------------------
def scene_chart(x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(24, 40, 60))
    for gx in range(x + 40, x + w, 40):
        d.line([(gx, y + 8), (gx, y + h - 8)], fill=(52, 74, 96), width=1)
    for gy in range(y + 16, y + h, 22):
        d.line([(x + 8, gy), (x + w - 8, gy)], fill=(52, 74, 96), width=1)
    pts = [(x + 12, y + 14), (x + 60, y + 22), (x + 100, y + 18),
           (x + 150, y + 34), (x + 190, y + 30), (x + 235, y + 52),
           (x + 280, y + 70)]
    d.line(pts, fill=(232, 70, 60), width=4)
    d.polygon([(x + 280, y + 70), (x + 266, y + 62), (x + 266, y + 78)],
              fill=(232, 70, 60))


def scene_flags(x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=LIGHT)
    # Union Jack, simplified: blue field, white saltire and cross, red cross.
    ux, uy, uw, uh = x + 14, y + 12, 118, 58
    d.rectangle([ux, uy, ux + uw, uy + uh], fill=(28, 52, 110))
    d.line([(ux, uy), (ux + uw, uy + uh)], fill=(245, 244, 238), width=9)
    d.line([(ux + uw, uy), (ux, uy + uh)], fill=(245, 244, 238), width=9)
    d.line([(ux + uw // 2, uy), (ux + uw // 2, uy + uh)], fill=(245, 244, 238), width=13)
    d.line([(ux, uy + uh // 2), (ux + uw, uy + uh // 2)], fill=(245, 244, 238), width=13)
    d.line([(ux + uw // 2, uy), (ux + uw // 2, uy + uh)], fill=(200, 40, 50), width=7)
    d.line([(ux, uy + uh // 2), (ux + uw, uy + uh // 2)], fill=(200, 40, 50), width=7)
    # EU flag: blue field, ring of gold stars.
    ex, ey, ew, eh = x + 176, y + 12, 118, 58
    d.rectangle([ex, ey, ex + ew, ey + eh], fill=(18, 52, 110))
    import math as _m
    for i in range(12):
        a = 2 * _m.pi * i / 12 - _m.pi / 2
        sx = ex + ew // 2 + int(20 * _m.cos(a))
        sy = ey + eh // 2 + int(15 * _m.sin(a))
        d.ellipse([sx - 2, sy - 2, sx + 2, sy + 2], fill=(255, 205, 60))


def scene_quake(x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(214, 196, 160))
    d.rectangle([x, y + h - 34, x + w, y + h], fill=(146, 118, 84))
    crack = [(x + 150, y + 6), (x + 138, y + 26), (x + 158, y + 44),
             (x + 140, y + 62), (x + 152, y + h - 34)]
    d.line(crack, fill=(70, 52, 34), width=4)
    # tilted house: leaning walls, small roof, second small building
    d.polygon([(x + 30, y + 46), (x + 92, y + 40), (x + 96, y + h - 30),
               (x + 34, y + h - 30)], fill=(178, 96, 60))
    d.polygon([(x + 24, y + 48), (x + 62, y + 30), (x + 100, y + 42),
               (x + 92, y + 40), (x + 30, y + 46)], fill=(120, 50, 40))
    d.polygon([(x + 200, y + 56), (x + 244, y + 52), (x + 246, y + h - 30),
               (x + 202, y + h - 30)], fill=(150, 84, 56))
    d.polygon([(x + 196, y + 58), (x + 224, y + 44), (x + 250, y + 54),
               (x + 244, y + 52), (x + 200, y + 56)], fill=(110, 46, 38))
    for dx, dy in [(210, 20), (240, 40), (270, 16), (200, 56), (255, 62)]:
        d.ellipse([x + dx - 2, y + dy - 2, x + dx + 2, y + dy + 2],
                  fill=(120, 100, 70))


def scene_mercury(x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(10, 14, 26))
    for px, py, r in [(30, 18, 1), (90, 30, 2), (250, 16, 1), (280, 44, 2),
                      (60, 66, 1), (200, 60, 1)]:
        d.ellipse([x + px - r, y + py - r, x + px + r, y + py + r],
                  fill=(220, 225, 235))
    cx, cy, r = x + 210, y + 52, 34
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(168, 160, 148))
    for ox, oy, orad in [(196, 40, 7), (224, 62, 9), (202, 68, 5), (230, 36, 4)]:
        d.ellipse([x + ox - orad, y + oy - orad, x + ox + orad, y + oy + orad],
                  fill=(140, 132, 120))
    # small probe: gold panels, white body, dish
    d.rectangle([x + 62, y + 34, x + 78, y + 52], fill=(245, 244, 238))
    d.rectangle([x + 40, y + 38, x + 62, y + 48], fill=(212, 160, 40))
    d.rectangle([x + 78, y + 38, x + 100, y + 48], fill=(212, 160, 40))
    d.line([(x + 70, y + 34), (x + 70, y + 22)], fill=(245, 244, 238), width=2)
    d.ellipse([x + 64, y + 14, x + 76, y + 24], fill=(245, 244, 238))


def scene_gavel(x, y, w, h):
    import math as _m
    d.rectangle([x, y, x + w, y + h], fill=(238, 230, 214))
    # handle: thick diagonal line
    d.line([(x + 52, y + 56), (x + 196, y + 18)], fill=(122, 82, 44), width=11)
    # head: small rectangle rotated 20 degrees, drawn as a polygon
    cx, cy = x + 212, y + 16
    hw, hh, a = 34, 13, _m.radians(20)
    ca, sa = _m.cos(a), _m.sin(a)
    pts = []
    for sx, sy in [(-hw, -hh), (hw, -hh), (hw, hh), (-hw, hh)]:
        pts.append((cx + sx * ca - sy * sa, cy + sx * sa + sy * ca))
    d.polygon(pts, fill=(96, 60, 30))
    d.polygon([(cx - hw, cy - hh), (cx - hw + 8, cy - hh + 2),
               (cx - hw + 8, cy + hh - 2), (cx - hw, cy + hh)],
              fill=(150, 104, 58))
    # sound block
    d.rectangle([x + 108, y + h - 16, x + 212, y + h - 6], fill=(96, 60, 30))


def scene_cop(x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(206, 226, 238))
    cx, cy, r = x + w // 2, y + 46, 32
    for ang in range(0, 360, 30):
        import math as _m
        a = _m.radians(ang)
        d.line([(cx + int(38 * _m.cos(a)), cy + int(38 * _m.sin(a))),
                (cx + int(48 * _m.cos(a)), cy + int(48 * _m.sin(a)))],
               fill=(212, 160, 40), width=3)
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(52, 110, 168))
    d.ellipse([cx - 18, cy - 12, cx - 2, cy + 4], fill=(88, 150, 90))
    d.ellipse([cx + 2, cy + 6, cx + 20, cy + 20], fill=(88, 150, 90))
    d.ellipse([cx - 8, cy - 26, cx + 8, cy - 12], fill=(88, 150, 90))


def cell(x, y, scene, kicker, headline, body):
    scene(x, y, 308, 76)
    d.text((x, y + 84), kicker, font=font(SANS_B, 13), fill=RED)
    yy = text_block(d, x, y + 100, headline, font(SANS_B, 19), width=308,
                    leading=1.12)
    text_block(d, x, yy + 2, body, font(SANS, 14), fill=(40, 38, 34),
               width=308, leading=1.2)


cell(30, 540, scene_chart, "ECONOMY", "WALL ST IN CORRECTION",
     "S&P 500 falls 3.7% as AI shares plunge; Nasdaq gives up all of 2026's gains.")
cell(358, 540, scene_flags, "EUROPE", "UK AND EU SIGN RESET DEAL",
     "Food, carbon and youth-mobility pacts agreed in Brussels; 100,000 places a side.")
cell(686, 540, scene_quake, "AMERICAS", "M6.7 QUAKE HITS PERU",
     "Strong tremor shakes central Peru on Friday evening, centred near Carhuamayo.")
cell(30, 728, scene_mercury, "SCIENCE", "BEPICOLOMBO REACHES MERCURY",
     "European-Japanese probe arrives after an eight-year voyage through space.")
cell(358, 728, scene_gavel, "JUSTICE", "GUILTY: PALISADES FIRE",
     "Los Angeles jury convicts Jonathan Rinderknecht of starting the blaze.")
cell(686, 728, scene_cop, "CLIMATE", "COP31 IN FINAL STRETCH",
     "Antalya talks haggle over fossil fuels and funding as the deadline nears.")
rule(d, 14, 914, W - 14, width=2, fill=INK)

# ---- In brief ---------------------------------------------------------------
d.text((30, 922), "IN BRIEF", font=font(SANS_B, 14), fill=RED)
brief = ("Kerch Bridge span down after Ukrainian strike  •  US loses measles "
         "elimination status  •  Bukele seeks third term  •  Nigeria ends jail "
         "for attempted suicide  •  Texas execution draws scrutiny  •  Hormuz "
         "tanker hit by strike")
text_block(d, 140, 922, brief, font(SANS, 14), width=854, leading=1.25)

# ---- Date check footer -------------------------------------------------------
rule(d, 14, 972, W - 14, width=2, fill=RED)
check = ("DATE CHECK — Every story above happened, or was first reported, on "
         "Friday 20 November 2026.  NOT 20 NOVEMBER: the ICJ Myanmar genocide "
         "ruling (19 Nov)  •  the Trump–Xi–Putin Shenzhen summit (19 Nov)  •  "
         "the GTA VI launch (19 Nov).")
text_block(d, 30, 980, check, font(SANS_B, 13), fill=INK, width=964,
           leading=1.3)

img.save(OUT, "PNG", optimize=True)
print("saved", OUT, os.path.getsize(OUT), "bytes")
