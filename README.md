# nc-p1123 — 非可換重み付き射影空間 P(1,1,2,3) の分類

**2026-11-18 / v4。完全分類は未完成。正本は GitHub main。**

[研究方針](research/plan_ja.tex) → [主論文](nc-p1123.tex) → [研究ノート](research/notes_ja.tex) の順に読む。
一般の次数列 `(1^n,2,3)` については [一般重みの構造定理と Ore 分類](papers/general_weights.tex) を参照する。
独立した原稿として [次数付き代数の Ore 分類](papers/graded_ore_classification.tex) と
[対角 Ore 表示空間の成分](papers/weighted_ore_strata.tex) を置く。
次の具体的課題と証明位置は [STATE](research/STATE.json)、一次文献の適用範囲は
[BASELINE](research/BASELINE.md)、実際の検証状態は [validation](research/validation.json)。
実行規則は [AGENTS.md](AGENTS.md)。

## 分類するもの

標数零の代数閉体上の正連結・局所有限 Z-代数について、最小生成元空間
`V = A_+ / A_+^2` の各始点での jump が **1,1,2,3** となり、
その生成元に関する**語長二次**の重み付き斉次関係を持つ四次元AS正則対象を、
**添字保持同型**で分類する。

「重み付き次数2の関係だけ」「Hilbert級数が同じ代数全て」「1周期的なgraded代数だけ」ではない。
可換基準は重み付き射影**スタック**である。

広いAS正則対象Qについて、語長Koszul性・AS添字7・7周期性は初期の構造定理として証明した。
所期のHilbert級数を持つ部分Hは標準型Sと一致するが、Q=Hは未証明である。
初期の標準型は、右単純加群の最小解消が次のシフトを持ち、左右のAS双対性を満たすものとする。

| ホモロジー次数 | 添字のシフト |
| --- | --- |
| 0 | 0 |
| 1 | 1, 1, 2, 3 |
| 2 | 2, 3, 3, 4, 4, 5 |
| 3 | 4, 5, 6, 6 |
| 4 | 7 |

語長に関して線型なこの解消から
`H(t)=1/((1-t)^2(1-t^2)(1-t^3))` が従う。
広い対象が全て標準型になることは未証明であり、分類の課題に残す。
domain・noetherian・PBW・Calabi–Yau性は全対象に仮定しない。

## 初期成果とその射程

**一般の次数列 `(1^n,2,3)`**：左右 noetherian、AS 次元 `n+2`、
Hilbert 級数 `1/((1-t)^n(1-t^2)(1-t^3))` を仮定した graded 代数について、
AS 添字 `n+5` と最小解消の内部次数 `i ≤ j ≤ i+3` を証明した。
語長二次なら、整域性を仮定せず語長 Koszul 性と関係数
`(binom(n,2),n,n,1)`（重み `2,3,4,5`）が従う。
さらに domain なら、任意の `n` について
`B[z;σ][w;τ,D]` が全対象を尽くし、`B=k<A_1>` は AS 正則次元 `n`、
`H_B(t)=(1-t)^(-n)` となる。必要十分条件は
`μσ=σμ`, `Lσ=cL`, `(μ⊗L+L⊗σ²)(R)=0`。
全 graded 同型と語長二次部分の同型存在判定も記述する。
証明は [general_weights.tex](papers/general_weights.tex)。

最小生成元次数だけを固定すると、同じ次数列で AS 次元が `n+m+2` となる
noetherian domain の族が存在し、大域次元は無界である。
一般 `n≥3` の任意の斉次関係について、語長二次性を除いた Ore 網羅性は未証明である。
基礎代数 `B` を一般の AS 正則代数から選ぶ必要も残る。
この一般化は graded 代数についての結果であり、上記の四次元 Z-代数の分類対象は変更しない。

