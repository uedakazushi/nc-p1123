# nc-p1123 — 最小生成元次数 (1^n,2,3) のAS正則代数

**2026-11-19 / 統合版 v6。一般のAS正則Z-代数の完全分類は未完成。**

[研究方針](research/plan_ja.tex) → [統合公表用主論文](papers/nc-p1123.tex) → [研究ノート](research/notes_ja.tex) の順に読む。

公表用原稿は `papers/nc-p1123.tex` の1本に統合。重み `(1,1,2,3)`、語長二次、AS次元4のZ-代数について、**Z-domainなら標準Hilbert級数・1周期性・量子平面またはJordan平面上の2段Ore表示が従う**。Hilbert級数、周期性、noetherian性を追加仮定せず、noetherian性も結論として得る。完全な証明は `idx:thm:domain-standard` から `idx:thm:domain-ore` にある。

また全対象で、**Z-domain性は、選んだ語長斉次二次表示の重み2・語長1生成元 `z_0,...,z_6` が全次数で左右正則であることと同値**である（`idx:prop:z-regular-criterion`）。7周期性により調べる添字は七つで足りるが、有限次数までの単射性検査だけで十分とはしていない。

整域性を仮定しない全対象について、**標準関係数 `(1,2,2,1)` と標準二変数Hilbert級数が従い、Q=H=S** となる（`idx:thm:mixed-relation-ranks`, `idx:cor:all-standard`）。重み2・5の関係数は、七周期の漸化式とテンソル鎖の非消滅で解析的に強制する。重み3・4の関係数の証明は、行列Hilbert級数の成長から必要条件を導き、890個の整数列を厳密に検査して零列以外を排除する計算補助の証明である。有限次数のHilbert一致からAS正則性を認定してはいない。

整域部分の二つのOre表示については、**裸の添字保持同型の存在を、一つの可逆行列と有限個の条件で完全に判定できる**（`idx:thm:finite-isomorphism`）。量子平面・Jordan平面と零の導分項を同じ条件で扱う。対角量子族では、三係数 `(a,b,c)` への正規化後の同一視は恒等変換と `(a,b,c) -> (a^(-1),b^(-1),c*a^3/b^2)` だけである（`diag:thm:indexed-isomorphism`）。全特殊値を含み、対角族の同型類は三次元トーラスの有限商で与えられる。

一般の `(1^n,2,3)` 型については、左右noetherian・指定AS次元・指定Hilbert級数の下の数値拘束と、さらに語長二次・整域である場合の全Ore表示・次数付き同型を収録する。この任意nの定理の仮定を上記の n=2 の強化によって除去したとはしない。語長二次を仮定しない n=2 の仮定付きgraded Ore網羅定理、対角Ore表示パラメータの4既約成分、添字保持同型の不変量も含む。

現在の核心は、七つの `z_i` の左右消去子が全次数で零になるか、標準次元を持つ混合関係の射影が退化し得るか、および有限同型条件から一般の軌道の標準形・成分・特殊化を記述することである。最小周期7または非定数の射影階数列を持つ対象は必ず零因子を持つが、その存在は未確認。同型の存在判定と、非線型自己同型を含むモジュライスタックは区別する。

研究状態は [STATE](research/STATE.json)、先行文献は [BASELINE](research/BASELINE.md)、組版・計算の検証は [validation](research/validation.json) を参照する。

```bash
latexmk -lualatex -outdir=. papers/nc-p1123.tex
python3 scripts/check_project.py
python3 computations/verify_mixed_ranks.py
python3 -m pip install -r requirements-symbolic.txt
python3 computations/verify_skew_ore.py
```

VS Code の設定は `.latexmkrc` と `.vscode/settings.json`。組版は別途確認が必要。
