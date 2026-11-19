# 一次文献・外部依存の現行索引

2026-11-19 / v17。読んだ箇所と適用範囲を区別する。外部PDFは同梱しない。
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
| Iyudu–Shkarin, *Classification of quadratic and cubic PBW algebras on three generators*, arXiv:1806.06844v1 (2018), 本稿引用キー `ISclass` | [一次本文](https://arxiv.org/html/1806.06844v1), §1の基礎体とクラスΩの定義、Theorem1.11の分類声明、Remark1.15、§12.1 | 代数閉体・標数≠2,3上の通常の次数1生成二次代数で、H=(1−t)^−3ならdomainとAS正則次元3が同値である。本稿の二周期Z-代数の認識定理に対する既知の一頂点基準として比較する。`p2base:thm:as3` とn=3の無条件Ore定理の証明はこの分類に依存せず、非1周期Z-代数へ分類を直接適用しない。分類表全件と各証明の独立再検証を実施したとはしない。 |
| Rogalski–Sierra, *Some noncommutative projective surfaces of GK-dimension 4*, arXiv:1101.0737v2 (2011), 本稿引用キー `RSsurface` | [一次本文](https://arxiv.org/html/1101.0737v2)、[PDF](https://arxiv.org/pdf/1101.0737), Theorem 1.1、解消 (1.2)、Theorem 1.6、Proposition 5.4の(5.5)–(5.6)、Proposition 5.11(1) | 通常の連結次数付きnoetherian整域で、Koszul、GK次元・大域次元4、線型Betti型14641、H=(1−t)^−4であってもAS–Gorensteinでない例。非可算代数閉体上の代数的に独立な二パラメータで成立し、特にC上で取れる。一般的な数値認識法の障害である。一方、本稿の十条件同値定理によりQ₄^domの純基礎として実現しない。最上写像(0,0,z₉,z₁₀)^Tと親AS由来の階数下界からも非実現を確認できる。 |
| Martínez-Villa–Solberg, *Artin–Schelter regular algebras and categories*, JPAA 215 (2011), 546–565; DOI 10.1016/j.jpaa.2010.06.006 | [arXiv:0902.1119](https://arxiv.org/pdf/0902.1119), Def.5.7、Lemma6.1(b)、Thm.6.2(a),(b) とその証明 | 有限生成射影解消と AS 双対性から得る Hom–Tor 双対、接続準同型との両立、Yoneda 積による完全対合を確認。全単純加群を取ると AS 添字の全単射が必要な安定性を与える。語長 Koszul 性と7移動は本稿の仮定から別途証明し、一般原理そのものを新規性としない。 |
| Rogalski–Zhang, *Regular algebras of dimension 4 with 3 generators*, arXiv:1101.1998v2 (2011) | [本文](https://arxiv.org/pdf/1101.1998), §1冒頭の次数1生成の設定、Lemma 1.1とそのchange-of-rings証明、Cor.1.2、Lemma 1.3(a),(c)（PDF pp.3–4） | Lemma 1.1 は連結graded・有限大域次元と次数1の正則正規元だけで商の大域次元を1下げ、noetherian性も商のdomain性も要求しない。語長1のzに適用し、交代barテンソルと合わせて全nの通常Koszul枝の混合射影を非退化にする。Cor.1.2は親domainの下でAS性を比較し、得られたOre商のwに適用して基礎AS性を得る。Lemma 1.3(a)はn=3の第1段Cのnoetherian性、同(c)は重み2正則元族からの整域判定に用いる。 |
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

### n=3の数値型・Ore構造・通常のgraded代数への下降

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

`p2base:thm:as3` は、標数0の代数閉体上で、隣接成分から生成される
正連結・局所有限な二次Z-domain Bが2周期で、
dim B_(i,i+m)=binom(m+2,2) を満たせば、左右Koszul・AS正則次元3・AS移動3となることを証明する。
noetherian性、Koszul性、1周期性はいずれも仮定しない。
標準二次表示複体の核と三次syzygyの単射像をHilbert級数で比較することで、
Betti数 (1,3,3,1) の左右線型解消を導く。

AS性を得るための退化syzygyの排除には、`p2base:lem:fraction-frame` を用いる。
二頂点foldの各cornerの多項式増大から左右Ore性を直接証明し、
二つの三次元生成空間X,Yの全交代積と次元を一つの分数斜体に保つ。
両端flatteningの階数 (2,2) の場合、異なるsupportには
dim XY=dim YX=6と一変数有理写像の合成次数から矛盾を得る。
等しいsupportには、P¹上の極因子の次数を使って交代積の線形成長を導き、
標準Hilbert数値の二次成長と矛盾させる。
最後にKoszul双対の完全対合とKoszul双加群解消から、左右AS性と大域次元3を確認する。

この証明は通常の一頂点代数の分類を使わず、本稿内で完結する。
上表の `ISclass` は、同じHilbert級数を持つ通常のgraded代数について
domain・twisted potential・AS3の対応を与える重要な比較先である。
二周期対象の認識定理では1周期への下降を先取りしない。
Ore局所化、Segre多様体による階数判定、有理写像の次数、P¹上の有効因子の次元公式、
Koszul双対は既知の道具であり、この組合せによる二周期認識の完全な先行結果照合と新規性確認は未完である。

`genidx:thm:three-light-ore` は、n=3の数値型によって純jump 1部分Bに上の認識定理を適用し、
BのAS3性と `genidx:thm:as-base-ore` から、全てのA∈Q₃^domのindexed二段Ore表示を導く。
Bには2周期とAS移動3があるので1周期でもある。

`genidx:thm:three-light-descent` は、さらにn=3の全対象A自身の1周期性を証明し、
通常の三生成元二次AS3代数を基礎とするgraded二段Ore表示へ下降させる。
この証明は、Aの2周期と8周期だけから1周期性を結論するものではない。
`genidx:prop:three-light-derivation-support` の係数の零集合の二分岐を保持し、
零補正の枝は正規元族wによる3周期、非零枝は以下の有限次元の延長で扱う。

共通表示では、zv=Svz、wv=Svw+ℓ_i(v)z²、wz=zw とでき、
E=span{ℓ_i}上の移動T(ℓ_i)=ℓ_(i+1)は可逆でT²=S*を満たす。
dim E=0,1,3では、Sと可換な基礎代数の自己同型PでT=P*|_Eを満たすものを直接構成する。
dim E=2では、Ann(E)が直線であることと整域性を使い、
商上のQ=T*の可能性を相異なる相反固有値または固有値1のJordanブロックへ絞る。
前者には対角写像、後者にはSのunipotent部分の平方根を用いてPを構成する。
これがA(1)≅Aを与える。分類に用いたブロック条件と各場合の排除・延長は本稿内で証明し、
三次元AS代数の外部分類には依存しない。

下降後の基礎代数は、共通表示のB₀=T(V)/(R)に対して
B′=T(V)/((id⊗P)R)である。
交換係数はSP^(-2)、SP^(-3)、ℓ₀P^(-3)となり、wz=zwを保つ。
B′はB₀のZhang twistであり、通常のgraded同型でB₀そのものと同一視しない。
Sierraの一般的なtwist/associated Z-algebra対応は既知であるが、
この具体的な延長と下降を既存分類と完全に照合したものではなく、新規性は未確認である。
二段表示と下降の網羅性は、全てのOreデータや基礎代数を含む同型軌道の完全分類とは異なる。

n=3の左右noetherian性は、下降後の第1段C=B′[z;σ′]に
Rogalski–Zhang Lemma1.3(a)を適用して得る。
Vとzを全て次数1とする語長次数ではCは連結・次数1生成であり、
基礎B′はAS正則次元3、σ′は次数付き自己同型なので、同論文の設定を満たす。
得られたCの左右noetherian性と、第2段のθ′の可逆性から、
通常のOre Hilbert基底定理によりD=C[w;θ′,δ′]は左右noetherianである。
A≅check(D)へ移すと、各行は右noetherian、各列は左noetherianとなる。
Lemma1.3(a)のより強い結論を、ここでのAの結論へ追加してはいない。

### n=4の最高差次数と純基礎部分の数値制約

`n4:lem:periodic-pd3-obstruction` は、各頂点の隣接生成元がm>=4本ある周期的な二次Z-domainについて、
多項式増大と有限生成射影による単純解消を保ったまま、全単純加群の射影次元を3以下にはできないことを証明する。
ここでの周期性は代数同型によるものであり、Hilbert数列の周期だけではない。
折畳Hilbert行列のcJ主部、Euler行列の行・列の均衡、巡回シフトの正定値性と
零固有値の二次微分の平方完成を使う。逆行列の非負性との矛盾まで本文で直接証明し、
有限候補の探索を必要としない。

`n4:cor:top-excess-three` は、A∈Q₄^domの最高語長NとAS移動LについてL−N=3を無条件に与える。
D>=4なら差次数零のbar複体とAS対合により純jump 1部分Bの単純射影次元が3以下となるため、上の補題に反する。
D>=3は重み5関係が全て消える場合の指数増大を排除して得る。

`n4:prop:pure-base-numerics` は、s=N−2>=4、L=s+5として、Bの右単純解消を
(1,0), (4,1), (r_i,2), {(p_(i,j),j):3<=j<=s−1}, (q_i,s)
へ絞る。q_i=r₅(i+s)∈{0,1}は全て零ではなく、
r_i=3+Σ_j p_(i,j)−q_i および Σ_(i,j)(j−2)p_(i,j)−(s−2)Σ_i q_i=2L が成立する。
これらは必要条件であり、一般の場合のs=4やKoszul性までを得たとはしない。

`n4:prop:koszul-base-numerics` は、語長Koszul性、同値にN=6を追加すると、
Bの線型型14641、全r₂=6、全r₅=1、H_B=(1−u)^−4を証明する。
Euler行列の二つのI−uS因子を取り出し、qに欠損があれば残る非負行列のスペクトル半径が
区間(0,1)内で1となってEuler逆行列が発散することから矛盾を得る。
これはn=4の無条件のKoszul性を証明したものではない。

`n4:thm:koszul-numerics-period` は、同じKoszul条件の下で混合関係数も飽和し、
全関係数(6,4,4,1,0)、標準二変数Hilbert級数とA自身の1周期性を与える。
差次数変数を固定したEuler行列を(I−uS)K(u,v)(I−uS)へ因数分解する。
混合関係の欠損α_i=4−r₃(i)があれば、det K(1,v)=−9(Σα_i)v+O(v²)となり、
小さいv>0に対してH_Aのu=1での極は高々2位となる。
これは純粋部分の4位の極と矛盾する。
飽和した関係数から正規元族zの2周期を得て、AS移動9と合わせて1周期性を得る。
下の `n4:thm:equivalent-criteria` は、基礎AS4性、二段Ore表示、全始点r₃=4・r₅=1を含む十条件の同値性へまとめる。
各条件の自動性は未証明だが、標準枝におけるB-AS4と第二段Ore表示は、noetherian性を追加せずに証明した。

行列Hilbert級数、Hopf不等式、固有値の摂動、非負行列の一般的手法は既知であり、
この具体的な周期解消の障害・数値型強制の新規性の最終確認は未完である。

### 四生成元の標準数値型からAS性を結論できない既知の障害

Rogalski–Sierraの上記一次資料では、Theorem 1.1がnoetherian・domain・Koszul・
GK次元4・大域次元4とAS–Gorensteinでないことを同時に述べる。
式(1.2)は0→R(−4)→R(−3)^4→R(−2)^6→R(−1)^4→R→k→0という線型解消であり、
H_R=(1−t)^−4も従う。Theorem 1.6は、非可算代数閉体上で二つのパラメータが素体上代数的に独立な場合に、
これらの結論を満たす具体的なR(τ)を与える。特に複素数体上で例を取れる。

従って付随Z-代数は1周期であり、2周期も持つ。
有限大域次元、整域性、Koszul性、線型Betti型14641、標準Hilbert級数、noetherian性、1周期性の
全てを用いても、一般の四生成元基礎候補BにAS4性を認定することはできない。
n=3の認識定理を生成元数だけ変更して適用する方針は、この既知の例によって排除される。

これらの例はQ₄^domの純jump 1部分として実現しない。
実現すれば、標準純粋Hilbert級数から十条件同値定理によりB-AS4が従い、矛盾する。
従って、対象内の二段Ore命題の反例ではない。

さらにProposition 5.4の(5.5)–(5.6)で、右最小解消の最上写像は(0,0,z₉,z₁₀)^Tと明示され、
Proposition 5.11(1)が該当パラメータでの正確性を保証する。
片側top flatteningの階数は高々2である。
研究ノートの親完全対合による補助計算は、標準n4対象の純粋top両階数が少なくとも3であることを与えるため、
この階数だけからも当該族の非実現が分かる。

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
この条件付き定理と、n>=4でBのAS性を全対象から導く未解決問題を区別する。
n=3では上の二周期基礎代数の認識定理によって、この追加仮定を対象の条件から導いた。
mapping cone、完全対合、PBWからのOreデータの構成は既知の方法である。
この仮定の組合せと結論の既存文献との完全同定、新規性の最終確認は未完である。

### 通常の次数付きKoszul対象での数値型と二段Ore表示

`ogk:lem:generator-bound` は、通常の連結Koszul代数が有限生成射影による有限解消と多項式増大を持つとき、
生成元数が大域次元以下であり、両者が等しければH=(1−t)^−nと二項Betti数になることを直接証明する。
スカラーEuler多項式の全根の絶対値、最高次係数、一次係数を比較する。
AS–Gorenstein性は仮定も結論もしていない。

`ogk:thm:numerics` は、通常の連結次数付きAS正則整域、次元n+2、最小生成元次数(1^n,2,3)、
有限生成射影による有限AS解消、多項式増大、語長Koszul性から、
AS添字n+5、標準二変数Hilbert級数、関係数(binomial(n,2),n,n,1,0)を導く。
noetherian性と指定Hilbert級数は不要である。
純jump 1部分Bは大域次元nのKoszul整域でH_B=(1−t)^−n、zは正則正規元であり、第1段はB[z;σ]となる。
全ExtのAS対合、差次数零のbar複体、差次数1のYoneda成分と上の根の議論を使う。
続く `ogk:thm:ore-without-noetherian` は、同じ仮定から基礎BのAS正則性と二段Ore表示までを導く。
第二段の構造にもnoetherian性と指定Hilbert級数は不要である。
一般の周期的Z-代数ではHilbert級数が行列の逆行列となるため、
スカラー根の議論をそのまま適用して1周期性やKoszul性を補うことはできない。

`bar:lem:two-cycle` は、非零の一次斉次元a,bがab=ba=0を満たせば、
交代純テンソルが全dでTor_(d,d)(k,k)の非零元を与えることを、正規化bar複体で直接証明する。
内部語長dにd+1次bar項がないため、これらのサイクルは境界にならない。
この一般的な障害はKoszul性を必要としない。

`bar:lem:normal-square` では、wz=c zw、zv=σ(v)zの下でwv=λz²が成立すると、
親代数の整域性による約分からσ(v)=cv、vw=λc^(−2)z²となる。
Q=A/(z)にはv,wの両順序の零積が生じるが、語長1のzへのRogalski–Zhang Lemma 1.1の適用でQは有限大域次元となる。
交代barテンソルと矛盾するので、この退化は存在しない。
`bar:cor:mixed-projections` は両混合射影の単射性を与え、標準関係数から両者は同型となる。
既知のHilbert級数と整列語の比較によりPBW基底を得て、自己同型・導分の係数を構成する。
Q=B[w;μ]の整域性・wの正則正規性はこの後に従い、再び正規元商を用いてB-ASnを得る。

ここで使う正規元商の有限大域次元は既知結果であり、Lemma 1.1の本文と証明を一次資料で再確認した。
交代barサイクルと本対象の交換関係を組み合わせた具体的な仮定削減について、新規性の最終確認は未完である。
一般AS基礎代数や得られたOre代数のnoetherian性を自動的な帰結とはしない。
`ogk:cor:noetherian-ore` は、Aの左右noetherian性を追加した場合にB=A/(z,w)も左右noetherianになることを記録する。

`n4:thm:equivalent-criteria` は、Q₄^domにおいて、語長Koszul性、N=6、Aの1周期性、
純基礎Bの1周期性、Bの全行Hilbert級数が同一であること、全行H_B=(1−u)^−4、
B-AS4、AS4基礎上の添字付き二段Ore表示、AS4基礎上の通常graded二段Ore表示への下降、
全始点r₃=4・r₅=1の十条件を同値にする。
全行Hilbert級数が共通のh(u)なら、p_i(u)h(u)=1からEuler多項式の全係数は始点によらず、q_iは全て1となる。
スカラーEuler多項式の根が単位円上にあることから自己相反性が従い、
s>=5では正の二次係数と非正の(s−2)次係数が等しくなる矛盾によってs=4へ限定する。
これがN=6とKoszul性を与え、上の混合数値型定理がAの1周期性を与える。
通常の下降への `ogk:thm:ore-without-noetherian` の適用でB-AS4と二段Ore表示が従い、
逆にB-AS4から一般AS-base定理を通じてBの1周期性へ戻る。
最後の階数条件とB-AS4の同値性は `igraph:thm:normal-z-ore` による。
十条件のいずれかが無条件に成立することを証明したわけではない。
標準枝でのB-AS4と第二段Ore表示は別の未解決問題として残らない。
`n4:cor:noetherian-periodic-ore` は、通常の下降がさらに左右noetherianの場合の基礎noetherian性を記録し、
noetherian性自体の自動性は結論しない。

### 二つの混合階数による任意nのindexed構造判定

`igraph:thm:normal-z-ore` は、全A∈Qₙ^domについて、全始点r₃=n・r₅=1、
純基礎Bの左右AS正則次元n、AS基礎B上の添字付き二段Ore表示を同値にする。
B-ASでは有限生成射影による有限AS解消を要求する。
Hilbert級数・Koszul性・noetherian性を追加せず、D=3、r₄=n、Bの1周期性、
一般AS-base定理のシフトとHilbert因数分解、AとBのKoszul性の同値も得る。
無条件の全次元問題は、r₃=n・r₅=1の自動性へ還元された。

`igraph:lem:as-graph-ore` が、混合射影の非退化性からPBWと基礎AS性へ進む箇所を担う。
正規商の二周期foldは、自由純部分F=T_S(V)の自己同型μを用いてQ=F[w;μ]/(R)と書ける。
w次数jの係数イデアルはI_j=(R,μR,…,μ^jR)で、有限次元F₂内の増大列により有限段で安定する。
よってG=H_Q(I−tT)はtの多項式行列で、有限解消のEuler行列とPG=I−tTを満たす。
AS対合が最高係数P_J(x)=(−1)^d x^a ΠP₀(x⁻¹)^Tを与え、これは可逆である。
従ってJ+deg_tG=1、J=1、G一定となり、I₁=I₀からμR=Rを得る。
QのOre表示とw正則性を導いた後でB-ASを降下させ、一般AS-base定理を適用する。
主論文に全証明を収め、研究ノート `note:normal-z-ore` に依存関係を記録した。

通常の一頂点の場合は、スカラーEulerの次数加法性によってAS対合を不要にできる。
研究ノート `note:ordinary-graph-finite-res` は、μが可逆な混合グラフ表示とk_Qの有限生成有限解消だけで、
μR=RとOre表示を証明する。AS性・整域性・Koszul性・noetherian性・多項式増大は不要である。
行列の場合の最高係数可逆性と、スカラーの場合の次数加法性を混同しない。
有限安定化・Euler式・AS対合は既知の道具であり、この具体的な判定の新規性の最終確認は未完である。

### Hilbert級数またはKoszul性を用いる系

`ibar:thm:standard-hilbert-ore` は、A∈Qₙ^domに全行の標準二変数Hilbert級数を追加すると、
純jump 1部分B上の添字付き二段Ore表示を与える。
Bは1周期的なKoszul AS正則次元nの整域となり、Aも語長Koszulとなる。
noetherian性、Koszul性、基礎AS性、Aの1周期性は追加仮定しない。
ただし、標準Hilbert級数の自動性をこの定理から導いたとはしない。

語長2の係数比較で標準関係数を得て、z正規族による2周期同型で折り畳む。
次数零部分k²に対する次数1の正則中央元による商の二行スペクトル系列を直接証明し、
商の単純Torが有限長となることを得る。
退化した混合関係は商で逆向きの二つの矢の両順序の零積を作るため、
k²上の交代barテンソルが与える無限のTorと矛盾する。
その後にHilbert級数との比較でPBW基底と第二段Ore表示を得て、二つの正規元商からB-ASnを得る。
これは通常の連結代数に対するRogalski–Zhangの声明をそのまま多頂点へ引用したのではなく、
必要な半単純次数零部分への拡張を本文で証明したものである。

`ibar:cor:normal-z-rank` は、標準Hilbert級数・Koszul性を仮定せず、
全r₃=n、r₅=1からr₄=nを導く。
bar障害による上界と、商の二周期Golod–Shafarevich行列・多項式増大による下界を組み合わせる。
この階数の強制が一般階数判定の最初の段階を与える。
AS混合グラフ補題を組み合わせると、同じ仮定だけでPBWと全二段Oreを得る。
階数条件成立後の関係保存性とPBW分解は未解決箇所ではない。
一般的なbar・スペクトル系列・Golod–Shafarevich法は既知であり、具体的な組合せの新規性は未確定である。

`ibar:cor:koszul-normal-z` は、A∈Qₙ^domに語長Koszul性と全r₃=n、r₅=1を追加すれば、
標準Hilbert級数を仮定せずにBのKoszul AS正則性、添字付き二段Ore表示、L_A=n+5、標準二変数Hilbert級数を導く。
正規商Q=A/(z)のKoszul性は二行スペクトル系列から従う。
Qのbar複体のw次数零部分がBのbar複体に一致するので、BのKoszul性を先に導ける。
2周期foldのExt代数Eは、F=Ext_BについてE=F⊕Fη、Fη=ηF、η²=0となる。
各頂点の最高w次数1のFrobenius対合がdim F=dim Fηを与え、η乗法は同型となる。
λ_F(f)=λ_E(fη)が非退化であることからB-ASnを得て、既存のAS-base定理を適用する。
基礎AS性・Hilbert級数・noetherian性の先取りはない。
主論文の同系は一般階数判定を適用する短い証明とし、上のExt分解による完全な別証明は
研究ノート `note:koszul-normal-z-frobenius` に保持する。一般階数判定はこの別証明を使わない。

### 純基礎Euler条件だけを使う方法の限界

研究ノート `note:n4-pure-euler-obstruction` は、s=5、N=7、L=10に対し、
非負Betti数、q≡1、行・列の均衡と一次モーメント、単位円上の行列式の根、
全次数での正の形式Hilbert係数、多項式増大、共通の最高Laurent係数、Hopf次元不等式を満たしながら、
行Hilbert級数が一定でない形式数値データを与える。
det P=(1−u¹⁰)³(1+u²⁰)と、各剰余類の二次準多項式を用いた全次数の証明をノートに記載した。
整数再帰と有限個の係数不等式の検査は `computations/verify_n4_pure_euler.py` で再現する。
これは計算補助の形式的数値結果であり、二次代数、最小解消、親AS6を実現したものではない。
十条件自動性の証明では、純Eulerデータだけでなく、実際の関係・中央Ext完全対合・混合Eulerの追加構造が必要である。

研究ノート `note:n4-s5-period-two-obstruction` は、s=5の一般の純基礎係数列に2周期性を追加すると、
二頂点のdet Kに対する単位円上の根の条件とBetti非負性が矛盾することを解析的に証明する。
これは表示した十周期列を全て排除する主張ではなく、2周期の枝についての追加の障害である。

`note:n4-parent-mixed-obstruction` は、表示した十周期純モデルの親AS6が存在すると仮定した場合に、
中央混合数値を20個の整数a_i=r₃(i)、b_i=r₄(i)へ還元する。
二次関係の交叉からSegre上界を加え、全親Euler行列の三位以上の極が、
残る行列束の行列式 det K(v)≡0 を要求することを示す。
一次係数を通る表示された一つの混合延長は、二次係数−942によって厳密に排除される。
**純モデルの全混合延長を排除したわけではない。** 全係数の同時消滅、二次代数の実現、AS完全対合の実現を別々に残す。
整数恒等式の再現コードは `computations/verify_n4_parent_mixed.py` である。
表示した計算は担当エージェントと主担当がそれぞれ実行し、現行入力の全恒等式を厳密に照合した。
実行・照合状態は `research/validation.json` に記録する。

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
上の通常Koszul対象の結果は本稿内のスカラー根の証明に依拠し、
Kabbajの特定の定理を同一仮定で引用して得たものではない。根・Euler多項式の方法自体に新規性を主張しない。
n=3では上記の直接証明によって数値型と基礎代数のAS3性を確定しており、このsurveyから補ってはいない。
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

この四次元Z-domainの定理は、三次元商のAS完全対合による独立の証明である。
任意nの通常Koszul対象についても、交代barテンソルの排除によってnoetherian性なしの構造定理を得た。
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
任意 n の既存の語長二次 graded 定理は、noetherian 性と指定 Hilbert 級数を仮定する。
一方、`ogk:thm:ore-without-noetherian` は語長Koszul性を仮定することで、
指定Hilbert級数とnoetherian性の両仮定を除く。
両定理の仮定を混同しない。

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

n=1,2,3の整域については、添字付き二段Ore表示の無条件の網羅性を証明した。
n=2,3では全対象の1周期性と通常のgraded二段Ore代数への下降も証明した。
これらの整域対象の左右noetherian性も結論であり、追加仮定ではない。
n=1では1周期化の必要十分条件があり、これを満たさない最小周期2の整域が存在する。
n=4では最高差次数D=3と純基礎部分の解消制約を無条件に得た。
語長Koszul性を追加した全標準型と1周期性を証明し、逆に1周期性から語長Koszul性も導いた。
これらはBの1周期性、Bの全行Hilbert級数の一致、Bの標準Hilbert級数とも同値である。
さらに基礎BのAS4性、添字付き・通常の二段Ore表示、全始点r₃=4・r₅=1を含めた十条件が同値である。
任意nの通常Koszul対象では、noetherian性やHilbert級数を追加せず全標準型・基礎AS性・二段Ore表示を得る。
任意nの一般indexed対象でも、r₃=n・r₅=1が基礎AS性と二段Ore表示の必要十分条件である。
n>=4では二つの階数条件の自動性が未解決であり、n=4では上の十条件の自動性と同じ問題である。
Koszul性や標準Hilbert級数を先に解くことは必須ではない。各次元での下降条件は別に扱う。
n=3の基礎代数とOreデータを含む同型軌道の完全分類は残る。
n=2の全分類では、Q 全体の整域性、混合関係射影の非退化性、非整域対象の存在と分類、一般の同型軌道の幾何・成分・特殊化が残る。
n=2の整域性の自動性に関する具体的課題は、七つの z_i の左右正則性である。
最小語長の零化元を仮定し、最小解消・AS対合・関係射影と syzygy から排除できるかを調べる。
最小周期7または非定数の射影階数が現れるとすれば、ある z_i の左右正則性が破れる部分に限られる。
対角族の同型判定と二同型類の基準族・射影階数分岐についても、既存の重み付き/Ore 族との完全な先行結果照合は未了である。

## 一般の最小生成元次数 (1^n,2,3)

`papers/nc-p1123.tex` は、左右 noetherian、指定大域次元と Hilbert 級数を持つ
語長二次の graded algebra について、全 n の Koszul 性・関係数を導き、
domain を加えた部分の canonical Ore 表示を網羅する。
商A/(z)のdomain性は追加仮定せず、混合射影の非退化性とHilbert級数から得るOre表示の後に導く。
通常Koszul対象では、交代barテンソルの排除を使う `ogk:thm:ore-without-noetherian` により、
noetherian性と指定Hilbert級数を追加せず同じ構造結論を得る。
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

## 重み5関係の行列GS飽和

`genidx:lem:r5-gs-saturation` は、周期的な二次Z-domainの多項式行増大から、
3∤Lなら全r5=1、3|Lなら少なくとも一つの法3剰余類上で全r5=1を導く。
既存の単項式商による非零位置数の下界より強いが、整域性によるrank上界を使う点を区別する。
最初の二段の行列Golod–Shafarevich不等式、S³軌道平均、正の左ベクトルの一次補正による直接証明を主論文に記載した。
標準的なGS原理自体の新規性は主張せず、今回の具体的な重み・周期による飽和基準の重複調査は未完である。
AS性・Koszul性・有限大域次元・noetherian性は補題に不要。3|Lで他の剰余類まで飽和すると読み替えない。
