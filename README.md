# nc-p1123 — 最小生成元次数 (1^n,2,3) のAS正則代数

**2026-11-19 / 統合版 v8。n=3の数値型・Koszul性・2周期性を証明。任意nで純jump 1部分がAS正則なら添字付き二段Ore表示が成立。基礎部分のAS性を元の仮定から導くことが残る。**

[研究方針](research/plan_ja.tex) → [統合公表用主論文](papers/nc-p1123.tex) → [研究ノート](research/notes_ja.tex) の順に読む。

現在は、整域性を仮定して primitive jumps `(1^n,2,3)`、AS次元 `n+2` の語長二次Z-代数へ拡張する問題を扱う。**全対象が単一のgraded二段Ore代数の付随Z-代数になる、という任意nの主張は n=1 で偽**である。`genidx:thm:period-two-counterexample` に、標準Hilbert級数・語長Koszul性・左右noetherian性も満たすAS正則Z-整域で、最小周期が2となる例と完全な証明を記載した。この例は2周期の添字付きOre表示を持つため、Z-代数上のOre表示そのものの反例ではない。

**n=3、primitive jumps (1,1,1,2,3)、AS次元5の全整域対象では、語長Koszul性・AS添字8・関係数 (3,3,3,1,0)・標準Hilbert級数・2周期性を導いた**（`genidx:thm:five-dimensional-numerics`）。Hilbert級数・noetherian性・周期を追加仮定しない。純jump 1部分の解消、折畳Hilbert行列のLaurent係数、唯一の例外の行列式排除、混合関係数の正値性による数学的証明であり、新しい有限列挙には依存しない。

**任意nについて、純jump 1部分 B 自身が左右AS正則次元nなら、添字付き二段Ore表示が成立する**（`genidx:thm:as-base-ore`）。Bの有限AS解消を仮定するが、混合関係数・Koszul性・指定Hilbert級数・noetherian性を追加仮定しない。Bは1周期的で、AS添字 L_B に対し L_A=L_B+5、最高語長 N_A=L_B+2、H_A=H_B(ut)/((1-ut^2)(1-ut^3)) となる。n=3ではこの二段表示の存在は **Bの1周期性、およびBのAS3性と同値**（`genidx:cor:five-dimensional-ore-criterion`）。Bの1周期性は最終代数Aの1周期性とは別条件である。

**n=1の全対象については、添字付き二段Ore表示と裸の添字保持同型を完全に決定した**（`genidx:thm:one-light-ore`, `genidx:thm:one-light-classification`）。正規形は `zx=xz`, `wz=c zw`, `w_i x_(i+3)=x_i w_(i+1)+d_i z_i z_(i+2)`、ただし `c!=0`, `d_(2m)=c^(-m) alpha`, `d_(2m+1)=c^(-m) beta`。二つの正規形はcが一致し、`(alpha,beta)`が同時非零スカラー倍で一致するときに限り同型である。1周期性の必要十分条件は `alpha^2=c beta^2`（零の組を含む）で、その他の最小周期は2。この構成の全てが語長Koszul・標準Hilbert・左右noetherianなAS3 Z-domainとなることも、一般パラメータの解消で証明した。

公表用原稿は `papers/nc-p1123.tex` の1本に統合。重み `(1,1,2,3)`、語長二次、AS次元4のZ-代数について、**Z-domainなら標準Hilbert級数・1周期性・量子平面またはJordan平面上の2段Ore表示が従う**。Hilbert級数、周期性、noetherian性を追加仮定せず、noetherian性も結論として得る。完全な証明は `idx:thm:domain-standard` から `idx:thm:domain-ore` にある。

また全対象で、**Z-domain性は、選んだ語長斉次二次表示の重み2・語長1生成元 `z_0,...,z_6` が全次数で左右正則であることと同値**である（`idx:prop:z-regular-criterion`）。7周期性により調べる添字は七つで足りるが、有限次数までの単射性検査だけで十分とはしていない。

整域性を仮定しない全対象について、**標準関係数 `(1,2,2,1)` と標準二変数Hilbert級数が従い、Q=H=S** となる（`idx:thm:mixed-relation-ranks`, `idx:cor:all-standard`）。重み2・5の関係数は、七周期の漸化式とテンソル鎖の非消滅で解析的に強制する。重み3・4の関係数の証明は、行列Hilbert級数の成長から必要条件を導き、890個の整数列を厳密に検査して零列以外を排除する計算補助の証明である。有限次数のHilbert一致からAS正則性を認定してはいない。

整域部分の二つのOre表示については、**裸の添字保持同型の存在を、一つの可逆行列と有限個の条件で完全に判定できる**（`idx:thm:finite-isomorphism`）。量子平面・Jordan平面と零の導分項を同じ条件で扱う。対角量子族では、三係数 `(a,b,c)` への正規化後の同一視は恒等変換と `(a,b,c) -> (a^(-1),b^(-1),c*a^3/b^2)` だけである（`diag:thm:indexed-isomorphism`）。全特殊値を含み、対角族の同型類は三次元トーラスの有限商で与えられる。

一般の `(1^n,2,3)` 型については、左右noetherian・指定AS次元・指定Hilbert級数の下の数値拘束と、さらに語長二次・整域である場合の全Ore表示・次数付き同型を収録する。この任意nの定理の仮定を上記の n=2 の強化によって除去したとはしない。語長二次を仮定しない n=2 の仮定付きgraded Ore網羅定理、対角Ore表示パラメータの4既約成分、添字保持同型の不変量も含む。

残る主課題は、n=3の純jump 1部分Bについて、整域・左右(1,3,3,1)線型解消・標準Hilbert・2周期という証明済み条件と親代数AのAS構造から、BのAS双対性または1周期性を導くことである。n>=4では数値型の自動性も未解決。通常の三生成元二次整域の分類（Iyudu–Shkarin, arXiv:1806.06844v1, §12.1）はBを1周期化した後に適用する。2周期のままのZ-代数に直接適用しない。一般の重み5関係の欠損を多項式増大で制限する補題と、その方法だけでは解けない配置も保持する。

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
