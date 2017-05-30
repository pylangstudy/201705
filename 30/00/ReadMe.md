# [4.7.3. 任意引数リスト](https://docs.python.jp/3/tutorial/controlflow.html#arbitrary-argument-lists)

< [4.7. 関数定義についてもう少し](https://docs.python.jp/3/tutorial/controlflow.html#more-on-defining-functions) < [4. その他の制御フローツール](https://docs.python.jp/3/tutorial/controlflow.html#more-control-flow-tools) < [Python チュートリアル](https://docs.python.jp/3/tutorial/index.html) < [ドキュメント](https://docs.python.jp/3/index.html)

## 用語の整理

引数の種類。呼び名が統一されていない。または文脈ごとに使い分けられている。

* 必須引数、位置指定引数、(ふつうの)引数
* キーワード引数、オプション引数、名前付き引数、デフォルト値を指定した引数
* 任意引数リスト、可変長引数、アンパック引数リスト
    * list型, tuple型 `*args`
* 任意引数辞書、キーワード可変長引数、アンパック引数辞書
    * dict型 `**kwargs`

## 任意引数リスト

### 優先度低

> 最も使うことの少ない

おそらく任意引数リストのtuple型は最も使用頻度が少ないと思われる。ただ、ライブラリなどでは`def func(*args, **kwargs):`の形は割とよく見かけると思う。

### 任意引数リストとは

> 関数が任意の個数の引数で呼び出せるよう指定する方法

> 引数はタプル ([タプルとシーケンス](https://docs.python.jp/3/tutorial/datastructures.html#tut-tuples) を参照) に格納されます。

```python
def MyFunc(*args):
    for arg in args:
        print(arg)

MyFunc(1, 2, 3, 'abc', 'def')
```
```sh
$ python3 0.py
1
2
3
abc
def
```

### 必須引数との位置関係

> 可変個の引数の前に、ゼロ個かそれ以上の引数があっても構いません。

> 可変 引数は、関数に渡される入力引数の残りを全て掬い取るために、仮引数リストの最後に置かれます。

```python
def MyFunc(title, *args):
    print('***** ' + title + ' *****')
    for arg in args:
        print(arg)

MyFunc('可変引数は必須引数より前に置くこと。', 1, 'abc')
```
```sh
$ python3 1.py
***** 可変引数は必須引数より前に置くこと。 *****
1
abc
```

### アンパック

listやtupleの前に`*`を付与することで可変引数リストとしてlistデータを渡せる。

2.py
```
def MyFunc(title, *args):
    print('***** ' + title + ' *****')
    for arg in args:
        print(arg)
    
#任意引数リストの1つ目に1, 2つ目に'abc'が渡される 
MyFunc('可変引数は必須引数より前に置くこと。1', 1, 'abc') 
MyFunc('可変引数は必須引数より前に置くこと。2', *(1, 'abc'))
MyFunc('可変引数は必須引数より前に置くこと。3', *[1, 'abc'])
a = (1, 'abc')
MyFunc('可変引数は必須引数より前に置くこと。4', *a)
a = [1, 'abc']
MyFunc('可変引数は必須引数より前に置くこと。5', *a)

# 任意引数リストの1つ目に配列として渡されてしまう
MyFunc('可変引数は必須引数より前に置くこと。6', [1, 'abc'])
```
```sh
$ python3 2.py
***** 可変引数は必須引数より前に置くこと。1 *****
1
abc
***** 可変引数は必須引数より前に置くこと。2 *****
1
abc
***** 可変引数は必須引数より前に置くこと。3 *****
1
abc
***** 可変引数は必須引数より前に置くこと。4 *****
1
abc
***** 可変引数は必須引数より前に置くこと。5 *****
1
abc
***** 可変引数は必須引数より前に置くこと。6 *****
[1, 'abc']
```

### 位置指定引数は任意引数リストの前に配置すること

> *args 引数の後にある仮引数は ‘キーワード専用’ 引数で、位置指定引数ではなくキーワード引数としてのみ使えます。

3.py
```python
def MyFunc(*args, title):
    print('***** ' + title + ' *****')
    for arg in args:
        print(arg)

MyFunc(1, 'abc', '可変引数は必須引数より前に置くこと。')
```
```sh
$ python3 3.py
TypeError: MyFunc() missing 1 required keyword-only argument: 'title'
```

位置指定引数のつもりで任意引数リストの後ろに`title`を用意した。しかし、任意引数リストの一つとして解釈されてしまう。

#### アンパックしてもダメ

4.py
```python
def MyFunc(*args, title):
    print('***** ' + title + ' *****')
    for arg in args:
        print(arg)

MyFunc(*[1, 'abc'], '可変引数は必須引数より前に置くこと。')
```
```sh
$ python3 4.py
SyntaxError: only named arguments may follow *expression
```

名前付き引数(named arguments)だけが後続にできるらしい。名前付き引数とは`arg=100`のようなデフォルト値を指定した形式の引数を言っているのだろう。任意引数リストの後ろに置けるのはキーワード引数だけと？（いや、任意引数リストの後ろには、任意引数辞書も配置できるはず。読み取れない）

#### キーワードを指定して呼びだせば任意引数リストの後ろでもOK

5.py
```python
def MyFunc(*args, option='オプション引数値です。'):
    print('----- option={0}'.format(option))
    for arg in args:
        print(arg)

MyFunc(*[1, 'abc'])
MyFunc(*[1, 'abc'], option='abc')
#MyFunc(*[1, 'abc'], 'abc') # SyntaxError: only named arguments may follow *expression
```
```sh
$ python3 5.py
----- option=オプション引数値です。
1
abc
----- option=abc
1
abc
```

キーワード指定せずにオプション引数を呼びだそうとするとエラーになる。

#### キーワード引数を前にするとキーワード指定呼出がエラーになる

キーワード引数を前にすると、今度はキーワード指定した方法で呼出たときにエラーになる。

```python
def MyFunc(option='オプション引数値です。', *args):
    print('----- option={0}'.format(option))
    for arg in args:
        print(arg)

MyFunc(*[1, 'abc'])
#MyFunc(option='abc', *[1, 'abc']) # TypeError: MyFunc() got multiple values for argument 'option'
MyFunc('abc', *[1, 'abc'])
```
```sh
$ python3 6.py
----- option=1
abc
----- option=abc
1
abc
```

エラーの意味がよくわからない。
```
MyFunc() got multiple values for argument 'option'
```

* `MyFunc（）に引数 'option'の値が複数ある`

`option`という名前の引数は1つしか無いはず。システムで予約されているのかと思い`aaa`という名前に変えてみても同じエラーだった。謎。

#### 任意引数リストを使うとき、キーワード引数は使えない

キーワード引数と任意引数リストを使うと`TypeError`が発生しうるから。

そういうものなのか、回避方法があるのかは不明。ただ、キーワード引数のみ`def func(opt=0)`か、任意引数リストのみ`def func(*args):`のどちらかにしておいたほうが無難か。

## 任意引数辞書 `**kwargs`

リストやタプルだけでなく、辞書も引数に渡せる。

```python
def MyFunc(**kwargs):
    print('----- MyFunc -----')
    for key, value in kwargs.items():
        print(key, value)

MyFunc(**{'key1': 'value1', 'key2': 'value2'})
d = {'key1': 'value1', 'key2': 'value2'}
MyFunc(**d)
```
```sh
$ python3 7.py
----- MyFunc -----
key1 value1
key2 value2
----- MyFunc -----
key1 value1
key2 value2
```

## 引数＋引数リスト＋引数辞書

```python
def MyFunc(req, *args, **kwargs):
    print('----- MyFunc -----')
    print('req={0}'.format(req))
    print('*args')
    for arg in args:
        print(arg)
    print('**kwargs')
    for key, value in kwargs.items():
        print(key, value)

MyFunc('必須引数値', *[1, 'abc'], **{'key1': 'value1', 'key2': 'value2'})
a = [1, 'abc']
d = {'key1': 'value1', 'key2': 'value2'}
MyFunc('必須引数値', *a, **d)
```
```sh
$ python3 8.py
----- MyFunc -----
req=必須引数値
*args
1
abc
**kwargs
key1 value1
key2 value2
----- MyFunc -----
req=必須引数値
*args
1
abc
**kwargs
key1 value1
key2 value2
```

