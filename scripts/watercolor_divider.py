"""Procedural watercolor dividers for zhuoliyin.github.io.
Each shape is a wet wash: warped edge, pigment pooling at the rim, granulation,
and a bleed into mist toward its base. Washes are glazed with multiply blending
on the site's paper color (light) or laid over the dark paper (dark)."""
import math, sys
import numpy as np
from PIL import Image, ImageDraw
from scipy.ndimage import gaussian_filter, map_coordinates

W, H = 2400, 460
PAPER_L = np.array([0xfa, 0xfa, 0xf8]) / 255
PAPER_D = np.array([0x16, 0x15, 0x14]) / 255
YY, XX = np.mgrid[0:H, 0:W].astype(np.float32)

def noise(seed, sigma):
    r = np.random.default_rng(seed).standard_normal((H, W)).astype(np.float32)
    n = gaussian_filter(r, sigma, mode="wrap")
    n -= n.min(); n /= n.max() + 1e-9
    return n

def fbm(seed, sigmas=(60, 24, 8), weights=(0.55, 0.3, 0.15)):
    return sum(w * noise(seed + i * 101, s) for i, (s, w) in enumerate(zip(sigmas, weights)))

GRAIN = noise(7, 0.8)
GRAIN2 = noise(8, 2.2)
_r = np.random.default_rng(9).standard_normal((H, W)).astype(np.float32)
STREAK = gaussian_filter(_r, (36, 2.5), mode="wrap"); STREAK -= STREAK.min(); STREAK /= STREAK.max()

def poly_mask(points):
    img = Image.new("L", (W * 2, H * 2), 0)
    ImageDraw.Draw(img).polygon([(x * 2, y * 2) for x, y in points], fill=255)
    return np.asarray(img.resize((W, H), Image.LANCZOS), np.float32) / 255

def ellipse_mask(cx, cy, rx, ry):
    return np.clip(1 - ((XX - cx) / rx) ** 2 - ((YY - cy) / ry) ** 2, 0, 1) ** 0.15 * (((XX - cx) / rx) ** 2 + ((YY - cy) / ry) ** 2 < 1)

def warp(m, seed, amp):
    dx = (noise(seed, 14) - 0.5) * 2 * amp + (noise(seed + 1, 3) - 0.5) * amp * 0.6
    dy = (noise(seed + 2, 14) - 0.5) * 2 * amp + (noise(seed + 3, 3) - 0.5) * amp * 0.6
    return map_coordinates(m, [YY + dy, XX + dx], order=1, mode="constant")

def smooth(a, b, t):
    t = np.clip((t - a) / (b - a), 0, 1)
    return t * t * (3 - 2 * t)

def wash(mask, density, seed, fade=None, edge=1.0, wobble=5, soft=1.0, streak=0.0):
    m = warp(mask, seed, wobble)
    m = gaussian_filter(m, soft)
    rim = np.clip(m - gaussian_filter(m, 7), 0, 1)
    body = 0.62 + 0.5 * fbm(seed + 9)
    d = m * density * body + rim * density * 1.6 * edge
    d *= 0.8 + 0.2 * GRAIN * 1.0 + 0.08 * (GRAIN2 - 0.5)
    if streak:
        d *= 1 - streak + streak * 1.5 * STREAK
    if fade is not None:
        y0, y1 = fade
        jitter = (fbm(seed + 17, (40, 12), (0.7, 0.3)) - 0.5) * (y1 - y0) * 0.9
        f = 1 - smooth(y0, y1, YY + jitter)
        # wet bleed: the faded zone softens and spreads a little
        d = d * f + gaussian_filter(d, 6) * (1 - f) * 0.35 * (1 - smooth(y0, y1 + 40, YY))
    return np.clip(d, 0, 1)

