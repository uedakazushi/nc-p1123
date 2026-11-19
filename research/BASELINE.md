# 一次文献・外部依存の現行索引

2026-11-19 / v13。読んだ箇所と適用範囲を区別する。外部PDFは同梱しない。
指定対象の完全な添字保持同型分類を与える文献は、現在の確認範囲では見つかっていない。
これは文献不存在や新規性の確定を意味しない。

## 直接使う文献

| 文献 | 確認した一次資料と箇所 | 本研究での使い方・限界 |
| --- | --- | --- |
| Auroux–Katzarkov–Orlov, *Mirror symmetry for weighted projective planes and their noncommutative deformations*, Ann. Math. 167 (2008), 867–943; DOI 10.4007/annals.2008.167.867; arXiv:math/0404281 | [出版版](https://annals.math.princeton.edu/wp-content/uploads/annals-v167-n3-p04.pdf), §2.2、Prop.2.3/Cor.2.4、Prop.2.6、Thm.2.12、Prop.2.18/Cor.2.19 | 任意重みの対角skew polynomial族。AS次元4、添字7と例外列7項は既知。qgrは可換基準でstackのcoh。非対角・非1周期の全分類ではない。 |
| Sierra, *G-algebras, twistings, and equivalences of graded categories*, Algebr. Represent. Theory 14 (2011), 377–390; DOI 10.1007/s10468-009-9193-y | [arXiv:math/0608791v3](https://arxiv.org/pdf/math/0608791), Thm.1.2 = Cor.4.4、§2 | degree1生成を要求せず、Zhang twistとassociated Z-algebra同型の対応。graded同型をそのままindexed同型に読み替えない。 |
| Vitória, *Equivalences for noncommutative projective spaces*, arXiv:1001.4400v3 (2011) | [本文](https://arxiv.org/pdf/1001.4400), §1、Theorem 2.5、Remark 2.6と証明冒頭 | 全生成元が次数1のskew polynomial環についてgraded Morita同値を係数のスカラー変更・置換で分類する比較先。本稿は重み (1,1,2,3) の添字を保持するため、同定式の指数と許容変更を直接証明する。通常次数での同定を重み付き同定へ読み替えない。 |
| Reyes–Rogalski, *Growth of graded twisted Calabi–Yau algebras*, arXiv:1808.10538v1 (2018) | [本文](https://arxiv.org/pdf/1808.10538), Lemma 2.7、Proposition 2.8とその証明 | 行列Hilbert級数の極と成長の一般理論の比較先。本稿の混合関係数の証明では、二変数のうち差次数変数を固定した正係数比較から行列式恒等式を直接導く。一般的な行列Hilbert級数の手法を新規性としない。 |
| Van den Bergh, *Non-commutative quadrics*, IMRN 2011, no.17, 3983–4026; DOI 10.1093/imrn/rnq234 | [arXiv:0807.3753v3](https://arxiv.org/pdf/0807.3753), §3、Prop.3.3、Lemma3.4、Definition4.1.1、Theorem4.2.2 | 1周期同型から graded 代数を復元する Lemma 3.4 は degree 1 生成を要求しない。Theorem4.2.2 の三次元quadratic全1周期は、Definition4.1.1の解消型 (0);(1,1,1);(2,2,2);(3) に対するもの。本稿の重み(1,2,3)の語長二次・最小周期2の例には適用されない。語長と添字差を混同しない。 |
| Iyudu–Shkarin, *Classification of quadratic and cubic PBW algebras on three generators*, arXiv:1806.06844v1 (2018), 本稿引用キー `ISclass` | [一次本文](https://arxiv.org/html/1806.06844v1), §1の基礎体とクラスΩの定義、Theorem1.11の分類声明、Remark1.15、§12.1 | 代数閉体・標数≠2,3上の通常の次数1生成二次代数で、H=(1−t)^−3ならdomainとAS正則次元3が同値である。`genidx:cor:five-dimensional-ore-criterion` において、Bの1周期性を先に確立した後のgraded下降B₀へ適用する。一般の非1周期Z-代数へ直接適用しない。分類表全件と各証明の独立再検証を実施したとはしない。 |
| Martínez-Villa–Solberg, *Artin–Schelter regular algebras and categories*, JPAA 215 (2011), 546–565; DOI 10.1016/j.jpaa.2010.06.006 | [arXiv:0902.1119](https://arxiv.org/pdf/0902.1119), Def.5.7、Lemma6.1(b)、Thm.6.2(a),(b) とその証明 | 有限生成射影解消と AS 双対性から得る Hom–Tor 双対、接続準同型との両立、Yoneda 積による完全対合を確認。全単純加群を取ると AS 添字の全単射が必要な安定性を与える。語長 Koszul 性と7移動は本稿の仮定から別途証明し、一般原理そのものを新規性としない。 |
| Rogalski–Zhang, *Regular algebras of dimension 4 with 3 generators*, arXiv:1101.1998v2 (2011) | [本文](https://arxiv.org/pdf/1101.1998), Lemma 1.1、Cor.1.2、Lemma 1.3(c)（PDF pp.3–4） | Lemma 1.1 は連結 graded 代数の有限 global dimension と degree 1 の正則正規元を仮定し、商の次元を1下げる。Cor.1.2 は親代数を domain として AS 正則性を比較する。どちらも noetherian 性を仮定しない。適用する次数は語長であり、重み2の z も語長1。Lemma 1.3(c) は重み2生成元族の正則性から整域性を導く判定の直接依存であり、適用順序は下記。 |
| Liu–Wang–Wu, *Twisted Calabi–Yau property of Ore extensions*, JNCG 8 (2014), 587–609; DOI 10.4171/JNCG/165; arXiv:1205.0893 | [出版版](https://ems.press/content/serial-article-files/30578), Thm.3.3、§1.2、§1.3、Remark 2.2、Prop.4.1 | 自己同型によるOre拡大のtwisted CY性、connected graded版のAS正則性との対応、正次数の拡大変数、noetherian/domain保存。一般graded Ore分類の逆構成に用い、多項式成長はPBW基底から別に確認する。一般的な構成法を新規性としない。 |
| Lu–Palmieri–Wu–Zhang, *Regular algebras of dimension 4 and their A-infinity-Ext-algebras*, Duke Math. J. 137 (2007), 537–584; DOI 10.1215/S0012-7094-07-13734-7 | [著者PDF](https://sites.math.washington.edu/~palmieri/Papers/hiext.pdf), Lemma 1.1、Lemma 1.3、Theorem 1.9 | 最小解消のAS双対性と、noetherian・global dimension 4・GK dimension 4のconnected graded AS正則代数がdomainとなる結果。Lemma 1.3は次数1生成を要求せず、出典を [ATV2, 3.9] と明記する。graded Ore網羅定理と重み2生成元族による整域判定で、noetherian性とGK dimension 4を先に確認して適用する。 |
| Bergman, *The diamond lemma for ring theory*, Adv. Math. 29 (1978), 178–218; DOI 10.1016/0001-8708(78)90010-5 | [著者ページ](https://math.berkeley.edu/~gbergman/papers/updates/diamond.html), Thm.1.2, p.181 | 停止順序と全重なりの解消から順序単項式基底。今回取得した一次資料は著者の書誌・訂正ページであり、原論文全PDFは未取得。適用の四重なりは直接検算。 |
| Priddy, *Koszul resolutions*, Trans. AMS 152 (1970), 39–60 | [一次PDF](https://math.mit.edu/~hrm/palestine/priddy-koszul-resolutions.pdf), Thm.5.3, p.51 | PBW基底から語長Koszul性。重み次数について線型であるとの主張ではない。 |
| Lu–Palmieri–Wu–Zhang, *Koszul equivalences in A-infinity-algebras*, NYJM 14 (2008), 325–378 | [出版版](https://nyjm.albany.edu/j/2008/14-16.pdf), Corollary D, p.327; 証明§9.3, p.372 | connected graded AS-regular性とFrobenius Extの対応。Definition9.1は有限GK成長を含めないので、本文では成長をPBW基底から独立に示す。 |

## 混同を避ける比較先

- 上表のLu–Palmieri–Wu–Zhangの序論、§1の二生成型、式(HS)も確認。degree1二生成・関係次数3,4の族は、今回と同じHilbert級数でも最小生成元とBetti型が違う。Lemma 1.3のdomain結果とは適用範囲を分け、同論文のdegree1生成やgenericityを仮定する分類定理を重み付き四最小生成元へ直接適用しない。
- Etingof–Ginzburg, *Noncommutative del Pezzo surfaces and Calabi–Yau algebras*, JEMS 12 (2010), 1371–1416; DOI 10.4171/JEMS/235; [出版版](https://ems.press/content/serial-article-files/31746)。§1.1、表(2.3.3)、式(3.5.1)。E8の重み(1,2,3)とdegree6 potentialを確認。巡回微分の線型項により最小生成元が消える場合があり、Reesによる四変数表示だけでは本対象と同定しない。
- Várilly-Alvarado–Zywina, *Arithmetic E8 lattices with maximal Galois action*, LMS J. Comput. Math. 12 (2009), 144–165; [著者PDF](https://pi.math.cornell.edu/~zywina/papers/E8lattice.pdf), Prop.2.3。degree1 del Pezzoのsextic表示。証明参照先Kollár, *Rational Curves on Algebraic Varieties*, III.3.5の本文は今回未確認。
- Rains, *Filtered deformations of elliptic algebras*, [arXiv:2107.13540v2](https://arxiv.org/pdf/2107.13540v2) (2022), Prop.5.1、Conjecture1。v1の命題番号を混用しない。全射性は予想、今回のweighted ambientの認識は未証明。

## nc-p3から継承したこと

[nc-p3](https://github.com/uedakazushi/nc-p3) の現行研究方針と
`sections/four_window.tex` のtraceによる周期構成を方法上の比較先として読んだ。
通常次数1の四窓の定理をそのまま引用して重み付き七窓を結論してはいない。
本稿では最小生成元の三種類のjump、Hom–Tor双対、trace選択、
非線型同型の線型化まで独立に記載した。
初期結果の再現にnc-p3や他の私的研究原稿の取得は必要ない。

## 対角skew Ore表示
統合公表論文 `papers/nc-p1123.tex` の対角節は、AKOの対角量子多項式環を基底とし、
Liu--Wang--Wu Thm.3.3のtwisted CY保存を利用する。重みを保つ語長二次の
対角skew Ore表示の全必要十分条件とパラメータ空間の4成分は同節で直接証明する。
Ore手法と一般正則性は既知である。これらの具体式と既存文献の構成の完全同定および新規性は未確認。

## 添字保持同型の有限判定と対角族の商

主論文 `idx:thm:finite-isomorphism` は、網羅済みの整域Ore表示間の裸の添字保持同型を、
一つの可逆行列 P と非零スカラー κ に関する有限条件へ帰着する。
その証明は、語長線型化、頂点スカラーの除去、重み2・3の交換関係が与える添字漸化式、
導分項の偶数・奇数両列への伝播で完結する。
Sierraの一般対応を踏まえているが、一般のtwisting systemを仮定したまま判定を残してはいない。
この有限条件は量子平面・Jordan平面を共通に扱い、導分項が零の場合も含む。

対角族の `diag:thm:indexed-isomorphism` は、三係数 (a,b,c) への正規化後、
恒等変換と (a,b,c) -> (a^(-1),b^(-1),c*a^3/b^2) だけが同型を与えることを証明する。
固定点は a=1, b=±1 であり、固有値重複と冪根を含む全特殊値を扱う。
`diag:cor:quotient` の三次元有限商はこの対角族の同型類を与えるが、全ASモジュライの成分とはしない。
Vitória Theorem 2.5 は通常次数1生成のskew polynomial環の重要な先行分類であり、
本稿の重み付き定理とは対象と同定式を区別する。
Cooney–Grabowski, *Automorphism groupoids in noncommutative projective geometry*,
[arXiv:1807.06383v4](https://arxiv.org/pdf/1807.06383) (2022), Definition 1、Lemma 5、Theorem 12の設定も確認した。
これらのdegree 1生成・幾何的代数の記述を、本稿の重み付きOre族へ直接適用してはいない。
具体的な有限判定式と対角商の完全な先行結果照合は継続中であり、新規性の確定を意味しない。

## 整域 Z-代数の構造定理と直接依存

### n=1の完全構造と、任意nの下降に対する反例

`genidx:thm:one-light-ore` と `genidx:thm:one-light-classification` は、
primitive jumps (1,2,3) の全AS3語長二次Z-整域について、添字付き二段Ore表示と
裸の添字保持同型を決定する。AS対合から語長Koszul性、AS添字6と関係数を強制し、
top syzygyで混合関係の両係数の非消失を得る。
正規形は zx=xz, wz=c zw, wx=xw+d_i zz、
d_(2m)=c^(-m) alpha, d_(2m+1)=c^(-m) beta である。
同型はc一致と(alpha,beta)の同時非零スカラー倍であり、
alpha^2=c beta^2 が1周期性の必要十分条件、他は最小周期2となる。
逆構成のPBW・左右AS3・整域・noetherian性も一般c,dについて直接証明する。
この同型類集合をaffine categorical quotientと同一視しない。
既存の重み付きZ-代数の分類とこの具体的な正規形との重複の最終確認は未完である。

`genidx:thm:period-two-counterexample` は、n=1、primitive jumps (1,2,3)、AS次元3の
語長二次Z-整域で、標準二変数Hilbert級数・語長Koszul性・左右noetherian性を持ちながら
最小正周期が2となる例を与える。係数 epsilon_i を偶数で1、奇数で0とし、
zx=xz, wz=zw, w_i x_(i+3)=x_i w_(i+1)+epsilon_i z_i z_(i+2) とする。
唯一のPBW重なりは wzx で、epsilon_(i+2)=epsilon_i により解消する。
主論文は右単純解消の全行列とtop tensorの両表示を明示し、左右AS条件と大域次元を直接証明する。
w個数の付随次数が可換重み付き多項式Z-代数であることから整域性・noetherian性を得る。

この例が否定するのは、全nの対象を単一のgraded代数 D の check(D) で表示する主張である。
Van den Bergh Lemma3.4 の1周期性との同値を用いる。
同論文Theorem4.2.2の通常三次元quadratic型は三本ともjump 1であり、
上のweighted word-quadratic型と異なることを一次PDFのDefinition4.1.1から確認した。
本例自体は2周期の添字付きOre表示を持つ。任意nの添字付きOre表示の網羅性を反証したとはしない。
この具体例や周期障害と、既存の重み付き・quiver・正規拡大の構成との完全な同定は未確認である。

研究ノートの一般AS平行移動はExtのNakayama同型と矢印グラフの順序から導く。
一般の重み2正規元族は r_3=n, r_5=1 とzの左右正則性を仮定する。
主論文 `genidx:lem:one-heavy-as` は一重生成元の **indexed** Ore補題であり、
QがAS次元n+1、純jump 1基礎 B がAS次元n、双方が有限生成射影による有限AS解消を持つことを仮定する。
全Yoneda圏の完全対合と重い生成元の個数によるbar次数を用い、
Q=B[w;μ]、μ:B(d)≅Bを導く。Koszul性、noetherian性、指定Hilbert級数、整域性は不要である。
二次双対と全Extの同一視は使わず、一般のFrobenius対合そのものを新規な結果としない。

### n=3の数値型と、基礎代数の1周期性によるOre判定

`genidx:thm:five-dimensional-numerics` は、primitive jumps (1,1,1,2,3)、
AS次元5、語長二次のZ-domainから、最高語長5、AS添字8、語長Koszul性、
関係数 (r₂,r₃,r₄,r₅,r₆)=(3,3,3,1,0)、標準二変数Hilbert級数と2周期性を導く。
Hilbert級数、noetherian性、Koszul性は追加仮定ではない。
`genidx:lem:weight-five-growth` の単項式商による増大障害、差次数零のbar複体、
`genidx:lem:three-light-base-numerics` の周期折畳Hilbert行列とLaurent係数を用いる。
非標準候補の行列式 (1−u⁷)²(1−64u⁷) による排除は代数的に証明し、
計算機の有限次数探索をその代用にしない。
AS完全対合、単項式商の増大、Hopfの次元不等式、行列Hilbert級数の一般的な手法は既知である。
この具体的な数値型強制と既存のweighted/quiver分類との完全照合、新規性の最終確認は未完である。

`genidx:cor:five-dimensional-ore-criterion` は、このn=3の範囲で、
純jump 1部分B上の標準的なindexed二段Ore表示、Bの1周期性、B自身のAS3性の三条件を同値にする。
Ore表示の二つの同型からBの2周期・3周期を得る方向は直接証明する。
Bが1周期なら、その下降B₀は通常のquadratic domainでH=(1−t)^−3となるので、
上表の `ISclass` の既知分類を用いてAS3性を得る。
この依存は、同論文のRemark1.15によるAS3とtwisted potentialの対応と、
§12.1によるΩ内のdomainとtwisted potentialの対応である。
基礎体は本研究の代数閉体・標数0の仮定で適合する。
Bの1周期性もAS3性も無条件に確立したとはしない。
B自身の1周期性と、A全体の1周期性を区別する。

### 任意nでのAS基礎代数を仮定した構造定理

`genidx:thm:as-base-ore` は、A∈Qₙ^domに対し、純jump 1部分B自身が
左右AS正則次元nで有限生成射影による有限AS解消を持つことだけを追加すると、
B上のindexed二段Ore表示が従うことを証明する。
混合関係数、Koszul性、標準Hilbert級数、noetherian性、商A/(z)の整域性はさらに仮定しない。
差次数零のExtとその相補対合が r₅=1、r₃=n を強制し、
第1段の最小mapping coneとAS対合から全Betti成分とr₄=nを復元する。
Hilbert級数と整列語の比較によるPBW基底を使い、第2段の同型・導分を構成する。

この定理はBの1周期性、L_A=L_B+5、N_A=L_B+2と
H_A(u,t)=H_B₀(ut)/((1−ut²)(1−ut³))も与える。
Aの語長Koszul性とBのKoszul性は同値であり、BがKoszulなら標準数値型となる。
この条件付き定理と、BのAS性を全対象から導く未解決問題を区別する。
mapping cone、完全対合、PBWからのOreデータの構成は既知の方法である。
この仮定の組合せと結論の既存文献との完全同定、新規性の最終確認は未完である。

### n>=4に残る数値型・Koszul性の文献上の確認範囲

Abdourrahmane Kabbaj, *On GK Dimension and Generator Bounds for a Class of Graded Algebras*,
[arXiv:2501.11346v1](https://arxiv.org/html/2501.11346v1) のCorollary 2.5、
Definition 3.2、Theorems 3.4, 3.9, 3.10の本文を確認した。
対象は通常の次数1生成の連結局所有限graded代数である。
Corollary 2.5はKoszul AS性とGKdim>=d-1から標準Hilbert級数を結論し、
Theorem 3.4はAS次元6以下のquadratic代数のmonotonic性を与える。
Theorems 3.9, 3.10はmonotonic性に加えGKdim=dまたは指定Hilbert型を仮定する生成元数の上界である。
これらを「二次・整域・生成元数=大域次元だけで任意次元のKoszul性が従う」という定理として使わない。

Daniel Rogalski, *Artin-Schelter Regular Algebras*,
[arXiv:2307.03174v2](https://arxiv.org/pdf/2307.03174), §7、本文p.29は、
標準Hilbert級数を持つAS正則代数のKoszul性に関するSmith論文内のZhangの定理への案内である。
これはsurveyによる所在情報であり、Smithの原資料を今回確認したという意味ではない。
今回確認した資料だけから、n>=4の一般indexed対象で不足しているKoszul性やHilbert仮定を補うことはできない。
n=3では上記の直接証明によって数値型を確定しており、このsurveyから補ってはいない。
この限定した確認を、文献全体に該当定理が存在しないという主張にはしない。

### n=2の網羅的な正の結果

公表論文 `papers/nc-p1123.tex` の `idx:def:target` は、各頂点の最小生成元 jump が
(1,1,2,3) で語長二次の広い四次元 AS 正則対象 Q を定義する。
その定義には noetherian、domain、標準 Hilbert 級数、1周期性を含めない。
現在の構造定理は、Q のうち Z-domain である全対象について次を証明する。

1. `idx:lem:duality-period` と `idx:thm:index-seven`：有限生成射影解消の AS 双対から、語長 Koszul 性、AS 添字7、語長を保つ7周期同型を導く。この部分は domain を使わない。
2. `idx:thm:domain-standard`：domain による関係数の上界と七行の語長 Euler 式から、関係数 (1,2,2,1) と標準 Hilbert 級数を強制する。
3. `idx:lem:normal-family` と `idx:thm:domain-period-one`：重み2の正規生成元族が2周期を与え、7周期との合成で1周期を得る。Van den Bergh Lemma 3.4 によって、語長二次の graded 代数 D を復元する。
4. `idx:lem:three-generator` と `idx:thm:domain-ore`：Rogalski–Zhang の正則正規元商を **語長次数** に適用し、D/(z) を AS 次元3へ下げる。その商の syzygy と AS 対合から第2生成元の正規性を導き、量子平面または Jordan 平面からの2段 Ore 表示を得る。商の domain 性や noetherian 性を仮定していない。左右 noetherian 性は Ore 表示から従う。

この四次元 Z-domain の定理は、任意 n の graded 定理で用いる noetherian 有限生成加群の議論とは別の証明である。
重み次数2の正規元商が一般に大域次元を下げる、と主張しているのではない。
語長二次表示と語長保存の1周期同型によって、z が通常次数1となる grading を確保している。

## 重み2生成元族の正則性による整域判定

`idx:prop:z-regular-criterion` は、Q の語長二次表示を一つ選んだとき、
重み2・語長1の全生成元 z_i が左右正則であることと、A が Z-domain であることの同値を示す。
7周期により z_0,...,z_6 の七つへ還元できる。ただし各生成元の左右乗法の単射性は
**全ての合成可能な次数成分**について要求され、有限次数の計算だけで判定できるとの主張ではない。

逆向きの依存順序は次の通りである。

1. z_i の正則性だけから重み3・5の関係射影が単射となる。AS対合と七行 Euler 式に加え、左乗法による h_i(u) >= u h_{i+2}(u) と 2 の mod 7 での生成性を用いて標準型を強制する。
2. z_i での約分だけによって正規元族と2周期を構成し、7周期と組み合わせて1周期の graded 代数 D を復元する。この段階で D の整域性はまだ使わない。
3. 正則正規元 z に Rogalski–Zhang **Lemma 1.1** を語長 grading で適用し、Rees の補題から AS-Gorenstein 性を移して D/(z) が AS 正則次元3であることを得る。**Corollary 1.2 の声明は親代数の domain 性を仮定するので、これをそのまま逆向きの根拠にはしない。** 必要なのは Lemma 1.1 と、Corollary 1.2 の証明でも使われる正則正規元に対する Rees の補題である。
4. Rogalski–Zhang **Lemma 1.3(c)** により D が strongly noetherian、Auslander regular、Cohen–Macaulay となる。ここでは noetherian 性を次の段階に使用する。
5. 標準語長 Hilbert 級数 (1-u)^(-4) から GK dimension 4 を確認し、Lu–Palmieri–Wu–Zhang **Lemma 1.3** により D が domain となる。これを associated Z-algebra へ移す。

Rogalski–Zhang Lemma 1.3(c) の条件は、同論文の連結・次数1生成の設定で、
正則な斉次正規元 f を持ち、D/(f) が AS 正則次元3であること。
この判定では語長 grading を使うためその設定を満たす。
D/(z) の整域性、重み2関係の二因子階数、Ore 表示を途中で先取りしない。

LPWZ の [著者PDF](https://sites.math.washington.edu/~palmieri/Papers/hiext.pdf) の
Lemma 1.3（PDF p.6）を直接確認した。noetherian・connected graded・AS正則・
global dimension 4・GK dimension 4 から domain を結論し、次数1生成を要求しないと明記している。
同箇所が根拠として挙げるのは **Artin–Tate–Van den Bergh, Theorem 3.9**、
*Modules over regular algebras of dimension 3*, Invent. Math. 106 (1991), no.2, 335–388（LPWZの書誌 [ATV2]）である。
今回直接確認したのは LPWZ におけるこの声明と出典表示であり、ATV2 原典の当該証明は直接再確認していない。

Sierra **Theorem 1.2 = Corollary 4.4** は、associated Z-algebra の添字保持同型と
Zhang twist の同一視を与え、degree 1 生成を要求しないことを本文で再確認した。
従って、1周期性と Ore 表示を得ても全 indexed 同型軌道の分類が自動的に終わるわけではない。

## 新規性と追加調査

整域部分の標準型・1周期性・Ore 構造は上記の各証明に依拠する。
一般の Frobenius Ext 圏、周期からの graded 復元、正則正規元商、Ore 正則性保存は既知の結果である。
本研究の具体的な組合せと、既存の重み付き AS 正則代数・正規拡大の分類との
完全な文献照合、新規性の最終確認は未完了である。

語長二次性を外した四次元 graded 網羅定理は、左右 noetherian、指定 Hilbert 級数と
最小生成元条件を仮定し、上表の LPWZ の domain 定理を使う。
この仮定付き定理と、語長二次の Z-domain から Hilbert 級数・noetherian 性まで導く定理を区別する。
任意 n の語長二次 graded 定理でも、現在は noetherian 性と指定 Hilbert 級数を仮定している。

全Qでの `idx:thm:outer-relation-ranks` は、重み2・5の関係数が各1であることを証明する。
純jump 1部分のbar複体と七周期monodromyから数値的二分岐を導き、
零関係の位置の制約と代数閉体上の積型線型汎関数によって有限幅を排除する。
これは有限次数のHilbert一致や、計算で残った数値表をAS対象と認定する議論ではない。
この具体的な強制結果の新規性は未確定である。

`idx:thm:mixed-relation-ranks` は、さらに全Qで r_3=r_4=2 を証明する。
正係数の行列Hilbert級数を用いる解析的な必要条件の導出と、
`computations/verify_mixed_ranks.py` による890整数列の網羅的な行列式検査を組み合わせる。
`idx:cor:all-standard` の Q=H=S はこの計算補助部分を含む結果である。
一方、整域部分の七行Euler式による標準型強制は計算非依存の別証明として保持する。
必要な数値型をAS条件から絞ることと、候補のAS正則性を有限次数で認定することは異なる。
新規性の最終確認、形式化、外部査読は未完了である。

n>=3の整域については、添字付き二段Ore表示の無条件の網羅性と基礎Z-代数のAS性が未解決である。
n=3の混合関係数・Koszul性・標準Hilbert級数は証明済みであり、その強制が残るのはn>=4である。
任意nでのAS基礎代数を仮定した二段Ore定理と、n=3でのBの1周期性による同値判定は、
この未解決範囲を正確に切り分ける結果である。
n=2の全分類では、Q 全体の整域性、混合関係射影の非退化性、非整域対象の存在と分類、一般の同型軌道の幾何・成分・特殊化が残る。
n=2の整域性の自動性に関する具体的課題は、七つの z_i の左右正則性である。
最小語長の零化元を仮定し、最小解消・AS対合・関係射影と syzygy から排除できるかを調べる。
最小周期7または非定数の射影階数が現れるとすれば、ある z_i の左右正則性が破れる部分に限られる。
対角族の同型判定と二同型類の基準族・射影階数分岐についても、既存の重み付き/Ore 族との完全な先行結果照合は未了である。

## 一般の最小生成元次数 (1^n,2,3)

`papers/nc-p1123.tex` は、左右 noetherian、指定大域次元と Hilbert 級数を持つ
語長二次の graded algebra について、全 n の Koszul 性・関係数を導き、
domain を加えた部分の canonical Ore 表示を網羅する。
商 A/(z) の domain 性を追加仮定する必要はなく、二変数 Hilbert 級数と
noetherian 有限生成性による成長度の議論から導く。
一般の高次元 AS-regular algebra が常に domain であるという主張は使用しない。
基礎代数の AS 性は、その後の正則正規元の商から得る。

| 文献 | 確認した一次資料と箇所 | 適用 |
| --- | --- | --- |
| Carvalho–Lopes–Matczuk, *Double Ore Extensions versus Iterated Ore Extensions*, arXiv:0909.3238v1 (2009) | [本文](https://arxiv.org/pdf/0909.3238), Definition 1.1、Theorem 2.2(a),(b)（PDF pp.6–7） | genuine graded double extension において、最小次数2,3から Sigma_12=0 が従い、固定順の2段 automorphism Ore 表示を得る。一般の2段Ore族の全てがdouble Oreであるとはしない。 |
| Iyudu–Shkarin, *Three dimensional Sklyanin algebras and Gröbner bases*, J. Algebra 470 (2017), 379–419; arXiv:1601.00564v2 | [本文](https://arxiv.org/html/1601.00564v2), Theorem 1.1、Theorem 1.2、Corollary 6.1 | S(1,2,1)のKoszul性・Hilbert級数・3-CY性。本文の直接の行列計算により、どの2次元一次部分空間内にも二次関係がないことを証明する。 |
| Levasseur, *Some properties of non-commutative regular graded rings*, Glasgow Math. J. 34 (1992), 277–300; DOI 10.1017/S0017089500008843 | [出版社PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/244AE0A8E9C8AB6782515B504F1AC5C0/S0017089500008843a.pdf/some_properties_of_noncommutative_regular_graded_rings.pdf), Theorem 6.2(i), p.297 | 次数1生成のAS正則次元3の代数のnoetherian/domain性をSklyanin例に適用する。 |

LPWZ Lemma 1.1 と Theorem 1.9 は最小解消の双対性とFrobenius Extを与える。
原稿では二重次数の保持を説明し、差次数0のbar複体を明示する。
LWW Theorem 3.3 は一般斉次Ore族と、固定最小次数で次元が無界となる族の逆構成に用いる。
同論文の定義は有限GK次元を含まないため、成長は各Ore基底のHilbert級数から別に確認する。
追加仮定を明記した一般 n の語長二次graded網羅定理、
AS基礎代数だけを追加したindexed構造定理、任意の斉次関係のOre部分族の記述は区別する。
これらの結果と既存文献との完全な同定・新規性の確定は未了である。
