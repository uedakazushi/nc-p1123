# nc-p1123 — 最小生成元次数 (1^n,2,3) のAS正則代数

**2026-11-19 / 統合版 v2。一般のAS正則Z-代数の完全分類は未完成。**

[研究方針](research/plan_ja.tex) → [統合公表用主論文](papers/nc-p1123.tex) → [研究ノート](research/notes_ja.tex) の順に読む。

公表用原稿は `papers/nc-p1123.tex` の1本に統合。一般の `(1^n,2,3)` 型について数値拘束、語長二次の場合の全Ore表示・次数付き同型を与え、特殊次元 `n=2` については語長二次を仮定しないgraded Ore網羅定理と、対角Ore表示パラメータの4既約成分および添字保持同型の不変量を収録する。

**注意**：通常のgraded代数の同型分類は、一般のAS正則Z-代数の添字保持同型分類の完成を意味しない。後者は研究方針・研究ノートに未解決課題として残す。

研究状態は [STATE](research/STATE.json)、先行文献は [BASELINE](research/BASELINE.md)、組版・計算の検証は [validation](research/validation.json) を参照する。

```bash
latexmk -lualatex -outdir=. papers/nc-p1123.tex
python3 scripts/check_project.py
python3 -m pip install -r requirements-symbolic.txt
python3 computations/verify_skew_ore.py
```

VS Code の設定は `.latexmkrc` と `.vscode/settings.json`。組版は別途確認が必要。