class Painting:
    def __init__(self):
        self.layers = []  # (density field, light pigment, dark pigment)

    def add(self, d, light, dark):
        self.layers.append((d, np.array(light), np.array(dark)))

    def render(self, mode, side_seed=5):
        c = np.broadcast_to(PAPER_L if mode == "light" else PAPER_D, (H, W, 3)).copy()
        for d, light, dark in self.layers:
            d3 = d[..., None]
            if mode == "light":
                c *= 1 - d3 * (1 - light)
            else:
                c += d3 * 0.85 * (dark - c)
        # dissolve the ends and the base into the paper so the band has no hard edge
        n = (fbm(side_seed, (50, 15), (0.7, 0.3)) - 0.5) * 140
        side = smooth(0, 300, XX + n) * smooth(0, 300, W - XX + n)
        base = 1 - smooth(H - 120, H - 8, YY + n * 0.4)
        k = (side * base)[..., None]
        paper = PAPER_L if mode == "light" else PAPER_D
        c = paper + (c - paper) * k
        return Image.fromarray((np.clip(c, 0, 1) * 255).astype(np.uint8))

# ---------------------------------------------------------------- palette
# light = transmittance for glazing on paper; dark = luminous pigment on dark paper
GARNET  = ((0.62, 0.20, 0.26), (0.80, 0.42, 0.46))
ROSE    = ((0.86, 0.62, 0.66), (0.62, 0.40, 0.44))
MAUVE   = ((0.70, 0.56, 0.64), (0.52, 0.40, 0.48))
SLATE   = ((0.70, 0.74, 0.84), (0.42, 0.46, 0.56))
WARMGRY = ((0.80, 0.76, 0.72), (0.46, 0.43, 0.40))
PEACH   = ((0.97, 0.76, 0.66), (0.70, 0.48, 0.40))
INK     = ((0.42, 0.34, 0.36), (0.74, 0.66, 0.64))

