# nc-p1123 研究指示

2026-11-19 / v14。最初に `research/plan_ja.tex` を読む。
主論文は `papers/nc-p1123.tex`、本文外の有効な知識は `research/notes_ja.tex`。
現在の証明位置・未解決事項・次の具体的操作は `research/STATE.json`、
一次文献の確認範囲は `research/BASELINE.md`、検証状態は `research/validation.json`。

## 現在の目標と対象

- 現在の主目標は、任意 n>=1、primitive jumps (1^n,2,3)、AS次元 n+2 の語長二次 AS-regular Z-algebra の構造である。ユーザーは **Z-domain性を仮定してよい**と明示した。正連結・局所有限、左右AS双対性、有限生成射影による単純解消、行・列の多項式増大を保つ。基礎体は標数零の代数閉体を基準とする。
- 最新の許可はdomain性であり、Hilbert級数、noetherian性、Koszul性、PBW性、1周期性まで新たに仮定してよいという意味ではない。quadraticは最小生成元に関する語長斉次二次である。
- **単一のgraded二段Ore代数 D の付随 Z-algebra A=check D で全nの対象を尽くすという主張は偽。** n=1の反例を主論文 `genidx:thm:period-two-counterexample` に証明した。x,z,w のjumpは1,2,3、zx=xz、wz=zw、w_i x_(i+3)=x_i w_(i+1)+epsilon_i z_i z_(i+2)、epsilon_even=1、epsilon_odd=0。これは標準Hilbert、語長Koszul、左右noetherian、Z-domain、AS3・添字6であり、最小正周期2。重み4関係のzz射影階数が交互0/1であるため1周期化不能。
- 自然なindexed二段Ore表示の網羅性はn=1,2,3で証明した。n=1の全対象は主論文 `genidx:thm:one-light-ore` により、Hilbert/noetherian/Koszulを追加仮定せず二段表示を持つ。AS3とquadraticからKoszul・top語長3、domainからr_2=r_6=0、AS双対性から添字6とr_3=r_4=r_5=1を導き、topテンソルで両混合係数の非零性、Hilbert級数と整列語からPBWを得る。無条件の網羅性の残る未解決範囲はn>=4である。n=2,3は下記のgraded下降まで含む強い定理が有効。
- n=1の完全分類は `genidx:thm:one-light-classification`。正規形はzx=xz、wz=c zw、w_i x_(i+3)=x_i w_(i+1)+d_i z_i z_(i+2)、c∈k*、d_(2j)=c^(-j) alpha、d_(2j+1)=c^(-j) beta。裸の添字保持同型はc'=cかつ(alpha',beta')=s(alpha,beta)、s∈k*と同値。各cの同型類の集合は{0}⊔P^1であり、affine quotientの構成とは主張しない。全パラメータの逆構成は具体的左右解消によりAS3、word-Koszul、domain、noetherian、標準Hilbertを満たす。period 1 iff alpha^2=c beta^2（零対も含む）、他は最小周期2。上の反例は(c,alpha,beta)=(1,1,0)という特殊例である。
- 研究ノート `note:general-as-translation`：AS頂点置換は任意nで平行移動i->i+Lとなり、A≅A(L)を二次表示から復元できる。Koszul性は不要。到達可能性による整数の順序を使うためn=1も含む。L=n+5やKoszul性の自動性はこの補題の結論ではない。
- 研究ノート `note:general-normal-z`：r_3(i)=n、r_5(i)=1が全始点で成立し全z_iが左右正則なら、正規元族からA(2)≅Aを得る。domainからの上界r_3<=n、r_5<=1、r_6=0と、上界の達成を区別する。上界の達成はn=1,2,3で証明済み、n>=4では無条件に未証明である。
- 主論文 `genidx:thm:five-dimensional-numerics`：n=3の全対象でN=5、L=8、ranks(3,3,3,1,0)、語長Koszul、標準二変数Hilbert、normal-z、A(2)≅Aを追加仮定なしに証明した。純jump1部分Bは左右1331線型解消、H_B=(1-t)^-3、domain、2periodを持ち、下記の認識定理によりAS3も証明済み。証明は最高差次数D=3、folded HilbertのcJ主部・一次係数、唯一のs9/L14例外のdet=(1-u^7)^2(1-64u^7)、混合関係数の行級数比較で完結する。
- 主論文 `genidx:thm:as-base-ore`：任意nで純jump1 B自身がAS_n（有限生成射影による有限左右AS解消）ならindexed二段Oreを証明した。B-AS以外にKoszul/noetherian/Hilbert/mixed ranksは不要。r3=r4=n、r5=1、B1period、L_A=L_B+5、N_A=L_B+2、H_A=H_B(ut)/((1-ut^2)(1-ut^3))が従う。A word-Koszul iff B Koszul。B-AS自動性はn>=4では未証明なので無条件all-n exhaustionと報告しない。
- 主論文 `igraph:thm:normal-z-ore`：全Q_n^domで「全始点r3=n,r5=1」⇔「B-ASn」⇔「AS基礎B上のindexed二段Ore」。H/Koszul/noetherian/B-ASの先取り不要。`igraph:lem:as-graph-ore` は、fold2のQ=T_S(V)[w;μ]/(R)で係数イデアルI_j=(R,μR,…,μ^jR)が有限安定化することと、AS双対性で最高w Euler係数P_Jが可逆になることを使う。P G=I−tTからJ+deg_tG=1、J1、G一定、μR=R、w正則、B-ASnとなる。D3、B1period、一般AS-baseの全式も結論。元の全次元問題は二つの階数条件の自動性へ還元され、Koszul/H自動性を先に証明する必要はない。
- 主論文 `genidx:lem:one-heavy-as` は非Koszul・indexed一重生成元版。Q AS_(n+1)かつpure B AS_nからQ=B[w;mu]を得る。noetherian/Hilbert/Q-domain不要。notes `note:one-heavy-frobenius` は適用範囲と証明先を参照する。
- 主論文 `p2base:thm:as3`：2periodic（三次元ベクトル空間のHilbert周期だけでなく代数同型）quadratic Z-domain、全行H=(1-t)^-3ならAS3・AS移動3。Koszul性や1331解消は二次表示/Hilbert/domainから導く。2vertex foldの非零射分数圏へ忠実埋込みし、rank22 top tensorをX,Y⊂division ringの交代積で扱う。異なるsupportではdimXY=dimYX=6からrational f,hの合成がMöbiusとなりdimXY<=5矛盾。同じsupportではk(t)上の極因子次数O(m)からdimB_0,2m=O(m)となり標準HSに矛盾。非退化topから左右Frobenius/AS、Koszul双加群解消から全unital modulesのgldim3を得る。ordinary分類には依存しない。
- 主論文 `genidx:thm:three-light-ore`：全Q3domに無条件のindexed二段Ore表示。数値型定理→Bの2period/Hstandard→p2base認識→一般AS-base定理で証明。Bは2periodとAS3periodから1period。下記の下降定理によりA自身も1period。n3のB-AS/Ore/下降を未解決に戻さない。
- 主論文 `genidx:prop:three-light-derivation-support`：n3のL_i零集合は空か全体。AS3 baseの関係の左右全支持とdelta(R)=0から隣接Lの消滅が同値。全零枝ではwが正規元族でA3period、既存A2periodと合わせA1period。全非零枝も下記の移動作用素の延長で下降を証明済み。n1偶奇ゼロ反例の単純拡張は不可。
- 主論文 `genidx:thm:three-light-descent`：全Q3domはA1periodで通常graded二段Oreへ下降。共通frame zv=S(v)z、w_i v=S(v)w_(i+1)+ell_i(v)zz、wz=zw。E=span ell_iにT ell_i=ell_(i+1)、T^2=S*を定め、dimE=0,1,3は直接、dimE=2は相反固有値/Jordan1の場合分けでSと可換するB0自己同型Pへ延長。R'= (id tensor P)R、sigma'=SP^-2、tau'|V=SP^-3、delta(v)=(ell_0 P^-3)(v)z^2、delta(z)=0。B'は共通frameのB0のZhang twistでありgraded同型と同一視しない。語長次数で第1段へRZ Lemma1.3(a)、第2段へautomorphism Ore Hilbert基底定理を適用し左右noetherian性も結論。全軌道分類は未完。
- Iyudu–Shkarin arXiv1806.06844v1 Theorem1.11/Remark1.15/§12.1のordinary quadratic H=(1-t)^-3 domain⇒AS3は既知比較先。現行の2period認識証明はこの分類なしに直接進む。具体的定理の新規性最終確認は未完。
- 主論文 `genidx:lem:weight-five-growth`：r6=0、r5がL周期、多項式増大なら、3∤Lでr5(i)+r5(i-3)>0、非零位置数>=ceil(L/2)。3|Lでは少なくともceil(L/6)の非零位置。rank上界がなければ位置数とsum ranksを区別。notes `note:general-r5-growth-limit` は単項式商の必要十分成長条件とL2交互欠損の方法限界を証明する（AS-domain例の構成ではない）。
- graded同型、周期構造を指定した同型、裸の添字保持同型、qgr同値、導来同値を区別する。graded代数のZhang twistは裸のassociated Z-algebraで既に同一視される。1周期性はindexed Oreの定義へ埋め込まない。

