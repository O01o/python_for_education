# 画像処理

皆さんは、普段からテレビやPCにiPhone等といったデジタル機器から、
週間雑誌や教科書の表紙といった印刷物など、
広く言えば、「グラフィック」という概念によく触れているかと思われます。  
この画像処理では、そのグラフィックを数値的に処理し、

## 画像の仕組み

### とりあえず勉強すべきこと
- 光の三原色の概念
- ピクセルの概念
- 階調の概念
- 色の定義の仕方(RGB, CMY, HSV)
- 規格の概念
- ファイルI/Oの概念
- 多重往復処理の概念
- 中学・高校の数学, 物理

[コンピュータにおける三原色について](http://yokoyamatakashi.com/archives/1306)  
[グラフィックにおけるピクセルの概念](https://e-words.jp/w/%E3%83%94%E3%82%AF%E3%82%BB%E3%83%AB.html)

基本的には、上記の概念さえ知っておけば十分です。  
要は、ピクセルは「格子状にRGBが配列されたもの」と覚えておけば結構です。  
なお、それぞれのピクセルには、「R・G・B」という3つのパラメータが入っているのですが、これは**0~255**の範囲で
値を指定することができます。0は当然ながら色無し、255は当然色有りになります。
RGBが全部0,0,0でできている場合、黒になります。逆に、255,255,255と指定した場合、白になります。

## 画像処理でできること

- 画像の読み込み
- ピクセルへのアクセス(ピクセルに直接書き込み, ネガポジ反転, RGBスワップ等)
- グレースケール化
- 二値化(またはそのヒストグラム)
- ラプラシアンフィルタ, キャニーフィルタ
- 輪郭の抽出
- オブジェクトの抽出
- 直線, 円の検出
- 直線の描画
- 円の描画
- 3Dメッシュの描画
- 幾何学模様の生成