**次数付き代数の Ore 分類**：複素数体上の連結・局所有限・左右 noetherian な4次元AS正則代数で、
最小生成元次数が `(1,1,2,3)`、Hilbert級数が `1/((1-t)^2(1-t^2)(1-t^3))` であるものは、
量子平面または Jordan 平面からの段階的 Ore 拡大 `B[z;σ,δ][w;τ,D]` で尽くされる。
全ての許容データを有限の係数条件で記述し、全 graded 同型を三角形変換として与える。
語長二次表示を持つ部分では、非対角自己同型を許したチャートと graded 同型の存在判定も得る。
証明は [graded_ore_classification.tex](papers/graded_ore_classification.tex)。
この定理は上記の仮定付き graded 分類であり、一般の七窓や裸の添字保持同型の分類は課題に残る。

**対角 Ore 表示空間**：対角量子三生成元環からの全ての対角 skew Ore 二次拡大を分類した。Ore 条件は
`a(v-p)=a(u-q*r^2)=b(v-r)=b(p^2-q*s)=0` の4式で必要十分であり、
表示空間は次元 `6,5,5,4` の4既約成分の和となる（同型類モジュライの成分ではない）。
全ファイバーの PBW/Koszul/AS 正則性と重み4射影階数による非対角族の分離を証明。
詳細な証明は [公表用原稿](papers/weighted_ore_strata.tex)。
計算検証は `python3 computations/verify_skew_ore.py`（SymPy 1.14.0）。


主論文と上記の独立原稿に次の証明を収める。新規性・第三者査読・形式化の完了は主張しない。

| 内容 | 得られたこと | 残ること |
| --- | --- | --- |
| 一般 `(1^n,2,3)` の語長二次 graded 部分 | 左右 noetherian・domain・AS 次元 `n+2`・指定 Hilbert 級数の下で全 `n` の Ore 表示と同型軌道を記述 | 語長二次性・指定 Hilbert 級数・domain/noetherian 仮定の除去 |
| 最小生成元次数だけの指定 | 固定した次数列で大域次元が無界となり、標準部分代数の最初の Ore 段階も存在しない明示族 | 次元 `n+2` を固定した広い対象の分類 |
| 同型の線型化 | 語長斉次な二次表示同士の同型の存在は、最小生成元空間の線型写像と二次関係の対応で判定できる | 非線型自己同型を含むmoduli stackの記述 |
| 一般対象の構造 | AS双対性と多項式成長から語長Koszul性とAS添字7を導く。Hilbert条件Hと標準解消Sは同値 | 所期のHilbert級数が全Qで強制されるか |
| 一般対象の周期 | Koszul双対のFrobenius traceから7周期同型を構成。最小正周期は1または7 | 最小周期7の対象の存在または排除 |
| 有限表示 | 標準型は固定階数の七窓、一般Qは有限個の階数表にわたる七窓の和へ還元 | 候補のAS/Koszul条件、明示的な全被覆 |
| 仮定付き graded 分類 | 複素数体、noetherian、指定Hilbert級数の下で段階的Ore表示が網羅的。有限係数条件と全三角形graded同型を記述 | 一般Qへの拡張、裸のindexed同型による商 |
| 語長二次の graded 部分 | 上記の仮定の下で、非対角自己同型を許すOreチャートと線型な同型存在判定 | 1周期性等を仮定しない全対象の被覆 |
| 対角量子族 | 既知の正則族。6交換係数を対角Zhang twistで3パラメータに正規化 | 残るGL2作用を含めた全indexed同型 |
| 対角skew Oreチャート | 4式による必要十分条件、表示パラメータ空間の4成分、全ファイバーの正則性 | 全AS空間の被覆・成分同定・完全indexed同型 |
| 非対角Ore族 | `[t,x]=a z^2, [t,y]=b z^2` は全パラメータで標準型。族内は零・非零の2同型類 | 全非対角対象の被覆 |
| 最初の不変分岐 | 重み4関係の `zz` 成分への射影階数は同型不変。非零Ore族は全対角量子族と非同型 | 各階数パターン内の構造定理 |