## n=4 と任意nの条件付き構造の現行結果

- `n4:lem:periodic-pd3-obstruction`：m>=4の隣接生成元を持つ周期的二次Z-domain、多項式増大、有限生成simple解消の条件で、全simpleのpd<=3は不可能。folded Hilbertの主部hJ、Euler零固有値の二次変動の平方和、inverseの非負性から矛盾。Koszul/AS/noetherianを補題へ追加しない。
- `n4:cor:top-excess-three`：全Q4domでD=L−N=3。`n4:prop:pure-base-numerics`：s=N−2>=4,L=s+5、pureB解消 (1,4,r_i,{p_ij},q_i)、shift (0,1,2,j,s)、q_i=r5(i+s)∈{0,1},notall0、rank balanceとfirst moment。N6/L9自動性は未証明。`n4:thm:top-word-divisible-three` により3|N,3|Lは無条件で、非Koszul残余はN=9,12,15,…。N7/N8および全N≡1,2(mod3)は排除済み。
- `n4:prop:koszul-base-numerics` と `n4:thm:koszul-numerics-period`：wordKoszulならpureBの14641線型解消、H_B=(1-u)^-4、全mixed ranks(6,4,4,1,0)、H_A標準、L9、normalz、A1period。基礎欠損は非負行列のPF半径、混合欠損はP=FKFとdetK(1,v)=−9(sum(4−r3_i))v+O(v²)、pole<=2対pure pole4で排除。
- `n4:thm:equivalent-criteria`：A wordKoszul ⇔ N6 ⇔ A1period ⇔ B1period ⇔ pureB Hilbert rows independent of source ⇔ all H_B=(1-u)^-4 ⇔ B-AS4 ⇔ indexed二段Ore over B-AS4 ⇔ ordinary graded二段Ore over Koszul AS4 domain ⇔ 全始点r3=4,r5=1、の十条件が同値。row uniformならscalar Euler同一、q全1、unit roots/self reciprocityからs4。n4構造の残る核心は十条件の自動性である。条件成立後のB-AS4性と第二段Oreは証明済みで、追加noetherian性は不要。
- `ogk:thm:numerics` と `ogk:thm:ore-without-noetherian`：通常graded、wordKoszul、AS(n+2)、domain、polynomial growthなら任意nでD3、標準HS/ranks、B Koszul ASn、normalz、二段Ore表示を得る。H/noetherian不要。スカラーEulerの根の議論を一般indexedへ移さない。`ogk:cor:noetherian-ore` と `n4:cor:noetherian-periodic-ore` は、さらにAの通常下降を左右noetherianと仮定すればBもnoetherianとなる系であり、第二Oreのための仮定ではない。
- `bar:lem:two-cycle`, `bar:lem:normal-square`, `bar:cor:mixed-projections`：正規な語長1元zの商はRogalski–Zhang Lemma1.1により有限大域次元を保つ。混合射影の退化wv=λz²は逆積vw=λc^-2 z²も強制し、商には両積0の非零語長1元v,wが生じる。交代barテンソルは全dでTor_(d,d)を非零にするため矛盾。商の整域性やnoetherian性を先に仮定しない。有限解消・PBW・B-ASという依存順序を保つ。
- `ibar:thm:standard-hilbert-ore`：一般Q_n^domで全行H_A(u,t)=((1-ut)^n(1-ut²)(1-ut³))^-1なら、任意nでindexed二段Ore、B Koszul ASn、B1period、A wordKoszulが従う。A1period、B-AS、Koszul、noetherianは追加仮定しない。標準二変数Hの語長2係数がr3=n,r4=n,r5=1を与える。正規zの2周期foldと半単純次数零部分上のbar／change-of-rings証明を使う。A自身の1周期性を全nへ拡張しない。
- `ibar:cor:normal-z-rank`：全始点r3=n,r5=1から、H/Koszulを追加せずr4=nを得る。mixed射影の単射性と2周期商の二変数Golod–Shafarevich不等式による。`igraph:thm:normal-z-ore` が、この階数条件だけから全OreとB-ASを完成させる。`ibar:cor:koszul-normal-z` はさらにA wordKoszulならL=n+5、標準二変数Hを与える。notes `note:koszul-normal-z-frobenius` にはQの純bar複体でB Koszulを先に導き、E=F⊕Fη、η²=0とFrobenius対合からB-ASを導く完全な別証明を保持する。一般階数判定はこの別証明に依存しない。
- notes `note:ordinary-graph-finite-res`：通常Q=T(V,w)/(R,wv−μ(v)w)、μ可逆の場合、k_Qの有限生成射影による有限解消だけでμR=RとOre表示が従う。AS/domain/Koszul/noetherian/growthは不要。係数イデアルの有限安定化とスカラーEulerのt次数による。indexed行列版にはAS最高係数可逆性を使うため、この補足の適用範囲と区別する。
- Rogalski–Sierra arXiv1101.0737v2 Theorem1.1/(1.2) は、noetherian domain/Koszul/14641/gldim4/standardHでも非ASの例。ordinaryなので1periodもある。この既知例は一般の基礎代数の数値だけのAS認識を否定するが、十条件定理によりQ4domのpureBとしては実現不能。Prop5.4の最高微分(0,0,z9,z10)^Tはtop flattening rank 2を与え、親ASの混合射影との対合から得るrank>=3にも反する。親内の実現を未確認に戻さない。
- notes `note:n4-pure-euler-obstruction`：s5/N7/L10の形式的pure Eulerデータで、非負Betti階数、行列Euler恒等式、単位円上の全根、全次数の正の行Hilbert係数、多項式増大、共通最高Laurent係数、全次数のHopf不等式と、Hilbert行の始点依存性が共存する。`computations/verify_n4_pure_euler.py` は厳密整数・多項式計算で再現する。代数、最小解消、AS6対象の実現ではなく、これらの純数値条件だけで十条件を強制する方法の障害である。親AS整域への全延長は三整除性定理で排除済みである。純条件だけの方法の限界として保持する。
- notes `note:n4-s5-period-two-obstruction` はs5の一般の二周期純数値枝を解析的に排除する。`note:n4-parent-mixed-obstruction` は表示した十周期モデルの親AS6条件を20整数a_i=r3_i,b_i=r4_iと全行列束の恒等的特異性へ還元する。一次条件を通る表示1延長は二次係数−942で排除される。純モデルのAS整域への全延長は `n4:thm:top-word-divisible-three` により排除済み。`computations/verify_n4_parent_mixed.py` は担当・主担当とも実行済みで、現行入力を厳密照合した。

