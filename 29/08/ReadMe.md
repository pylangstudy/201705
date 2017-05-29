# [4.7.1. デフォルトの引数値](https://docs.python.jp/3/tutorial/controlflow.html#default-argument-values)

< [4.7. 関数定義についてもう少し](https://docs.python.jp/3/tutorial/controlflow.html#more-on-defining-functions) < [4. その他の制御フローツール](https://docs.python.jp/3/tutorial/controlflow.html#more-control-flow-tools) < [Python チュートリアル](https://docs.python.jp/3/tutorial/index.html) < [ドキュメント](https://docs.python.jp/3/index.html)

## 必須引数

```python
def AddOne(value):
    return value + 1

print(AddOne(7))
```
```sh
$ python 0.py
8
```

## オプション引数

引数にデフォルト値を設定する。

```python
def AddOne(value=99):
    return value + 1

print(AddOne())
print(AddOne(7))
```
```sh
$ python 1.py
100
8
```

呼出側で引数が渡されなかったとき、定義時に設定したデフォルト値が代入される。

### オプション引数が複数あるときの呼出

2.py
```python
def Sum(value1=1, value2=2):
    return value1 + value2

print(Sum())
print(Sum(value1=100))
print(Sum(value2=200))
print(Sum(value1=100, value2=200))
print(Sum(100,200))
print(Sum(100))
```
```sh
$ python 2.py
3
102
201
300
300
102
```

## 必須引数＋オプション引数

* 必須の引数のみ与える
* 全ての引数を与える: ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')
* オプション引数を与える

```python
def Sum(value1, value2=200, value3=300):
    return value1 + value2 + value3

print(Sum(10))
print(Sum(10, 20))
print(Sum(10, 20, 30))
print(Sum(10, value2=20))
print(Sum(10, value3=30))
print(Sum(10, value2=20, value3=30))
```
```sh
$ python 3.py
510
330
60
330
240
60
```

## デフォルト値の変数指定

4.py
```python
v3 = 333
def Sum(value1, value2=200, value3=v3):
    return value1 + value2 + value3

v3 = 999
print(Sum(10))
```
```sh
$ python 4.py
543
```

引数のデフォルト値として`333`が設定された。定義時点での`v3`は`333`だから。

> デフォルト値は 1 度だけしか評価されません。

コードは先頭行から順に実行される。1行目で`v3 = 333`、2行目で`value3=v3`なので引数のデフォルト値は`333`になる。たとえ後続に`v3 = 999`があっても反映されない。引数のデフォルト値は1度だけしか評価されないから。

### 変更可能なオブジェクトの場合、継続されてしまう

5.py
```python
def Append(value, l=[]):
    l.append(value)
    return l

print(Append(1))
print(Append(2))
print(Append(3))
```
```sh
$ python 5.py
[1]
[1, 2]
[1, 2, 3]
```

変更可能(mutable)な場合、最後に代入された値がデフォルト値になってしまう。はたしてそれは「デフォルト値」と言えるのか。

### Noneで回避する

```python
def Append(value, l=None):
    if l is None:
        l = []
    l.append(value)
    return l

print(Append(1))
print(Append(2))
print(Append(3))
print(Append(7,[1,3,5]))
```
```sh
$ python 6.py
[1]
[2]
[3]
[1, 3, 5, 7]
```

## in キーワード

関数とは関係ない話。

> シーケンスが特定の値を含んでいるかどうか調べる

`A in B`はBの中にAがあるとき真(True)を返す。ないなら偽(False)を返す。

```python
if 3 in [1, 2, 3]:
    print('3')
if 'b' in ['a', 'b', 'c']:
    print('b')
```
```sh
$ python 7.py
3
b
```

