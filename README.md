# nc-p1123 — 最小生成元次数 (1^n,2,3) のAS正則代数

**2026-11-19 / 統合版 v12。任意nの対象で、全始点の二つの階数条件 r3=n, r5=1、純基礎BのAS正則性、AS基礎上の添字付き二段Ore表示が同値である。Hilbert級数・Koszul性・noetherian性はこの判定の追加仮定ではない。n=1,2,3では階数条件の自動性を含めて証明済みで、n=2,3では通常gradedへ下降する。n=4では最高差次数3を無条件に証明し、語長Koszul性・周期・基礎AS4性・Ore表示・二つの階数条件を含む十条件が同値である。無条件の全次元問題は、n>=4で二つの階数条件を強制することに還元された。**

[研究方針](research/plan_ja.tex) → [統合公表用主論文](papers/nc-p1123.tex) → [研究ノート](research/notes_ja.tex) の順に読む。

現在は、整域性を仮定して primitive jumps `(1^n,2,3)`、AS次元 `n+2` の語長二次Z-代数へ拡張する問題を扱う。**全対象が単一のgraded二段Ore代数の付随Z-代数になる、という任意nの主張は n=1 で偽**である。`genidx:thm:period-two-counterexample` に、標準Hilbert級数・語長Koszul性・左右noetherian性も満たすAS正則Z-整域で、最小周期が2となる例と完全な証明を記載した。この例は2周期の添字付きOre表示を持つため、Z-代数上のOre表示そのものの反例ではない。

**n=4、AS次元6では、最高Extの重みLと語長Nの差は無条件に L−N=3 である**（`n4:cor:top-excess-three`）。鍵は、四本以上の隣接生成元を持つ周期的二次整域で、多項式増大と全単純加群の射影次元3以下が両立しないという補題である。Euler行列の零固有値の二次変動を平方和で評価し、逆Hilbert行列の非負性と矛盾させる。純jump 1部分Bの長さ4の解消とモーメント制約も得た。

**n=4では、次の十条件が同値である**（`n4:thm:equivalent-criteria`）。

1. Aが語長Koszulである。
2. 最高語長が N=6 である。
3. Aが1周期的である。
4. 純jump 1部分Bが1周期的である。
5. Bの行Hilbert級数が始点によらない。
6. 全行で H_B=(1-u)^−4 である。
7. Bが左右AS正則次元4を持つ。
8. AがB上の添字付き二段Ore表示を持ち、BがAS4である。
9. Aが四生成元Koszul AS4整域上の通常graded二段Ore代数へ下降する。
10. 全始点で r3=4, r5=1 が成立する。

これらの条件の下で L=9、関係数 (6,4,4,1,0)、標準二変数Hilbert級数を得る。**n=4の構造に残る核心は十条件の自動性である。条件成立後のB-AS4性と第二段Ore表示は証明済み**であり、noetherian性を追加する必要はない。四生成元のnoetherian Koszul整域・標準14641解消でも非ASの既知例は、一般の基礎代数の数値だけによるAS認識を妨げる（Rogalski–Sierra, arXiv:1101.0737v2, Theorem 1.1, (1.2)）。一方、この既知例は上の同値定理により対象AS6代数の純基礎Bとして実現できない。

**通常の次数付き語長Koszul対象では、任意nで二段Ore表示と基礎BのKoszul AS正則性を証明した**（`ogk:thm:numerics`, `ogk:thm:ore-without-noetherian`）。Hilbert級数とnoetherian性は追加仮定ではなく、標準数値型とHilbert級数も結論である。語長1の正規元zによる商は有限大域次元を持つ。混合関係の退化があれば、この商に両方向の積が零となる非零の語長1元v,wが生じ、交代barテンソルが全次数の非零Torを与えて矛盾する。混合射影の可逆性とHilbert比較からPBW基底、第二段Ore表示、BのAS性が従う。追加のnoetherian仮定を置く系は、Bもnoetherianとなる帰結を記録する。

**一般indexed対象でも、全行の標準二変数Hilbert級数だけを追加すれば、任意nで添字付き二段Ore表示とBのKoszul AS正則性が従う**（`ibar:thm:standard-hilbert-ore`）。AのKoszul性・1周期性、BのAS性、noetherian性は追加仮定しない。正規元族で2周期に折り畳み、半単純次数零部分上の有限Torとbar複体を使う。Bは1周期的となるが、Aの1周期性を任意nの結論には含めない。

