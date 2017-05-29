# [4.3. range() 関数](https://docs.python.jp/3/tutorial/controlflow.html#the-range-function)

< [4. その他の制御フローツール](https://docs.python.jp/3/tutorial/controlflow.html#more-control-flow-tools) < [Python チュートリアル](https://docs.python.jp/3/tutorial/index.html) < [ドキュメント](https://docs.python.jp/3/index.html)

## [range()](https://docs.python.jp/3/library/stdtypes.html#range)

> 数列にわたって反復を行う必要がある場合、組み込み関数 range() が便利です。この関数は算術型の数列を生成します

```python
>>> range(5)
range(0, 5)
>>> print(range(5))
range(0, 5)
```

### rangeはオブジェクトである

`[0,1,2,3,4]`となると思っていたが違うらしい。一体何者なのか。[range()](https://docs.python.jp/3/library/stdtypes.html#range)のリンク先をみるとclassのようだ。`list(range(5))`とすると`[0,1,2,3,4]`のようにリスト型に変換できるらしい。

```python
>>> list(range(5))
[0, 1, 2, 3, 4]
```

> range() が返すオブジェクトは、いろいろな点でリストであるかのように振る舞いますが、本当はリストではありません。これは、イテレートした時に望んだ数列の連続した要素を返すオブジェクトです。

### rangeはイテラブルである

> このようなオブジェクトは イテラブル (iterable) と呼ばれます。これらは関数やコンストラクタのターゲットとして、あるだけの項目を逐次与えるのに適しています。

> for 文がそのような イテレータ であることはすでに見てきました。
> 関数 list() もまた一つの例です。これはイテラブルからリストを生成します:

```python
>>> list(range(5))
[0, 1, 2, 3, 4]
```

つまり、以下のように表現すると言うことか？

* `range`はイテラブルなオブジェクトである
* `list()`はイテラブルなオブジェクトを引数にとる関数である

### for文と組み合わせる

```python
for i in range(5):
    print(i)
```

```sh
$ python3 0.py 
0
1
2
3
4
```

for文はlist型, tuple型, dict型, range型で使えるということか。

### 負数

```python
>>> list(range(-5, -2))
[-5, -4, -3]
>>> list(range(-2, 0))
[-2, -1]
>>> list(range(-2, 3))
[-2, -1, 0, 1, 2]
```

### `第一引数 < 第二引数`でないと空リストを返す

```python
>>> list(range(3, 3))
[]
>>> list(range(4, 3))
[]
>>> list(range(0, -4))
[]
```

### 開始と終了の指定

```python
>>> list(range(3,5))
[3, 4]
>>> 
>>> list(range(-2, 0))
[-2, -1]
>>> list(range(-2, 3))
[-2, -1, 0, 1, 2]
```

3から5までの間の整数でできた数列を作る。

### ステップの指定

```python
range(0, 100, 9)
>>> list(range(0, 100, 9))
[0, 9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99]
```

0から100までの間で9ずつ刻んだ整数でできた数列を作る。

## `range()`と`len()`と`for`文

1.py
```python
l = ['a', 'b', 'c']
for i in range(len(l)):
    print(i, l[i])
```
```sh
$ python3 1.py 
0 a
1 b
2 c
```

* `print('a', 'b')`のようにカンマ区切りで渡すと`a b`のようにスペース区切りで出力される

### 前回のprint文を改善

以下の[前回](https://github.com/pylangstudy/201705/tree/master/29/03#enumerate)コードとどちらがスマートか。

```python
for index, item in enumerate(['ab', 'cd', 'ef']):
    print("{0}: {1}".format(index, item))
```

合わせ技で以下がいい。

2.py
```python
for i, item in enumerate(['a', 'b', 'c']):
    print(i, item)
```
```sh
$ python3 2.py 
0 a
1 b
2 c
```

### 前回のdictループを改善

[前回](https://github.com/pylangstudy/201705/tree/master/29/03#dict%E5%9E%8B)コード。

```python
d = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
for key in d.keys():
    print("{0}: {1}".format(key, d[key]))
```

[ループのテクニック](https://docs.python.jp/3/tutorial/datastructures.html#looping-techniques)によると`dict.items()`という関数があるらしい。少しスマートにできる。

```python
d = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
for key, value in d.items():
    print(key, value)
```
```sh
$ python3 3.py 
key2 value2
key3 value3
key1 value1
```