- `n4:thm:top-word-divisible-three`：全Q4domで3|N,3|L。3∤Lを仮定するとr5all1、heavy-w境界detP(ε²,ε^-1)=0とsimple kernelからsum r4=4L,sum r3=sum p_(s−1)。pure/mixed momentからE3pureはword s−1に集中。domain/minimal exactnessで各tail rank p_i>=2、ゆえs<=6。s5/s6は数値Eulerの実零点で排除。全証明は解析的で有限列挙なし。
- `nozz:prop:koszul-saturation`：固定wordgradingでR4のzz射影0かつwordKoszulなら、任意nで全mixed ranks標準・通常二段skew下降・B Koszul ASn。有限foldでFrob dualの4corner全射とdimF=dimE11からF→Fζη同型を導く。`nozz:cor:periodic-saturation` は同じnozz、r5all1、6∤Lの実周期からKoszulなしに全ranks/通常skew下降。`nozz:lem:one-heavy-gs` が二つの商に適用できる。nozzを一般対象へ黙って追加しない。

- `knd:lem:dual-quotient-support` と `knd:thm:koszul-ore`：一般wordKoszul Qn_domは任意nで全r3=r4=n,r5=1、B Koszul ASn、全indexedOre、standardH、L=n+5。H/noetherian/nozz/period1/ranksの追加仮定なし。Edualでζnormal、E/(ζ)=Fbar+Fbarηのexcessは0,2。D>=3からF→Fζ単射、r3n。ηζ0の補元はexcessD−2で、D≠4なら即消える。D4もF^(d−2)とE²_e4=R6*=0の対合によりF^(d−2)=0、商の(d−1,2)成分0となって矛盾。全Koszul枝が解決済みで、6倍数等の例外は残さない。`knd:cor:even-descent`：偶数nはnormalz2periodと奇数ASperiodからA1period/ordinaryOre下降。奇数n全下降は主張しない。
- notes `note:n4-three-class-boundary`：N9/L12のr5飽和剰余類が1/2/3個の各枝について平均r4と三次可解式を証明。2class枝の式は明示したγ≠0に依存し、all3ではγ0γ1γ2=0のみ。N9自体の排除ではない。正核だけで全γ0を強制できない形式3×3例も保持する。

