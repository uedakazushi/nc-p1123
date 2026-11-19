# nc-p1123 — 重み (1^n,2,3) のAS正則代数

**2026-11-20 / 公表準備稿 v26。** 主論文は [papers/nc-p1123.tex](papers/nc-p1123.tex)。日本語 LuaLaTeX、著者欄は空欄。

研究を再開するときは [研究方針](research/plan_ja.tex) を最初に読む。本文外の有効な補題・例・障害は [研究ノート](research/notes_ja.tex)、七窓表示の詳細は [添字付き研究資料](research/indexed_z_algebra.tex) にある。

## 中心結果と適用範囲

一般対象 Q_n^dom は、正連結・局所有限、primitive jumps (1^n,2,3)、語長斉次二次、左右AS次元 n+2、有限生成射影による単純加群の有限解消、行・列の多項式増大、Z-domain性を要求する。Hilbert級数・Koszul性・noetherian性・1周期性は定義に含めない。

純jump 1部分を B、重み d の二次関係数を r_d(i) とする。任意 n で次は同値である。

1. 全始点で r_3(i)=n、r_5(i)=1。
2. B が有限生成の単純解消を持つ左右AS正則次元 n の代数である。
3. A がそのAS基礎 B 上の添字付き二段Ore拡張である。

証明は本文の igraph:thm:normal-z-ore と genidx:thm:as-base-ore。交換関係の存在だけでなく、PBW分解も結論に含む。A の語長Koszul性と B のKoszul性は同値となる。

| 対象・追加条件 | 主な到達点 | 本文の主要ラベル |
| --- | --- | --- |
| 任意 n、語長Koszul | 全混合階数、標準二変数Hilbert級数、添字付き二段Ore。偶数 n は1周期下降 | knd:thm:koszul-ore |
| n=1、追加条件なし | 全添字保持同型類と周期を決定。最小周期2の整域が存在 | genidx:thm:one-light-classification |
| n=2、追加条件なし | Koszul性、1周期下降、量子平面／Jordan平面上の二段Ore、左右noetherian性 | idx:thm:domain-ore |
| n=3、追加条件なし | 数値型からKoszul性を強制し、一般定理で基礎AS3・Oreを認識。最終代数の1周期下降、左右noetherian性 | genidx:thm:five-dimensional-numerics, genidx:thm:three-light-descent |
| n=4、追加条件なし | L−N=3、3がN,Lを割る。Koszul性・周期・基礎AS4性等の十条件が同値 | n4:thm:top-word-divisible-three, n4:thm:equivalent-criteria |

n=1 の正規形は zx=xz, wz=c zw, w_i x_(i+3)=x_i w_(i+1)+d_i z_i z_(i+2)、d_(2j)=c^(-j) alpha, d_(2j+1)=c^(-j) beta。裸の添字保持同型は c の一致と (alpha,beta) の共通非零スカラー倍で分類される。1周期性は alpha^2=c beta^2 と同値であり、零対を含む。他の対象の最小周期は2。この結果は「全対象が一つの通常graded代数から来る」という全次元の主張を否定するが、添字付きOre網羅性とは両立する。

n=2 では整域性を仮定しない広い対象 Q も扱い、標準関係数とHilbert級数を得る。混合関係数の強制には890個の整数列の厳密検査を用いる。整域部分には計算に依存しない数値強制の証明もある。

## 通常の次数付き対象で二段Oreを得る自然な条件

最小生成元次数 (1^n,2,3)、AS次元 n+2 の通常の連結局所有限AS正則代数について、次の判定を本文に証明した。左右noetherian性は必要な有限生成解消を保証する。

| 条件 | 結論と適用範囲 | 本文ラベル |
| --- | --- | --- |
| AS添字 n+5、整域、全最小生成元を語長1とする重みと両立した第二次数 | 語長Koszul性、基礎のKoszul AS_n性、標準二変数Hilbert、通常の二段Ore。語長二次性は結論 | prop:index-compatible-word-grading |
| I=A_+ に対する gr_I A が I次数でKoszulな整域 | 非二次補正を許す A=B[z;σ,δ₁][w;τ,δ₂]。AS添字 n+5と標準Hilbertも結論。gr_I Aの整域性は追加仮定 | thm:koszul-tangent-ore |
| n=2、AS添字7、整域・左右noetherian | 標準Hilbertと量子平面／Jordan平面上の二段Ore。二次性・第二次数・付随環条件は追加不要 | spec:cor:index-seven-ore |

z x₁−x₁ z=x₁³、他のx_jとzは可換、wは中心という族は、標準HilbertとAS添字 n+5を持つ非語長二次の二段Ore例である。この族の減少I進付随環は可換多項式環なので、第二の判定が適用できる。増加する語長filtrationとは区別する。

