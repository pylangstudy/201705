# [4.6. 関数を定義する](https://docs.python.jp/3/tutorial/controlflow.html#defining-functions)

< [4. その他の制御フローツール](https://docs.python.jp/3/tutorial/controlflow.html#more-control-flow-tools) < [Python チュートリアル](https://docs.python.jp/3/tutorial/index.html) < [ドキュメント](https://docs.python.jp/3/index.html)

## `def`

> def は関数の 定義 (definition) を導くキーワードです。 

> def の後には、関数名と仮引数を丸括弧で囲んだリストを続けなければなりません。

> 関数の実体を構成する実行文は次の行から始め、インデントされていなければなりません。

0.py
```python
def AddOne(value):
    return value + 1
print(AddOne(7))
```
```sh
$ python3 0.py
8
```
1〜2行目で関数を定義している。3行目でその関数を呼び出している。戻り値を`print`文で表示する。

## スコープ

## ドキュメンテーション文字列(docstring)

> 関数の本体の記述する文の最初の行は文字列リテラルにすることもできます。その場合、この文字列は関数のドキュメンテーション文字列 (documentation string)、または docstring と呼ばれます。

> (docstring については [ドキュメンテーション文字列)](https://docs.python.jp/3/tutorial/controlflow.html#documentation-strings) でさらに扱っています。

```python
def AddOne(value):
    """
    引数で渡された値に1を加えた値を返す.
    
    日本語などASCII文字でない文字は使うべきではないらしいが。
    """
    return value + 1
print(AddOne(7))
```

> 自分が書くコードにドキュメンテーション文字列を入れるのはよい習慣です。書く癖をつけてください。

ただし英語で。また、コメントが良い習慣とは言い切れない。コメント不要でもすぐに分かるような名前をつけたり、わかりやすい構造になるよう設計することこそ、最良という意見もある。

## 関数内シンボルテーブル

> 関数を 実行 (execution) するとき、関数のローカル変数のために使われる新たなシンボルテーブル (symbol table) が用意されます。
> 関数内で変数への代入を行うと、その値はすべてこのローカルなシンボルテーブルに記憶されます。

> ある関数がほかの関数を呼び出すときには、新たな呼び出しのためにローカルなシンボルテーブルが新たに作成されます。

### 検索の優先順位

> 変数の参照を行うと、まずローカルなシンボルテーブルが検索され、次にさらに外側の関数のローカルなシンボルテーブルを検索し、その後グローバルなシンボルテーブルを調べ、最後に組み込みの名前テーブルを調べます。

「変数のスコープ」の話か。

## 関数内ではグローバル変数への代入ができない

> 関数の中では、グローバルな変数を参照することはできますが、直接値を代入することは (global 文で名前を挙げておかない限り)できません。

## 実引数と仮引数

* 関数を呼び出した側でメモリ確保した引数を実引数という
* 呼び出された関数側でモリ確保した引数を仮引数という

引数がポインタ変数か否かで影響範囲が変わる。ポインタ変数なら参照渡しという。そうでないなら値渡しという。もし参照渡しなら、関数内で引数に代入したとき、呼び出し側で参照する引数も代入されたものを参照する。もし値渡しなら関数内で引数を変更しても、呼び出し側の引数は変更されない。

### C言語における関数の引数は値渡しである

http://www.cc.kyoto-su.ac.jp/~yamada/ap/parameter_argument.html

ポインタ変数を使えば参照できるので参照渡しにもできる。

### Pythonにおける関数の引数は参照渡しである

参照渡しである。たったそれだけのことを、ドキュメント本文ではものすごくわかりづらく書いている。

> 関数を呼び出す際の実際の引数 (実引数) は、関数が呼び出されるときに関数のローカルなシンボルテーブル内に取り込まれます。そうすることで、引数は 値渡し (call by value) で関数に渡されることになります (ここでの 値 (value) とは常にオブジェクトへの 参照(reference) をいい、オブジェクトの値そのものではありません) [1]

> [1] 実際には、オブジェクトへの参照渡し (call by object reference) と書けばよいのかもしれません。というのは、変更可能なオブジェクトが渡されると、関数の呼び出し側は、呼び出された側の関数がオブジェクトに行ったどんな変更 (例えばリストに挿入された要素) にも出くわすことになるからです。

たぶんPythonはポインタ変数をコピーして値渡ししているのだろう。Pythonでは仕組み上、参照渡ししかできないのだと思う。C言語のようにポインタ引数にするか否かで値渡しか参照渡しかを使い分ける必要がないのだろう。

## 関数オブジェクト

> 関数の定義を行うと、関数名は現在のシンボルテーブル内に取り入れられます。関数名の値は、インタプリタからはユーザ定義関数 (user-defined function) として認識される型を持ちます。この値は別の名前に代入して、後にその名前を関数として使うこともできます。これは一般的な名前変更のメカニズムとして働きます:

2.py
```python
def AddOne(value):
    return value + 1
AO = AddOne
print(AO(7))
```
```sh
$ python3 2.py
8
```

たぶんC言語でいう関数ポインタか。リテラルを変数に代入するのと同じように扱っている。

## 関数はデフォルトでNoneを返す

> return 文を持たない関数もややつまらない値ですが値を返しています。この値は None と呼ばれます

> None だけを書き出そうとすると、インタプリタは通常出力を抑制します。本当に出力したいのなら、以下のように print() を使うと見ることができます:

```python
def MyFunc():
    pass
print(MyFunc())
```
```sh
$ python 3.py
None
```

### 引数

`def 関数名(引数1, 引数2, 引数3, ...):`という書式で定義する。

### 戻り値

`return`文で処理を終了する。値があれば返す。

* `return`
* `return 何かの値`

> return 文では、関数から一つ値を返します。 return の引数となる式がない場合、 None が返ります。関数が終了したときにも None が返ります。

## メソッド

関数ではなくメソッド。

> メソッドとは、オブジェクトに ‘属している’ 関数のこと

### `object.method`

> obj を何らかのオブジェクト (式であっても構いません)、 methodname をそのオブジェクトで定義されているメソッド名とすると、 obj.methodname と書き表されます。

### 名前空間

> 異なる型は異なるメソッドを定義しています。異なる型のメソッドで同じ名前のメソッドを持つことができ、あいまいさを生じることはありません。

### クラスによるメソッド定義

> クラス (class) を使うことで、自前のオブジェクト型とメソッドを定義することもできます。[クラス](https://docs.python.jp/3/tutorial/classes.html#tut-classes) 参照

以下のようにして自前のオブジェクト型とメソッドを定義する。

4.py
```python
class MyClass:
    def MyFunc(self):
        print('MyClass.MyFunc()')

c = MyClass()
c.MyFunc()
```
```sh
$ python 4.py
MyClass.MyFunc()
```