## 保持する n=2 と graded の成果

- 従来のn=2対象Qは整域性を課さない。Q=H=Sを証明済みで、全Qに語長Koszul性、AS添字7、7周期性、標準関係数(1,2,2,1)、標準Hilbert級数がある。主論文 `idx:thm:mixed-relation-ranks`, `idx:cor:all-standard`。これを全nの結論に広げない。
- r_2=r_5=1の強制は解析的証明。r_3=r_4=2の強制は解析的な必要条件と890候補の厳密整数排除による計算補助証明。`computations/verify_mixed_ranks.py` と `computations/mixed_ranks_certificate.json` を保持する。低次数Hilbert一致からAS正則性を認定したのではない。
- n=2のZ-domain部分では、Hilbert/noetherian/周期を追加仮定せず、1周期性と量子平面またはJordan平面上の二段Ore表示、noetherian性を導く。主論文 `idx:thm:domain-standard` から `idx:thm:domain-ore`。全nの下降は反例により偽である。
- n=2の全Qについて、domain性は選んだ表示のz_0,...,z_6の全次数での左右正則性と同値。`idx:prop:z-regular-criterion`。今回domain性は許されているため、その自動性を主課題の前提にしない。有限添字の判定を有限次数の検査と混同しない。
- 既存の整域Oreデータの裸のindexed同型存在は、`idx:thm:finite-isomorphism` の有限行列条件で必要十分に判定する。入力が正しいOreデータであることが前提で、全indexed対象の1周期化、AS正則性の有限検査、全非線型自己同型群の記述ではない。
- 正規化対角三係数の完全同型は一致または(a^-1,b^-1,c*a^3/b^2)による一致。固定点a=1,b=+/-1。`diag:thm:indexed-isomorphism`, `diag:cor:quotient`。対角族の有限商は次元3であり、全ASモジュライの成分や次元ではない。
- 任意nの既存graded網羅定理 `thm:general-quadratic-classification` は、domain、左右noetherian、指定Hilbert級数、AS次元n+2、語長二次という明示した仮定の下で有効。その定理の仮定を新しいindexed主問題へ黙って加えない。語長二次を外すn>=3のgraded問題は副次課題。
- n=2の全対象は固定階数98次元の七窓表示へ帰着するが、AS locus・軌道幾何・全分類は未完成。最小周期7や非定数rhoなら零因子を持つという結論はn=2のQに限定される。n=1の非定数rhoを持つ整域反例と矛盾しない。
- 元のn=2全分類の成果・未解決問題は副課題として保持する。加重射影空間の可換基準ではスタックを用い、coarse Projと同一視しない。