# ---------------------------------------------------------------- A: mountains
def mountains():
    p = Painting()
    sun = wash(ellipse_mask(1330, 105, 58, 58), 0.55, 40, edge=0.6, wobble=3, soft=2)
    p.add(sun, *ROSE)
    rng = np.random.default_rng(3)
    specs = [  # base, peak height, n peaks, width range, color, density, seed
        (235, 120, 3, (150, 260), SLATE, 0.40, 14),
        (290, 140, 5, (130, 240), MAUVE, 0.48, 21),
        (330, 120, 6, (110, 200), ROSE, 0.55, 31),
        (370, 85, 6, (90, 170), GARNET, 0.42, 41),
        (410, 45, 8, (70, 140), INK, 0.40, 51),
    ]
    xs = np.arange(-20, W + 21, 4)
    for base, ph, n, wr, color, dens, seed in specs:
        r = np.random.default_rng(seed)
        y = np.full(xs.shape, float(base))
        for _ in range(n):
            cx, w, a = r.uniform(150, W - 150), r.uniform(*wr), r.uniform(0.55, 1.0)
            y -= ph * a * np.exp(-(np.abs(xs - cx) / w) ** 1.25)
        y = np.maximum(y, 40 + 20 * np.tanh((y - 40) / 20))
        y += (np.interp(xs, np.arange(0, W + 40, 20), r.normal(0, 3.5, (W + 40) // 20)))
        pts = list(zip(xs, y)) + [(W + 20, H + 20), (-20, H + 20)]
        crest = y.min()
        d = wash(poly_mask(pts), dens, seed, fade=(crest + (base - crest) * 0.55, base + 30), wobble=4)
        p.add(d, *color)
    return p

# ---------------------------------------------------------------- B: Columbia skyline
def rect(x0, y0, x1, y1):
    return [(x0, y0), (x1, y0), (x1, y1), (x0, y1)]

def columbia():
    p = Painting()
    G = 400  # ground line
    sun = wash(ellipse_mask(1930, 110, 56, 56), 0.5, 40, edge=0.6, wobble=3, soft=2)
    p.add(sun, *PEACH)

    def bld(points, color, dens, seed, top=None):
        top = min(y for _, y in points) if top is None else top
        p.add(wash(poly_mask(points), dens, seed, fade=(top + (G - top) * 0.62, G + 25), wobble=3.5, streak=0.35), *color)

    def flat(x0, x1, top, color, dens, seed):
        bld(rect(x0, top, x1, G), color, dens, seed)
    back = [(600, 700, 230, SLATE), (690, 770, 190, MAUVE), (760, 850, 250, ROSE), (840, 920, 160, SLATE),
            (995, 1070, 175, WARMGRY), (1140, 1220, 205, GARNET), (1210, 1300, 170, MAUVE),
            (1290, 1380, 225, SLATE), (1370, 1450, 195, PEACH), (1440, 1520, 250, ROSE)]
    for i, (x0, x1, t, c) in enumerate(back):
        flat(x0, x1, t, c, 0.36, 200 + i)
    bld([(1060, 160), (1150, 135), (1150, G), (1060, G)], SLATE, 0.42, 220)
    # Capitol Center: the tallest tower, stepped crown
    cc = [(920, 118), (940, 118), (940, 96), (980, 96), (980, 118), (1000, 118), (1000, G), (920, G)]
    bld(cc, MAUVE, 0.55, 221, top=96)
    front = [(580, 660, 300, PEACH), (720, 800, 290, MAUVE), (880, 950, 280, PEACH), (1030, 1110, 300, ROSE),
             (1180, 1260, 285, PEACH), (1330, 1410, 295, MAUVE), (1480, 1560, 310, SLATE),
             (1860, 1940, 300, MAUVE), (1930, 2010, 325, PEACH)]
    for i, (x0, x1, t, c) in enumerate(front):
        flat(x0, x1, t, c, 0.42, 240 + i)
    # State House: wide colonnaded body, drum, dome, lantern
    sh = [(1620, 300), (1700, 300), (1700, 285), (1760, 285), (1760, 300), (1840, 300), (1840, G), (1620, G)]
    bld(sh, WARMGRY, 0.55, 113, top=285)
    drum = rect(1700, 230, 1760, 290)
    bld(drum, WARMGRY, 0.5, 114, top=230)
    dome = [(1700 + 30 + 34 * math.cos(t), 232 - 46 * math.sin(t)) for t in np.linspace(0, math.pi, 40)]
    bld(dome, SLATE, 0.6, 115, top=186)
    bld(rect(1724, 160, 1736, 190), SLATE, 0.6, 116, top=160)
    # Gervais Street Bridge over the Congaree, far left
    deck = 330
    bridge = [(250, deck), (560, deck), (560, deck + 14)]
    xs = np.linspace(560, 250, 120)
    for x in xs:
        k = ((x - 250) / 310 * 5) % 1
        bridge.append((x, deck + 62 - 40 * math.sin(math.pi * k) ** 0.7))
    bridge += [(250, deck + 62)]
    p.add(wash(poly_mask(bridge + [(250, deck)]), 0.45, 120, fade=(deck + 40, G + 20), wobble=2.5), *ROSE)
    river = wash(poly_mask([(150, 392), (700, 382), (900, 402), (150, 410)]), 0.25, 121, edge=0.4, wobble=6, soft=4)
    p.add(river, *SLATE)
    # palmettos: thin trunk, a fan of fronds
    for x0, h, seed in ((470, 150, 130), (2110, 175, 131), (2180, 130, 132), (1585, 120, 133)):
        top = G - h
        trunk = [(x0 - 4, G), (x0 - 2, top + 4), (x0 + 2, top + 4), (x0 + 4, G)]
        fronds = []
        r = np.random.default_rng(seed)
        for a in np.linspace(-3.45, 0.3, 17):
            a += r.normal(0, 0.06)
            L = r.uniform(30, 46)
            droop = 16 * math.cos(a) ** 2
            tip = (x0 + L * math.cos(a), top + L * math.sin(a) + droop)
            mid = lambda s_: (x0 + 0.55 * L * math.cos(a + s_), top + 0.55 * L * math.sin(a + s_) + droop * 0.3)
            fronds += [(x0, top), mid(-0.16), tip, mid(0.16)]
        m = poly_mask(trunk)
        for i in range(0, len(fronds), 4):
            m = np.maximum(m, poly_mask(fronds[i:i + 4]))
        p.add(wash(m, 0.55, seed, fade=(top + h * 0.6, G + 20), wobble=1.6, soft=0.8, edge=0.6), *INK)
    return p

if __name__ == "__main__":
    out = sys.argv[1]
    for name, fn in (("mountains", mountains), ("columbia", columbia)):
        p = fn()
        for mode in ("light", "dark"):
            p.render(mode).save(f"{out}/divider-{name}-{mode}.webp", quality=84, method=6)
            print(name, mode)
