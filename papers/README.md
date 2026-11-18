# 公表用論文原稿

2026-11-18 / v3。

- [graded_ore_classification.tex](graded_ore_classification.tex) — 複素数体上、左右noetherian、指定Hilbert級数、最小生成元次数(1,1,2,3)の4次元AS正則graded代数を段階的Ore拡大で尽くす定理。有限係数条件、全三角形graded同型、語長二次部分の非対角チャートと同型判定、中心的な次数3最小生成元を持つ場合を扱う。
- [weighted_ore_strata.tex](weighted_ore_strata.tex) — 重み(1,1,2,3)の対角量子三生成元環上の斉次対角skew Ore拡大の必要十分条件、4表示成分、全ファイバー正則性とindexed同型不変量。

日本語LuaLaTeX。著者欄は空欄。証明は各原稿に集約し、研究用総合原稿から参照する。
新規性の最終調査、一般の二次AS正則Z-代数の完全分類、裸のindexed同型による全ての商は未完成。
graded分類の三角形同型条件を、そのまま裸のindexed同型条件として用いることはしない。
組版・計算・論理監査の実施範囲は [validation](../research/validation.json) を参照する。

再生成はリポジトリルートから行う。

```bash
latexmk -lualatex papers/weighted_ore_strata.tex
latexmk -lualatex papers/graded_ore_classification.tex
```

対角Ore表示の計算は `python3 -m pip install -r requirements-symbolic.txt` に続けて
`python3 computations/verify_skew_ore.py`。一般Ore網羅定理は、この有限計算とは別に原稿内で証明する。