各始点の関係の表示空間は
`Gr(1,4) × Gr(2,4) × Gr(2,5) × Gr(1,2)`、次元14。
七窓では表示空間次元98、線型生成元変更群次元42になる。
**これらの数はモジュライ次元を与えない。**

## 最初に進める課題

一般の次数列についての継続点は、まず `n=3`、AS 次元5、指定 Hilbert 級数の下で、
語長二次性を仮定しない最小関係と augmentation filtration を調べることである。
付随次数代数の AS 正則性・二次性は未証明なので仮定せず、
一般の斉次 Ore チャートに還元できる範囲を特定する。
大域次元が増える明示族を、次元 `n+2` を固定した場合への反例として用いない。

複素数体上の noetherian・指定Hilbert級数の graded 部分には、非対角の場合を含むOre表示が得られた。
次はその仮定の外の標準七窓（特に重み4射影階数の非定数パターン）と、裸のindexed同型の商を優先する。


1. 重み4の `zz` 射影階数と、重み2・3の関係の階数を組み合わせ、全標準七窓を覆う不変な分岐を作る。
2. 各枝で有限双対のFrobenius条件とKoszul複体の正確性を別々に扱う。
3. 対角族を3パラメータに正規化した後、同重み生成元2本の基底変更と例外値の同型を決める。
4. 最小周期7の可能性を調べる。7周期の存在だけから非1周期の例の存在を結論しない。

現行の具体的な着手方法は研究方針とSTATEに集約する。

## 再現

基礎計算は Python 3.10以降の標準ライブラリ、対角skew Oreの記号計算はSymPyを使う。

```bash
python3 computations/weighted_baseline.py
python3 scripts/check_project.py
python3 -m pip install -r requirements-symbolic.txt
python3 computations/verify_skew_ore.py
```

第1コマンドは重み24までのHilbert係数、二変数Euler恒等式、
二つの族の全三重重なり、対角twistの整数指数行列と正規化を厳密に検算し、
現行の `computations/baseline_certificate.json` と照合する。
証明書の再生成は `python3 computations/weighted_baseline.py --write`。
第2コマンドはファイル・参照・台帳の構造検査であり、数学的証明ではない。

LuaLaTeX、latexmk、LuaTeX-ja、日本語フォントHaranoAji、標準AMS・hyperref・booktabs・xurlパッケージを用いる。
TeX Liveの `texlive-luatex`、`texlive-lang-japanese`、`texlive-latex-recommended`、`texlive-latex-extra`
相当の構成を想定する。リポジトリルートから：

```bash
latexmk -lualatex nc-p1123.tex
latexmk -lualatex research/plan_ja.tex
latexmk -lualatex research/notes_ja.tex
latexmk -lualatex papers/weighted_ore_strata.tex
latexmk -lualatex papers/graded_ore_classification.tex
latexmk -lualatex papers/general_weights.tex
```

PDFはルートに出力し、Synctexを有効にする。VS CodeのLaTeX Workshop設定を同梱。
PDF・ZIP・コンパイル中間物は追跡しない。

検証済みソースをcommitし、6本のPDFを再生成した後、現行一式を作る場合：

```bash
python3 scripts/build_bundle.py
```

`output/nc-p1123-2026-11-18-v4.zip` に現行ソースと6本のPDFだけをまとめ、
各ファイルのSHA-256とZIPの整合性を確認する。Git履歴・旧版・ログは含めない。
このコマンドは生成と検証を行うだけで、外部への保存を実行しない。

## nc-p3との関係

[nc-p3](https://github.com/uedakazushi/nc-p3) の「完全分類を上位目標に置く」「添字保持同型を基準にする」
「証明・計算・未解決を分ける」「約15分を目安にmainへ直接保存する」という設計を継承する。
通常次数1の4生成元・四窓をそのままコピーせず、最小生成元のjump、
二変数次数、ASシフト7の強制と重み付き基底変更を独立に定式化した。
本リポジトリの初期結果の証明に、nc-p3の私的原稿や計算資産の取得は不要。

これは研究継続用の現行一式であり、旧版や作業日誌を収録するアーカイブではない。
