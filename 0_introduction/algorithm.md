# アルゴリズムとは何か

よく、プログラミングでは、アルゴリズムという言葉を耳に
すると思います。普通科ではなく情報科の学科に進む高校や
高専の方も、アルゴリズムが科目の一つとして入っており
ますが、  
  
アルゴリズムとは、一言で、  
**ある問題解決のための手続き**  であり、  
**数学の一つの形**  です。

はて、なるほど。といった感じだと思いますが、例えば、
こんな感じです。  

- 1,3,5,4,2 と、煩雑に並んだ数列を 1,2,3,4,5 と
キレイな昇順に並べ替える。(バブルソート, クイックソート, マージソート, ラディックスソート等々)
- ある2つの正の整数の最大公約数を求める。(ユークリッドの互助法)
- 無量大数もの大きな数を素数であるかを判別する。(数体篩(ふるい)法等)
- ある出発地点から目的地までの数ある運転ルートの中でも
最短距離であるルートを計算する。(要はカーナビ, ダイクストラ法)
- ある歌声が収録された音声データについて、それを
短い時間ごとに区切り、ドレミファソラシドのどの高さの
音が最も特性が強いかを判別する。(要はカラオケ採点システム, クロマ定数Q変換アルゴリズム)

え、それって何の役に立つの？って話から、思ったより実用的な
ものまであるんだなってものまで、沢山あるかと思います。  
  
これらの共通点は、**1個の数式では計算できないこと**です。  
つまり、ある程度の**手順を追ったプロセスで計算する**のです。
また、その計算手順がアルゴリズムなのです。
これが、プログラミングで解決できることかつ、どれだけ数字が
多くて、手計算では到底間に合わないものでも、コンピュータ
なら、大抵の問題を一瞬で計算することができます。
(ちなみに、世の中には、スーパーコンピューターを持ってしても290億年かかってしまうような計算問題も存在してしまうのですが、それはまたどこかの機会にお話しします。)  
  
ちなみに、その中でも最古のアルゴリズムと呼ばれているのが、
ユークリッド互助法で、その名の通り、ユークリッドという
化け物みたいな数学者様が発見してくださいました。  
