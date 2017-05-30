# [4.7.5. ラムダ式](https://docs.python.jp/3/tutorial/controlflow.html#lambda-expressions)

< [4.7. 関数定義についてもう少し](https://docs.python.jp/3/tutorial/controlflow.html#more-on-defining-functions) < [4. その他の制御フローツール](https://docs.python.jp/3/tutorial/controlflow.html#more-control-flow-tools) < [Python チュートリアル](https://docs.python.jp/3/tutorial/index.html) < [ドキュメント](https://docs.python.jp/3/index.html)

## lambda

> キーワード lambda を使うと、名前のない小さな関数を生成できます。

> ラムダ式は、構文上単一の式に制限されています。

内容が1行の関数を表せる記法らしい。

### 書式

```
lambda 引数名: 文
```

文の結果がreturnされる関数になる。

### 関数を変数に入れて使いまわす

0.py
```python
l = lambda x: print(x)
l(100)
```
```sh
$ python3 0.py
100
```

### 1回限りの使い捨て関数

1.py
```python
(lambda x: print(x))(100)
```
```sh
$ python3 1.py
100
```

### 戻り値

2.py
```python
l = lambda x: x + 1
print(l(100))
```
```sh
$ python3 2.py
101
```

## 配列の並び替え

```python
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
print(pairs)
```
```sh
$ python3 3.py
[(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]
```
[list.sort()のkey引数](https://docs.python.jp/3/howto/sorting.html#key-functions)として関数を指定する。その関数はソートする値を返すものとする。

ここでは`pairs[1]`である。つまり`one`, `two`, 'three', 'four'の文字列をソートキーとした。出力結果をみると`four`, `one`, `three`, `two`のようにアルファベット順にソートされていることがわかる。

### 辞書の並び替え

```python
from operator import itemgetter
d = {'Z': 1, 'Y': 2, 'X': 3, 'W': 4}
print(d)
print(sorted(d.items(), key=itemgetter(1)))
```

* http://qiita.com/ysk24ok/items/b546471c37b2f443f4c7

以降は[ソート HOW TO](https://docs.python.jp/3/howto/sorting.html#sorting-how-to)の項で学ぶこととする。