- `genidx:lem:r5-gs-saturation`：語長保存L周期を持つ正連結局所有限二次Z-domainと多項式行増大だけで、3∤Lなら全r5=1、3|Lなら少なくとも一つのmod3class上で全r5=1。AS/Koszul/有限大域次元/noetherian不要。P2=I−S³+ε(−S²+R5S⁵)+O(ε²)とPH>=I、軌道平均の負固有値/正左ベクトル補正で証明。n4で3∤Lと仮定した全q_i=1は、三整除性定理の背理法で使用済みである。3|Lの残る二classやr3=nは未解決。

- notes `note:nonkoszul-existence`：Qn_dom内の非Koszul実例は未構成、今回確認した一次文献にも未発見。n4のN9,12,…は未排除候補であって存在族ではない。既知のHeisenberg U(h2)は四生成元・二次・AS5・非Koszulの整域（FV arXiv0911.5129v3 Thm2.1, Remark3.2）。本対象のgeneratorcount=ASdimから外れる。一般U(g)でもASdim−minimalgen=dim[g,g]であり非可換包絡例は同数条件を満たさない。中心cを追加のprimitive generatorと数えたり、C!のみに全ExtのFrobenius性を適用したりしない。既知例と初等的な適用範囲確認であり新規例ではない。

## 継続の優先順位

