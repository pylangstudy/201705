# [3.2. プログラミングへの第一歩](https://pylangstudy.github.io/docs.python.jp.Progress.v0/)

< [3. 形式ばらない Python の紹介](https://docs.python.jp/3/tutorial/introduction.html#an-informal-introduction-to-python) < [Python チュートリアル](https://docs.python.jp/3/tutorial/index.html)

## Fibonacci 級数列

[フィボナッチ数列](https://ja.wikipedia.org/wiki/%E3%83%95%E3%82%A3%E3%83%9C%E3%83%8A%E3%83%83%E3%83%81%E6%95%B0)を作るコード。

```python
a, b = 0, 1
while b < 10:
    print(b)
    a, b = b, a+b
```
```python
>>> a, b = 0, 1
>>> while b < 10:
...     print(b)
...     a, b = b, a+b
... 
1
1
2
3
5
8
```

### 同時代入

```python
>>> a,b=100,200
>>> a
100
>>> b
200
```

#### tuple型

以下のようにするとtupleとして表示された。tupleはまだPythonドキュメントのチュートリアルに出てきていない。
```python
>>> a,b
(100, 200)
```

tupleは変更不可なlist。
```python
>>> t = (1,2,3)
>>> t[0] = 100
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
```

tupleで同時代入もできた。
```python
>>> a,b=(300,400)
>>> a
300
>>> b
400
>>> a,b
(300, 400)
```

### 数の不一致

```python
>>> a,b = 1,2,3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: too many values to unpack (expected 2)
```

左辺と右辺の要素数が違うと上記エラーになる。ただし左辺が1つの場合は以下のように[tuple略記](#tuple略記)として解釈されるようだ。

### tuple略記

```python
>>> a = 1,2,3
>>> a
(1, 2, 3)
```

`(1,2,3)`とせずともtupleになってくれるらしい。`a = 1,2,3`と`a = (1,2,3)`は同一か。Pythonドキュメントには書いていない。

### while文

#### 条件式

`while b < 10:`文の条件式は`b < 10`である。条件式の結果が真(True)ならループを継続する。偽(False)ならループを終了する。

> ゼロでない整数値は真となり、ゼロは偽です。

* `while True:`とすると無限ループになる
* `while False:`とすると一切ループしない

#### 比較演算子

表記|意味
----|----
`<`|より小さい
`>`|より大きい
`<=`|以下
`>=`|以上
`==`|等しい
`!=`|等しくない
`is`|同一のオブジェクトである
`is not`|同一のオブジェクトでない

https://docs.python.jp/3/library/stdtypes.html#comparisons

2項比較演算子。

#### コロン

Pythonドキュメントには書かれていないが、コロン`:`を行末に付与している。

if, for, while, def, classなど複数行に渡って定義する構文には行末に`:`をつける。さもなくば以下の構文エラーとなる。

```python
>>> while False
  File "<stdin>", line 1
    while False
              ^
SyntaxError: invalid syntax
```

高頻度で犯す凡ミス。なのにエラーを見ても何をどうすればいいか不明。`:`付与すべきと知らねば対処できない。

#### インデント

ループ文の本体はインデントする必要がある。

```python
while b < 10:
    print(b)
    a, b = b, a+b
```

インデントしないと以下のエラーが出る。

```python
>>> while False:
... print('a')
  File "<stdin>", line 2
    print('a')
        ^
IndentationError: expected an indented block
```

インデントはスペース1つでもOK。対話モードならできるだけ少ないほうが楽か。
```python
>>> while False:
...  print('a')
```

インデントのスペース数を間違えてしまうとエラーになる。
```python
>>> while False:
...  print('a')
...   print('b')
  File "<stdin>", line 3
    print('b')
    ^
IndentationError: unexpected indent
```

C言語の`{}`とどちらが良いか賛否両論ある。バグの元にもなりうる。

* インデントのスペース数はいくつでもいい
* インデント幅はブロックごとに統一されてればいい
	* コード全体で統一されていなくてもいい
* タブとスペースの混合インデントはpython3でエラー
* タブは内部で8文字スペースに置き換えられる

自由すぎるとバグや読みづらさによる誤りを誘発する。使い方を決めたほうがいい。

* 対話モードではスペース1つ。短く済むから
* ソースファイルではスペース4つ。見やすいから
* TAB(ハードタブ)は使わない。バグを避けるため
	* タブとスペースの混合インデントはpython3でエラー
	* タブは内部で8文字スペースに置き換えられる
		* もしインデントが4つなら2つ分になってしまいエラーになる

http://studylog.hateblo.jp/entry/2015/10/22/043739

Pythonコードを書くならテキストエディタによるハードタブからスペースに置換する機能が必須。

### print文

Pythonドキュメント本文にはないが、print文に`()`をつけたほうがいい。

Python2,3どちらでも実行可能。
```python
>>> print('a')
a
```

Python2のみ実行可能。3ではエラー。
```python
>>> print 'a'
  File "<stdin>", line 1
    print 'a'
            ^
SyntaxError: Missing parentheses in call to 'print'
```

## 罠まとめ

* コロン
* インデント
* `print`の`()`有無

