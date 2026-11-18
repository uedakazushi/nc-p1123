# 公表用論文原稿

2026-11-18 / v2。最初の独立した短報：

- [weighted_ore_strata.tex](weighted_ore_strata.tex) — 重み(1,1,2,3)の対角量子三生成元環上の斉次対角skew Ore拡大の必要十分条件、4表示成分、全ファイバー正則性とindexed同型不変量。

日本語LuaLaTeX。著者欄は空欄。原稿は5ページに組版確認済み。
新規性の最終調査、完全なAS正則モジュライ分類、各成分の同型類商は未完成。
主張を研究用総合原稿で重複証明せず、本稿を証明の正本とする。
再生成：リポジトリルートから `latexmk -lualatex papers/weighted_ore_strata.tex`。
計算：`python3 -m pip install -r requirements-symbolic.txt` に続けて `python3 computations/verify_skew_ore.py`。
