# 第2章の振り返り

## サブルーチン
### 用語
#### サブルーチン
今までのプログラミング講義では、名付けて「手続き型プログラミング」というものを行っておりました。  
今度は、それが「関数型プログラミング」へとシフトします。  
この、関数と呼ばれるものは、厳密にはサブルーチンと名付けられています。関数はサブルーチンの一種です。  
サブルーチンとは、端的に言えば、あるプログラムの塊をブロックに内包したもの…と呼べば良いでしょうか。  
これに関しては、言葉で説明するより実際にプログラムを見て貰った方が早いと思います。  
そして、それを見ればすぐに分かることがあります。  
このサブルーチンは一体何のためにあるのかと言いますと、ある機能ごとにプログラムを分割するためにあります。  
例えば、車に関しても、エンジン、ホイール、ハンドル…と、果たす役割ごとに固められてますよね。そんな感じです。  
このように機能ごとにプログラムを分割すると、どんな場合にどのタイミングで決まったプログラムを呼び出すと
いった手順が非常にやりやすくなり、プログラムの見た目としてもスッキリします。
また、手続き型よりも大規模なものを作れるようになりますので、アプリ開発を始め、関数型は広く採用されています。　　
ちなみに、もう一つ「オブジェクト指向プログラミング」というものもやりますが、これは関数型プログラミングをさらに
進化させたもので、先程、関数型はアプリ開発等に広く採用されているとは言ってしまいましたが、すいません。
それはちょっと嘘で、本当はオブジェクト指向の方が広く採用されています。もっと大規模な開発となった時に向くからです。  
まぁ、手続き型, 関数型, オブジェクト指向は、端的に言えば、フシギダネ, フシギソウ, フシギバナみたいな感じです。  
オブジェクト指向プログラミングの演習では、実際にポケモンのバトルシステムの再現プログラムを開発しますから、
それを楽しみに待っていてください。

#### サブルーチンの種類



# 演習課題
1. if文、if文と続いた場合、質問は何回されるかを答えなさい。プログラムを書く必要はありません。
2. if文、else文と続いた場合、質問は何回されるかを答えなさい。プログラムを書く必要はありません。
3. if文、elif文、else文と続いた場合、質問は何回されるかを答えなさい。プログラムを書く必要はありません。
(答えは2つあります。この場合なら何回、この場合なら何回という風に答えを用意してください。)
4. 2人でジャンケンをしなさい。
    1. import random で、ランダム機能を導入しなさい。
    2. 2人の変数を、それぞれa,bとします。a,bに当てはまる値は、1,2,3のいずれかがランダムで入ってきた値です。1をグー、2をチョキ、3をパーとして、2人の出した手をコンソール出力しなさい。
    3. ジャンケンの勝ち負けを判別する分岐処理を作成し、勝ち負けorあいこを出力しなさい。誰が勝って誰が負けたかも明記する必要があります。
5. あなたがジャンケンに参加しなさい。つまり、変数aはあなたで、変数bはCPUです(両方ともあなたは禁則とします)。コンソール入力にて、1,2,3のどれかの値を入力すれば良いです。また、それ以外の値を入力した場合は、ジャンケンに参加させないようプログラムを組みなさい。
6. ジャンケンの人数を3人に増やしなさい。3人の変数は、それぞれa,b,cとします。ジャンケンにはあなたが参加しても構いません。ただし、そうする場合は、3人のうち1人以上をCPUにしなさい。