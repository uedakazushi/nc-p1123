# nc-p1123 — 最小生成元次数 (1^n,2,3) のAS正則代数

**2026-11-19 / 統合版 v7。n=1の添字付きOre表示・同型・周期を完全に決定。全nの単一graded代数への帰着は偽であり、n>=3の添字付きOre網羅性は未解決。**

[研究方針](research/plan_ja.tex) → [統合公表用主論文](papers/nc-p1123.tex) → [研究ノート](research/notes_ja.tex) の順に読む。

現在は、整域性を仮定して primitive jumps `(1^n,2,3)`、AS次元 `n+2` の語長二次Z-代数へ拡張する問題を扱う。**全対象が単一のgraded二段Ore代数の付随Z-代数になる、という任意nの主張は n=1 で偽**である。`genidx:thm:period-two-counterexample` に、標準Hilbert級数・語長Koszul性・左右noetherian性も満たすAS正則Z-整域で、最小周期が2となる例と完全な証明を記載した。この例は2周期の添字付きOre表示を持つため、Z-代数上のOre表示そのものの反例ではない。

**n=1の全対象については、添字付き二段Ore表示と裸の添字保持同型を完全に決定した**（`genidx:thm:one-light-ore`, `genidx:thm:one-light-classification`）。正規形は `zx=xz`, `wz=c zw`, `w_i x_(i+3)=x_i w_(i+1)+d_i z_i z_(i+2)`、ただし `c!=0`, `d_(2m)=c^(-m) alpha`, `d_(2m+1)=c^(-m) beta`。二つの正規形はcが一致し、`(alpha,beta)`が同時非零スカラー倍で一致するときに限り同型である。1周期性の必要十分条件は `alpha^2=c beta^2`（零の組を含む）で、その他の最小周期は2。この構成の全てが語長Koszul・標準Hilbert・左右noetherianなAS3 Z-domainとなることも、一般パラメータの解消で証明した。

公表用原稿は `papers/nc-p1123.tex` の1本に統合。重み `(1,1,2,3)`、語長二次、AS次元4のZ-代数について、**Z-domainなら標準Hilbert級数・1周期性・量子平面またはJordan平面上の2段Ore表示が従う**。Hilbert級数、周期性、noetherian性を追加仮定せず、noetherian性も結論として得る。完全な証明は `idx:thm:domain-standard` から `idx:thm:domain-ore` にある。

また全対象で、**Z-domain性は、選んだ語長斉次二次表示の重み2・語長1生成元 `z_0,...,z_6` が全次数で左右正則であることと同値**である（`idx:prop:z-regular-criterion`）。7周期性により調べる添字は七つで足りるが、有限次数までの単射性検査だけで十分とはしていない。

整域性を仮定しない全対象について、**標準関係数 `(1,2,2,1)` と標準二変数Hilbert級数が従い、Q=H=S** となる（`idx:thm:mixed-relation-ranks`, `idx:cor:all-standard`）。重み2・5の関係数は、七周期の漸化式とテンソル鎖の非消滅で解析的に強制する。重み3・4の関係数の証明は、行列Hilbert級数の成長から必要条件を導き、890個の整数列を厳密に検査して零列以外を排除する計算補助の証明である。有限次数のHilbert一致からAS正則性を認定してはいない。

整域部分の二つのOre表示については、**裸の添字保持同型の存在を、一つの可逆行列と有限個の条件で完全に判定できる**（`idx:thm:finite-isomorphism`）。量子平面・Jordan平面と零の導分項を同じ条件で扱う。対角量子族では、三係数 `(a,b,c)` への正規化後の同一視は恒等変換と `(a,b,c) -> (a^(-1),b^(-1),c*a^3/b^2)` だけである（`diag:thm:indexed-isomorphism`）。全特殊値を含み、対角族の同型類は三次元トーラスの有限商で与えられる。

一般の `(1^n,2,3)` 型については、左右noetherian・指定AS次元・指定Hilbert級数の下の数値拘束と、さらに語長二次・整域である場合の全Ore表示・次数付き同型を収録する。この任意nの定理の仮定を上記の n=2 の強化によって除去したとはしない。語長二次を仮定しない n=2 の仮定付きgraded Ore網羅定理、対角Ore表示パラメータの4既約成分、添字保持同型の不変量も含む。

未解決のn>=3では、整域性から混合関係数・正規元族・基礎Z-代数のAS性を導き、添字付き二段Ore表示の網羅性を証明できるかが核心である。Hilbert級数・noetherian性・1周期性は追加許可された仮定として扱わない。n=1の `E^1 × E^2`、n=2の `E^2 × E^2` 対合によるKoszul性の強制は、そのまま一般次元へ移らない。研究ノートには、一般AS平行移動、関係数を仮定した正規元族、および基礎代数のAS性を仮定した一重生成元のOre補題を完全な証明とともに残す。

元のn=2の全分類では、整域性の自動性、零因子を持つ枝、一般の軌道の幾何は引き続き未解決である。n=2で最小周期7または非定数の射影階数列を持つ対象は必ず零因子を持つ、という結果を、今回のn=1の整域反例へ適用しない。同型の存在判定と、非線型自己同型を含むモジュライスタックも区別する。

研究状態は [STATE](research/STATE.json)、先行文献は [BASELINE](research/BASELINE.md)、組版・計算の検証は [validation](research/validation.json) を参照する。

```bash
latexmk -lualatex -outdir=. papers/nc-p1123.tex
python3 scripts/check_project.py
python3 computations/verify_mixed_ranks.py
python3 -m pip install -r requirements-symbolic.txt
python3 computations/verify_skew_ore.py
```

VS Code の設定は `.latexmkrc` と `.vscode/settings.json`。組版は別途確認が必要。
