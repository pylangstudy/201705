# [5.1. リスト型についてもう少し](https://docs.python.jp/3/tutorial/datastructures.html#more-on-lists)

< [5. データ構造](https://docs.python.jp/3/tutorial/datastructures.html#data-structures) < [Python チュートリアル](https://docs.python.jp/3/tutorial/index.html) < [ドキュメント](https://docs.python.jp/3/index.html)

## list.append()

### `append()`

list.append.0.py
```python
l = [1,2,3]
l.append(4)
# l.append([5,6]) # [1, 2, 3, 4, [5, 6]]
# l.append(*[5,6]) # TypeError: append() takes exactly one argument (2 given)
print(l)
```
```sh
$ python3 list.append.0.py 
[1, 2, 3, 4]
```

### `l[len(l):] = [x]`

list.append.1.py
```python
l = [1,2,3]
l[len(l):] = [4]
l[len(l):] = [5,6]
print(l)
```
```sh
$ python3 list.append.1.py 
[1, 2, 3, 4, 5, 6]
```

#### `l[len(l)] = 4` (`IndexError`)

list.append.2.py
```python
l = [1,2,3]
l[len(l)] = 4 # IndexError: list assignment index out of range
print(l)
```
```sh
$ python3 list.append.2.py 
IndexError: list assignment index out of range
```

## `list.extend()`

### `extend([x,y])`

list.extend.0.py
```python
l = [1,2,3]
l.extend([4,5])
print(l)
```
```sh
$ python3 list.extend.0.py
[1, 2, 3, 4, 5]
```

### `extend(range(s, e))`

list.extend.1.py
```python
l = [1,2,3]
l.extend(range(4,6))
print(l)
```
```sh
[1, 2, 3, 4, 5]
```

### `extend((x, y))`

list.extend.2.py
```python
l = [1,2,3]
l.extend((4,5))
print(l)
```
```sh
$ python3 list.extend.2.py
[1, 2, 3, 4, 5]
```

### `extend({'k': 'v'}.values())`

list.extend.3.py
```python
l = [1,2,3]
l.extend({'key1': '100', 'key2': '200', 'key3': '300'}.values())
print(l)
```
```sh
$ python3 list.extend.3.py
[1, 2, 3, '300', '100', '200']
```

## `list.insert()`

### `insert(0, x)`

list.insert.0.py 
```python
l = [1,2,3]
l.insert(0, 100)
print(l)
```
```sh
$ python3 list.insert.0.py 
[100, 1, 2, 3]
```

### `insert(len(l), x)`

list.insert.1.py 
```python
l = [1,2,3]
l.insert(len(l), 100)
print(l)
```
```sh
$ python3 list.insert.1.py 
[1, 2, 3, 100]
```

## `list.remove()`

### `list.remove(x)`

list.remove.0.py
```python
l = [1,2,1,3]
l.remove(1)
print(l)
```
```sh
$ python3 list.remove.0.py 
[2, 1, 3]
```

### `list.remove(x)` (`ValueError`)

list.remove.1.py
```python
l = [1,2,1,3]
l.remove(4)
print(l)
```
```sh
$ python3 list.remove.1.py
ValueError: list.remove(x): x not in list
```

値が存在したら消すことはできるが、無いときにスルーできない。

### `list.remove(x)` try-except

list.remove.2.py
```python
l = [1,2,1,3]
try:
    l.remove(4)
except:
    pass
print(l)
```
```sh
$ python3 list.remove.2.py 
[1, 2, 1, 3]
```

[8.3. 例外を処理する](https://docs.python.jp/3/tutorial/errors.html#handling-exceptions)にある`try-except`文で例外をキャッチし、[pass](https://docs.python.jp/3/tutorial/controlflow.html#pass-statements)文でエラーをスルーする。冗長な記述になってしまう。

### `del l[i]`

list.remove.3.py
```python
l = [1,2,1,3]
del l[0]
print(l)
```
```sh
$ python3 list.remove.3.py 
[2, 1, 3]
```

### `del l[s:e]`

list.remove.4.py
```python
l = [1,2,3,4]
del l[1:3]
print(l)
```
```sh
$ python3 list.remove.4.py 
[1, 4]
```

### `del l[i]` (`IndexError`)

list.remove.5.py
```python
l = [1,2,3,4]
del l[100]
print(l)
```
```sh
$ python3 list.remove.5.py 
IndexError: list assignment index out of range
```

`list.remove()`だけでなく`del`文でもエラーになる。削除操作でエラーがでないようにするにはtry-except文を使うしかないのか。

## `list.pop()`

### `pop()`

list.pop.0.py
```python
l = [1,2,1,3]
print(l.pop())
print(l)
```
```sh
$ python3 list.pop.0.py
3
[1, 2, 1]
```

### `pop(x)`

list.pop.1.py
```python
l = [1,2,1,3]
print(l.pop(1))
print(l)
```
```sh
$ python3 list.pop.1.py 
2
[1, 1, 3]
```

#### ドキュメントの説明

```
list.pop([i])
```

> i の両側にある角括弧は、この引数がオプションであることを表しているだけなので、角括弧を入力する必要はありません。この表記法は Python Library Reference の中で頻繁に見ることになるでしょう。

配列の`[]`と見分けがつかないのですが……。そういえば以下のような表記があった。

```
list.extend(iterable)

> a[len(a):] = iterable と等価です。
```

配列は`iterable`と表記し、API引数の`[]`はオプション引数を表すということだろうか？少なくとも表記を統一しているとは書いていない。iterableは配列だけでなく`range()`の戻り値なども含まれているから、文脈次第で使い分けられるのだろう。`iterable`の正体は現時点で不明だが。

## `list.clear()`

### `clear()`

list.clear.0.py 
```python
l = [1,2,1,3]
l.clear()
print(l)
```
```sh
$ python3 list.clear.0.py 
[]
```

### `del l[:]`

list.clear.1.py 
```python
l = [1,2,1,3]
del l[:]
print(l)
```
```sh
$ python3 list.clear.1.py 
[]
```

## `list.index()`

### `index(x)`

list.index.0.py 
```python
l = [10,20,30,40]
print(l.index(30))
```
```sh
$ python3 list.index.0.py 
2
```

指定した値が最初に見つかったindex値を返す。

### `index(x)` (`ValueError`)

list.index.1.py 
```python
l = [10,20,30,40]
print(l.index(999))
```
```sh
$ python3 list.index.1.py 
ValueError: 999 is not in list
```

値が存在しないと`ValueError`を返す。

### `index(x, s, e)`

list.index.2.py 
```python
l = [10,20,30,40]
print(l)
v = 30
print("v={0} i={1}".format(v, l.index(30, 0, len(l))))
```
```sh
$ python3 list.index.2.py 
[10, 20, 30, 40]
v=30 i=2
```

`l.index(30, 0, len(l))`はリスト`l`の中から値`30`が最初に見つかったindex値を返す。範囲は全index。

### `index(x, s, e)` (`ValueError`)

list.index.3.py 
```python
l = [10,20,30,40]
print(l)
s, e = 0, 2
print(l[s:e])
print(l.index(30, s, e))
```
```sh
$ python3 list.index.3.py 
[10, 20, 30, 40]
v=30 i=2
[10, 20]
ValueError: 30 is not in list
```

`l.index(30, s, e)`は、0〜1のindex内から30を探す。存在しないので`ValueError`。

### `index(x,s,e)` 先頭位置を返す

> 返される添字は、start 引数からの相対位置ではなく、リスト全体の先頭からの位置になります。

list.index.4.py
```sh
l = [10,20,30,40]
print(l)
s, e = 1, 4
print(l[s:e])
print(l.index(30, s, e))
```
```
$ python3 list.index.4.py 
[10, 20, 30, 40]
[20, 30, 40]
2
```

## `list.count(x)`

> x の出現回数を返します。

list.count.0.py
```python
l = [11, 22, 11, 22, 33, 11]
print(l.count(11))
print(l.count(22))
print(l.count(33))
```
```sh
$ python3 list.count.0.py 
3
2
1
```

## `list.sort()`

### `sort()`

list.sort.0.py 
```python
l = [3,2,1]
print(l)
l.sort()
print(l)
```
```sh
$ python3 list.sort.0.py 
[3, 2, 1]
[1, 2, 3]
```

### `sort(key)` ラムダ式

list.sort.1.py
```python
l = [{'key': 300}, {'key': 200}, {'key': 100}]
print(l)
l.sort(key = lambda x: x['key'])
print(l)
```
```sh
$ python3 list.sort.1.py 
[{'key': 300}, {'key': 200}, {'key': 100}]
[{'key': 100}, {'key': 200}, {'key': 300}]
```

* list.sort()の`key`引数は関数である
    * key引数に渡す関数は[ソートに使うキーを返す関数を指定する](https://docs.python.jp/3/library/functions.html#sorted)
        * 戻り値: ソートに使うキー値
        * 引数: listの1要素

`def func(listの1要素): return ソートに使うキー値`という形式の関数を渡せばいい。

### `sort(key)` def関数

list.sort.2.py 
```python
def ReturnKey(item):
    return item['key']

l = [{'key': 300}, {'key': 200}, {'key': 100}]
print(l)
l.sort(key = ReturnKey)
print(l)
```
```sh
$ python3 list.sort.2.py 
[{'key': 300}, {'key': 200}, {'key': 100}]
[{'key': 100}, {'key': 200}, {'key': 300}]
```

ラムダ式でなくdef定義した関数で渡してみた。`l.sort(key = ReturnKey)`という形になる。C言語でいう関数ポインタを渡したような形にみえる。

### `l.sort(reverse=True)`

list.sort.3.py
```python
l = [1,2,3,4]
print(l)
l.sort(reverse = True)
print(l)
```
```sh
$ python3 list.sort.3.py 
[1, 2, 3, 4]
[4, 3, 2, 1]
```

昇順でなく降順にする。

## `list.copy()`

### `copy()`

list.copy.0.py 
```python
l = [1,2,3,4]
c = l.copy()
c[0] = 100
print(l)
print(c)
```
```sh
$ python3 list.copy.0.py 
[1, 2, 3, 4]
[100, 2, 3, 4]
```

### `l[:]`

list.copy.1.py 
```python
l = [1,2,3,4]
c = l[:]
c[0] = 100
print(l)
print(c)
```
```sh
$ python3 list.copy.1.py 
[1, 2, 3, 4]
[100, 2, 3, 4]
```

## 戻り値 None なメソッド

* `append()`
* `extend()`
* `insert()`
* `remove()`
* `sort()`

list.return.None.methods.py
```python
l = [1,2,3,4]
print(l.append(5))
print(l.extend([6,7]))
print(l.insert(len(l), 8))
print(l.remove(8))
print(l.sort(reverse=True))
```
```sh
$ python3 list.return.None.methods.py 
None
None
None
None
None
```

Pythonではデータ構造オブジェクトのうちデータ構造を変更するメソッドの戻り値はすべてNoneを返すらしい。オブジェクト自身の参照や、複製されたオブジェクトの返却を期待しても無駄ということ。

