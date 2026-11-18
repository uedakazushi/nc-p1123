# nc-p1123 — 最小生成元次数 (1^n,2,3) のAS正則代数

**2026-11-19 / 統合版 v3。一般のAS正則Z-代数の完全分類は未完成。**

[研究方針](research/plan_ja.tex) → [統合公表用主論文](papers/nc-p1123.tex) → [研究ノート](research/notes_ja.tex) の順に読む。

公表用原稿は `papers/nc-p1123.tex` の1本に統合。重み `(1,1,2,3)`、語長二次、AS次元4のZ-代数について、**Z-domainなら標準Hilbert級数・1周期性・量子平面またはJordan平面上の2段Ore表示が従う**。Hilbert級数、周期性、noetherian性を追加仮定せず、noetherian性も結論として得る。完全な証明は `idx:thm:domain-standard` から `idx:thm:domain-ore` にある。

一般の `(1^n,2,3)` 型については、左右noetherian・指定AS次元・指定Hilbert級数の下の数値拘束と、さらに語長二次・整域である場合の全Ore表示・次数付き同型を収録する。この任意nの定理の仮定を上記の n=2 の強化によって除去したとはしない。語長二次を仮定しない n=2 の仮定付きgraded Ore網羅定理、対角Ore表示パラメータの4既約成分、添字保持同型の不変量も含む。

現在の核心は、全対象で整域性が自動的に従うか、零因子を持つ枝でも標準Hilbert級数が強制されるか、および整域部分の裸の添字保持同型の軌道である。非標準型、最小周期7、非定数の射影階数列を持つ対象は必ず零因子を持つが、その存在は未確認。graded同型分類だけでは、Zhang twistも同一視される裸のindexed分類は完成しない。

研究状態は [STATE](research/STATE.json)、先行文献は [BASELINE](research/BASELINE.md)、組版・計算の検証は [validation](research/validation.json) を参照する。

```bash
latexmk -lualatex -outdir=. papers/nc-p1123.tex
python3 scripts/check_project.py
python3 -m pip install -r requirements-symbolic.txt
python3 computations/verify_skew_ore.py
```

VS Code の設定は `.latexmkrc` と `.vscode/settings.json`。組版は別途確認が必要。