**任意nで、全始点の r3=n, r5=1 だけから、B-ASnと全二段Ore表示まで従う**（`igraph:thm:normal-z-ore`）。標準Hilbert級数・Koszul性・noetherian性を追加しない。bar障害と二周期Golod–Shafarevich不等式が r4=n を与える。正規商Qの混合関係を自由純部分の自己同型μによるグラフとして書くと、wの個数を増やす際の係数イデアルは `(R,μR,…,μ^jR)` となり、有限次元の二次関係空間内で安定する。一方、AS双対性はEuler行列の最高w係数を可逆にする。この二つからイデアルは最初から一定、従って μR=R とQのOre表示が従う。wの正則性から基礎AS性を得て、一般AS-base定理でAの二段表示が完成する。逆向きも既存のAS-base定理から従い、二つの階数条件は基礎AS性と同値である。

語長Koszul性も満たす場合は、L=n+5と標準Hilbert級数も従う（`ibar:cor:koszul-normal-z`）。この系には、正規商Qのw次数零のbar複体と、Ext代数の分解 F⊕Fη、η²=0 を使う別証明もある。完全な別証明を研究ノート `note:koszul-normal-z-frobenius` に保存した。一般の階数判定はこの別証明に依存しない。

**n=4の純基礎Euler条件だけでは、標準型の自動性を強制できない。** s=5、N=7、L=10の形式数値データが、Eulerの行列恒等式、全次数の行Hilbert係数の正値性、多項式増大、共通の最高Laurent係数、全次数のHopf不等式を満たす一方、行Hilbert級数は始点に依存する。完全な計算補助証明は研究ノート `note:n4-pure-euler-obstruction`、再現コードは `computations/verify_n4_pure_euler.py` にある。代数・最小解消・AS6対象としての実現は主張しない。純基礎のこれらの数値条件に、実際の二次関係、親AS対合、または混合成分の制約を組み合わせる必要がある。

**n=3、primitive jumps (1,1,1,2,3)、AS次元5の全整域対象では、語長Koszul性・AS添字8・関係数 (3,3,3,1,0)・標準Hilbert級数・2周期性を導いた**（`genidx:thm:five-dimensional-numerics`）。Hilbert級数・noetherian性・周期を追加仮定しない。純jump 1部分の解消、折畳Hilbert行列のLaurent係数、唯一の例外の行列式排除、混合関係数の正値性による数学的証明であり、新しい有限列挙には依存しない。

**n=3では、純jump 1部分BのAS3性も導け、添字付き二段Ore表示が無条件に成立する**（`genidx:thm:three-light-ore`）。鍵となる `p2base:thm:as3` は、2周期の三生成元二次Z-整域が H=(1-t)^-3 を持てばAS3であることを証明する。Koszul性や有限大域次元も仮定不要。分数斜体内の交代積空間に移し、退化した最高syzygyを積空間次元または有理関数の極因子による成長で排除する。通常gradedの分類を直接適用する証明ではない。基礎Bは1周期的になる。さらに `genidx:thm:three-light-descent` は、導分係数が張る空間上の移動を基礎代数の自己同型へ延長し、**最終代数A自身の1周期性と通常のgraded二段Ore表示**を証明する。移動空間の次元0,1,2,3を全て処理しており、非零補正も含む。下降後の基礎代数は共通表示のZhang twistとなる場合がある。第1段を語長次数でRogalski–Zhang Lemma 1.3(a)へ適用し、第2段にOreのHilbert基底定理を使うことで、左右noetherian性も導く。

**任意nについて、純jump 1部分 B 自身が左右AS正則次元nなら、添字付き二段Ore表示が成立する**（`genidx:thm:as-base-ore`）。Bの有限AS解消を仮定するが、混合関係数・Koszul性・指定Hilbert級数・noetherian性を追加仮定しない。Bは1周期的で、AS添字 L_B に対し L_A=L_B+5、最高語長 N_A=L_B+2、H_A=H_B(ut)/((1-ut^2)(1-ut^3)) となる。n=3ではBのAS性を上の認識定理で確立した。

**n=1の全対象については、添字付き二段Ore表示と裸の添字保持同型を完全に決定した**（`genidx:thm:one-light-ore`, `genidx:thm:one-light-classification`）。正規形は `zx=xz`, `wz=c zw`, `w_i x_(i+3)=x_i w_(i+1)+d_i z_i z_(i+2)`、ただし `c!=0`, `d_(2m)=c^(-m) alpha`, `d_(2m+1)=c^(-m) beta`。二つの正規形はcが一致し、`(alpha,beta)`が同時非零スカラー倍で一致するときに限り同型である。1周期性の必要十分条件は `alpha^2=c beta^2`（零の組を含む）で、その他の最小周期は2。この構成の全てが語長Koszul・標準Hilbert・左右noetherianなAS3 Z-domainとなることも、一般パラメータの解消で証明した。

