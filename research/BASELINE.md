# 一次文献・外部依存の現行索引

2026-11-18 / v1。読んだ箇所と適用範囲を区別する。外部PDFは同梱しない。
指定対象の完全分類を与える文献は今回の初期調査では確認できなかった。
これは文献不存在や新規性の確定を意味しない。

## 直接使う文献

| 文献 | 確認した一次資料と箇所 | 本研究での使い方・限界 |
| --- | --- | --- |
| Auroux–Katzarkov–Orlov, *Mirror symmetry for weighted projective planes and their noncommutative deformations*, Ann. Math. 167 (2008), 867–943; DOI 10.4007/annals.2008.167.867; arXiv:math/0404281 | [出版版](https://annals.math.princeton.edu/wp-content/uploads/annals-v167-n3-p04.pdf), §2.2、Prop.2.3/Cor.2.4、Prop.2.6、Thm.2.12、Prop.2.18/Cor.2.19 | 任意重みの対角skew polynomial族。AS次元4、添字7と例外列7項は既知。qgrは可換基準でstackのcoh。非対角・非1周期の全分類ではない。 |
| Sierra, *G-algebras, twistings, and equivalences of graded categories*, Algebr. Represent. Theory 14 (2011), 377–390; DOI 10.1007/s10468-009-9193-y | [arXiv:math/0608791v3](https://arxiv.org/pdf/math/0608791), Thm.1.2 = Cor.4.4、§2 | degree1生成を要求せず、Zhang twistとassociated Z-algebra同型の対応。graded同型をそのままindexed同型に読み替えない。 |
| Van den Bergh, *Non-commutative quadrics*, IMRN 2011, no.17, 3983–4026; DOI 10.1093/imrn/rnq234 | [arXiv:0807.3753](https://arxiv.org/pdf/0807.3753), §3、Lemma3.4、§4.1 | Z-代数、1周期とgraded由来、AS正則の定義。三次元のquadric分類を本対象へ直接適用しない。 |
| Martínez-Villa–Solberg, *Artin–Schelter regular algebras and categories*, JPAA 215 (2011), 546–565; DOI 10.1016/j.jpaa.2010.06.006 | [arXiv:0902.1119](https://arxiv.org/pdf/0902.1119), §6、Thm.6.2 | AS双対性からFrobenius Ext圏。重み付きのHom–Tor議論と7移動は本文で書き直す。Thm.6.4のLoewy長の数え方に注意し、次元4は明示双対から直接導く。 |
| Liu–Wang–Wu, *Twisted Calabi–Yau property of Ore extensions*, JNCG 8 (2014), 587–609; DOI 10.4171/JNCG/165; arXiv:1205.0893 | [出版版](https://ems.press/content/serial-article-files/30578), Thm.3.3、Prop.4.1 | 自己同型によるOre拡大のtwisted CY性。今回のOre族では双対を直接計算し、重みと成長も確認する。一般的な構成法を新規性としない。 |
| Bergman, *The diamond lemma for ring theory*, Adv. Math. 29 (1978), 178–218; DOI 10.1016/0001-8708(78)90010-5 | [著者ページ](https://math.berkeley.edu/~gbergman/papers/updates/diamond.html), Thm.1.2, p.181 | 停止順序と全重なりの解消から順序単項式基底。今回取得した一次資料は著者の書誌・訂正ページであり、原論文全PDFは未取得。適用の四重なりは直接検算。 |
| Priddy, *Koszul resolutions*, Trans. AMS 152 (1970), 39–60 | [一次PDF](https://math.mit.edu/~hrm/palestine/priddy-koszul-resolutions.pdf), Thm.5.3, p.51 | PBW基底から語長Koszul性。重み次数について線型であるとの主張ではない。 |
| Lu–Palmieri–Wu–Zhang, *Koszul equivalences in A-infinity-algebras*, NYJM 14 (2008), 325–378 | [出版版](https://nyjm.albany.edu/j/2008/14-16.pdf), Corollary D, p.327; 証明§9.3, p.372 | connected graded AS-regular性とFrobenius Extの対応。Definition9.1は有限GK成長を含めないので、本文では成長をPBW基底から独立に示す。 |

## 混同を避ける比較先

- Lu–Palmieri–Wu–Zhang, *Regular algebras of dimension 4 and their A-infinity Ext-algebras*, Duke Math. J. 137 (2007), 537–584; DOI 10.1215/S0012-7094-07-13734-7; [arXiv:math/0411497](https://arxiv.org/pdf/math/0411497)。序論、§1の二生成型、式(HS)を確認。degree1二生成・関係次数3,4で、今回と同じHilbert級数でも最小生成元とBetti型が違う。genericity付き分類の射程を超えて使わない。
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

## 新規性と追加調査

対角族の正則性、一般的なZhang twist、Koszul–Frobenius、Ore手法は既知。
ここで証明した具体的な非対角族、二同型類、射影階数分岐と既知の重み付き/Ore族との
完全な同定は未了であり、新規定理としての独立性は未確認である。
一般四次元AS正則代数のgraded分類と、本研究のindexed分類の差を継続して調べる。