1. n>=4の非Koszul対象で全始点r3=n,r5=1を元の仮定から導くことを主目標とする。一般indexed語長Koszul枝は任意nで解決済みなので再開しない。`igraph:thm:normal-z-ore` により、これだけでB-ASと全Oreが従う。Koszul性・標準Hの自動性を先に証明する必要はない。r3の欠損n−r3、r5の零位置を、親AS対合・混合Euler・R5欠損成長から排除する。n4ではこの課題が十条件の自動性と同値である。
2. n4ではD3と3|N,3|Lを無条件に証明済み。非Koszul枝はN=9,12,15,…に限られる。最初にN9/L12/s7の重み3境界の三次元核を法3剰余類へ分解し、有効3×3行列を作る。少なくとも一つのr5飽和剰余類、pure tailのsum_j p_ij>=2q_i、r2_i>=3+q_i、中央E3対合とmixed momentを組み合わせる。N7の十周期純形式モデルのAS整域への全延長は排除済みで、20整数探索へ戻らない。全次数の純形式証明と個別mixed pencil計算は方法障害として保持する。
3. n3の全同型軌道を調べる。A1periodと通常graded二段Ore下降は全対象で証明済み。基礎AS3代数の自己同型、E=span ell_iと移動T、周期構造変更によるZhang twistを含めて同型判定を整理する。n1反例を独立light変数で拡張する際は三重重なりの係数制約を検証する。
4. 一般条件付き定理ではL_B偶数ならA1period、Koszul baseかつn偶数はその場合。n>=4の前提自動性は未証明。通常wordKoszul全nの二段Oreへnoetherianを再導入しない。任意nのAS基礎代数のnoetherian性は未主張。ordinary三生成元の既知分類と2period認識定理の重複調査を進め、新規性確定と数学的証明を区別する。
5. 副課題としてn2の整域Ore軌道幾何、domain自動性、混合射影退化、最小周期7の零因子例を保持する。逆向き片側R5関係の位置差2、3、4（法7）は `note:r5-orientation` で排除済み。rho=0全体を対角族、rho=1全体を初期Ore族と同一視しない。

## 自律研究と保存

- 研究依頼では具体的な証明、反例、厳密計算を進め、計画更新だけで終わらない。
- 一つの局所問題で止まったら本質的障害をノートへ残し、分類全体への寄与が高い別の課題へ移る。
- 約15分を目安に切りのよいところでmainへ直接保存する。時間切れが近いときは早めに保存する。
- 保存前に変更範囲の検証と `git diff --check`。遠隔先端をfetchして他者の更新を保護する。
- 明示したソースだけをstageし、通常のfast-forward pushを行い、遠隔SHAを照合する。
- **PR、force push、GitHub Actionsは禁止。** 空コミット、認証情報、PDF、ZIP、コンパイル中間物、旧版をGitに入れない。
- 保存は研究完了ではない。継続依頼の実行枠内では次の具体的課題へ進む。無期限実行や自動再起動は約束しない。
- GitHub mainがソース正本。Git管理物をLibraryへ重複保存しない。独立した非追跡の配布成果は利用可能な保存先へ常設許可の範囲で保存する。
- 保存失敗を成功と記録しない。Library上の既存ファイルを無断で削除しない。

## 原稿と主張

- 日本語LuaLaTeX、著者欄は空欄。現在有効な成果を論理的な順序で統合する。
- 証明済み・追加仮定付き・未証明・予想・計算観察を区別する。
- 証明の記載、複数AIエージェントによる独立監査、厳密計算、形式化、第三者査読、新規性確認を別状態とする。AIによる独立監査を査読や新規性確認と同一視しない。
- 既知の構成法や基準族を新発見としない。一次資料の定理番号と適用範囲を確認する。
- 有限次数のHilbert一致や有限双対のFrobenius性だけから一般Koszul性を認定しない。
- 表示パラメータ数98と基底変更群次元42からモジュライ次元56を結論しない。
- 誤りを直したら本文・要約・方針・直接依存を更新し、古い誤記の履歴を蓄積しない。
- 価値ある証明を軽量化のために削らない。ノートは作業日誌にせず、本文との証明重複を避ける。

## 再開と外部依存

- 起動時は方針とSTATEを読み、現在の命題と直接依存だけを取得する。
- nc-p3は方法上の比較先。巨大な全体・全履歴・私的原稿を毎回clone・転載しない。
- nc-p3の通常次数1の四窓を、重み付き七窓へ数字だけ置換しない。各jumpの始点・終点と語長を追う。
- 本リポジトリの現行ソースだけで初期定理の証明と計算を再現できるようにする。
- 新しい空台帳や分類表は必要になるまで増やさない。達成済み・未解決・次の一手を現行情報として書き換える。