公表用原稿は `papers/nc-p1123.tex` の1本に統合。重み `(1,1,2,3)`、語長二次、AS次元4のZ-代数について、**Z-domainなら標準Hilbert級数・1周期性・量子平面またはJordan平面上の2段Ore表示が従う**。Hilbert級数、周期性、noetherian性を追加仮定せず、noetherian性も結論として得る。完全な証明は `idx:thm:domain-standard` から `idx:thm:domain-ore` にある。

また全対象で、**Z-domain性は、選んだ語長斉次二次表示の重み2・語長1生成元 `z_0,...,z_6` が全次数で左右正則であることと同値**である（`idx:prop:z-regular-criterion`）。7周期性により調べる添字は七つで足りるが、有限次数までの単射性検査だけで十分とはしていない。

整域性を仮定しない全対象について、**標準関係数 `(1,2,2,1)` と標準二変数Hilbert級数が従い、Q=H=S** となる（`idx:thm:mixed-relation-ranks`, `idx:cor:all-standard`）。重み2・5の関係数は、七周期の漸化式とテンソル鎖の非消滅で解析的に強制する。重み3・4の関係数の証明は、行列Hilbert級数の成長から必要条件を導き、890個の整数列を厳密に検査して零列以外を排除する計算補助の証明である。有限次数のHilbert一致からAS正則性を認定してはいない。

整域部分の二つのOre表示については、**裸の添字保持同型の存在を、一つの可逆行列と有限個の条件で完全に判定できる**（`idx:thm:finite-isomorphism`）。量子平面・Jordan平面と零の導分項を同じ条件で扱う。対角量子族では、三係数 `(a,b,c)` への正規化後の同一視は恒等変換と `(a,b,c) -> (a^(-1),b^(-1),c*a^3/b^2)` だけである（`diag:thm:indexed-isomorphism`）。全特殊値を含み、対角族の同型類は三次元トーラスの有限商で与えられる。

一般の `(1^n,2,3)` 型については、左右noetherian・指定AS次元・指定Hilbert級数の下の数値拘束と、さらに語長二次・整域である場合の全Ore表示・次数付き同型を収録する。この任意nの定理の仮定を上記の n=2 の強化によって除去したとはしない。語長二次を仮定しない n=2 の仮定付きgraded Ore網羅定理、対角Ore表示パラメータの4既約成分、添字保持同型の不変量も含む。

残る主課題は、n>=4で r3=n, r5=1 を元の仮定から導くことである。n4ではこれは十条件の自動性と同値であり、親AS6の中央Ext対合と混合Euler条件を使って階数欠損を調べる。Koszul性や標準Hilbert級数を先に確定することは必須ではない。n3の数値型、基礎AS3性、添字付き二段Ore表示、最終代数の1周期下降を未解決として扱わない。n3では基礎代数とOreデータを含む全同型軌道の分類が残る。Iyudu–Shkarin, arXiv:1806.06844v1, §12.1 の通常三生成元分類と今回の2周期認識定理を比較し、新規性の最終確認は未了と明示する。一般の重み5関係の欠損を多項式増大で制限する補題と、その方法だけでは解けない配置も保持する。任意nのAS基礎代数が自動的にnoetherianであるとは主張しない。

元のn=2の全分類では、整域性の自動性、零因子を持つ枝、一般の軌道の幾何は引き続き未解決である。n=2で最小周期7または非定数の射影階数列を持つ対象は必ず零因子を持つ、という結果を、今回のn=1の整域反例へ適用しない。同型の存在判定と、非線型自己同型を含むモジュライスタックも区別する。

**階数の自動性について、AS周期 L が3で割り切れなければ全 r5(i)=1 も証明した**（`genidx:lem:r5-gs-saturation`）。3で割り切れる場合にも、少なくとも一つの法3剰余類上では全て1である。二段目までの行列GS不等式と正の左ベクトルの一次補正による証明で、Koszul性は不要。この結果を踏まえ、前者では残る r3=n、後者では r3 と他の剰余類の r5 を調べる。

研究状態は [STATE](research/STATE.json)、先行文献は [BASELINE](research/BASELINE.md)、組版・計算の検証は [validation](research/validation.json) を参照する。

```bash
latexmk -lualatex -outdir=. papers/nc-p1123.tex
python3 scripts/check_project.py
python3 computations/verify_mixed_ranks.py
python3 computations/verify_n4_pure_euler.py
python3 computations/verify_n4_parent_mixed.py
python3 -m pip install -r requirements-symbolic.txt
python3 computations/verify_skew_ore.py
```

VS Code の設定は `.latexmkrc` と `.vscode/settings.json`。組版は別途確認が必要。