一般nでAS添字と基本仮定だけから二段Oreが従うかは未解決。上記は十分条件の証明であり、条件の自動性を主張するものではない。元の語長二次indexed問題と、通常gradedの非二次問題の仮定を混同しない。

## 論文の構成

要旨と序論では、中心定理、次数の規約、仮定と結論の一覧、先行研究との関係を説明する。本文は次の六部からなる。

| 部 | 内容 |
| --- | --- |
| I | 通常の次数付き代数の数値型、一般Oreデータ、次数付き同型、次数列だけでは決まらない例 |
| II | 添字付き対象、共通AS双対性と周期、正規元商、基礎AS性と混合階数の認識、一般Koszul構造 |
| III | n=1,2,3 の分類・数値型・周期と通常graded下降 |
| IV | 裸の添字保持同型の有限判定、対角表示空間と全特殊値を含む対角族の同型 |
| V | 語長二次性を仮定しない四次元の通常graded分類 |
| VI | 多項式増大、Euler行列式の因子、六次元対象の数値拘束、未解決問題 |

第I部の比較クラス G_n は noetherian性と指定一変数Hilbert級数を仮定する。一方、AS添字・付随環の判定は各声明の独立した仮定からHilbert級数を導く。第V部はこの通常graded設定の n=2 について語長二次性を外す。一般indexed対象の仮定と混同しない。

共通AS補題は genidx:lem:as-translation。全Extを一次生成と仮定せず、完全対合・AS平行移動・最高語長の一定性・二次表示からの周期復元を証明する。周期Hilbert行列の共通極と一次モーメントは hilbert:lem:common-pole にまとめる。n=3 の主依存は数値型から一般Koszul定理へ進む。親代数を要しない二周期三生成元認識定理も独立結果として保持し、定理文と証明を一続きに配置する。直接の混合階数証明は研究ノート note:n3-direct-mixed-ranks に収める。

## 未解決問題と主張の確実性

- n>=4 の非Koszul対象で二つの階数条件が自動かは未解決。n=4 の最初の未決着は N=9,L=12。N=9,12,15,... は未排除候補であり、存在族ではない。
- 全ての語長Koszul対象の添字付き構造は任意 n で証明を収めている。偶数 n と n=3 の下降を、全奇数 n へ拡張してはいない。
- n=2 非整域部分、一般Oreデータの軌道の幾何、n=3 の全同型軌道は未分類。同型の存在判定とモジュライ全体の構成を区別する。
- Euler行列式の因子分解は、Hilbert行列やPBW分解を自動的に与えない。
- 原稿中の証明、今回の内部点検、厳密計算、形式化、第三者査読、新規性の最終確認は別状態である。後三者の完了は主張しない。

詳細な証明位置と次の具体的な着手方法は [STATE](research/STATE.json)、一次文献と確認箇所は [BASELINE](research/BASELINE.md)、実際の検証範囲は [validation](research/validation.json) を参照する。

## 組版と再現

LuaLaTeX、LuaTeX-ja（ltjsarticle、luatexja-preset）、原ノ味フォント、標準の数学・組版パッケージを用意する。.latexmkrc の既定対象は主論文で、PDFとSyncTeXはリポジトリのルートに生成する。VS Code の LaTeX Workshop 設定も同梱する。

```bash
latexmk
latexmk research/plan_ja.tex research/notes_ja.tex research/indexed_z_algebra.tex
python3 scripts/check_project.py
python3 computations/verify_mixed_ranks.py
python3 computations/weighted_baseline.py
python3 computations/verify_n4_pure_euler.py
python3 computations/verify_n4_parent_mixed.py
python3 -m pip install -r requirements-symbolic.txt
python3 computations/verify_skew_ore.py
python3 computations/verify_euler_identities.py
```

check_project.py はファイル・ラベル・引用・主張参照の検査であり、数学的証明や組版の代用ではない。計算の役割と入力は [computations/README.md](computations/README.md) に記載する。

## 保存と配布

編集可能なソースの正本は GitHub main。PDF、ZIP、ログ、キャッシュ、旧版はGitで追跡せず、GitHub Actionsは使わない。Libraryへの定常的な二重保存やZIP作成は行わない。push不能時の緊急保存または別途指示がある場合に、現行ソースと主要PDFを含む一式を保存する。研究の区切りでは、本repoのmainへの反映を確認してから[research-hub](https://github.com/uedakazushi/research-hub)の該当項目を更新する。

緊急保存または明示的に配布一式が必要な場合には、検証済みソースをコミットし、主論文・方針・ノートを組版した後、次で現行版だけのZIPを作成できる。

```bash
python3 scripts/build_bundle.py
```

このスクリプトはZIP内のCRCと各ファイルのバイト一致を検査する。生成、組版、遠隔保存は別々に確認する。
