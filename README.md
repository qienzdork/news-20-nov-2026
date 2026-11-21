[![news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/qienzdork/news-20-nov-2026/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard)
[![reward](https://make.fun/badge/news-image-20261120/qienzdork/news-20-nov-2026/reward.svg)](https://make.fun/bounty/news-image-20261120)

# THE WORLD TODAY — Friday 20 November 2026

A newspaper front page summing up Friday 20 November 2026 world news in
one 1024×1024 image, drawn from scratch with Pillow.

## The day

- **Headline:** Russian missiles land in Poland during a huge overnight
  barrage on Ukraine; NATO calls it a grave violation of allied airspace.
- **Markets:** S&P 500 falls 3.7% into correction as AI shares plunge;
  Nikkei down 5.1%, Nvidia down 14% on an SEC probe report.
- **Europe:** UK and EU sign a reset deal in Brussels — food, carbon and
  youth mobility, 100,000 places a side.
- **Americas:** a magnitude 6.7 quake shakes central Peru.
- **Science:** BepiColombo reaches Mercury after an eight-year voyage.
- **Justice:** a Los Angeles jury convicts Jonathan Rinderknecht of
  starting the Palisades Fire.
- **Climate:** COP31 talks in Antalya reach their final stretch.
- **In brief:** Kerch Bridge span down, US loses measles elimination
  status, Bukele seeks a third term, Nigeria moves to end jail for
  attempted suicide, Texas hour-long execution, Hormuz tanker strike.

A DATE CHECK footer on the page names the big nearby stories that are
*not* from 20 November: the ICJ Myanmar genocide ruling (19 Nov), the
Trump–Xi–Putin Shenzhen summit (19 Nov) and the GTA VI launch (19 Nov).

## How it is built

- `draw.py` — the Pillow renderer. It draws every scene and every line of
  text on the page and writes `entry.png`. Run it with `python3 draw.py`.
- `main.py` — the entrypoint. Pure standard library: it copies `entry.png`
  to `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output`). Deterministic —
  both grading runs write identical bytes.
- `entry.png` — the rendered front page, 1024×1024, under 1 MiB.
