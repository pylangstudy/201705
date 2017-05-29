# [4.7.2. キーワード引数](https://docs.python.jp/3/tutorial/controlflow.html#keyword-arguments)

< [4.7. 関数定義についてもう少し](https://docs.python.jp/3/tutorial/controlflow.html#more-on-defining-functions) < [4. その他の制御フローツール](https://docs.python.jp/3/tutorial/controlflow.html#more-control-flow-tools) < [Python チュートリアル](https://docs.python.jp/3/tutorial/index.html) < [ドキュメント](https://docs.python.jp/3/index.html)

## 文言統一がされていない

* 必須引数、位置指定引数、(ふつうの)引数
* オプション引数、キーワード引数、デフォルト値を指定した引数

## 位置関係

> キーワード引数は位置指定引数の後でなければなりません。

0.py
```python
def AddOne(value, value1=100):
    return value + value1

print(AddOne(7))
print(AddOne(7, 8))
```
```sh
$ python3 0.py
107
15
```

1.py
```python
def AddOne(value1=100, value):
```
```sh
SyntaxError: non-default argument follows default argument
```

## キー名

オプション引数のキー名は定義されたもののうちのどれかでなければならない。

2.py
```python
def AddOne(value, value1=100):
    return value + value1

print(AddOne(abcd=200))
```
```sh
SyntaxError: non-default argument follows default argument 'abcd'
```

## オプション引数は順不同

> 順序は重要ではありません。

3.py
```python
def Sum(value1=100, value2=200):
    return value1 + value2

print(Sum(value1=10, value2=20))
print(Sum(value2=20, value1=10))
```
```sh
$ python3 3.py
30
30
```

## 必須引数もキー名を指定して代入できる

4.py
```python
def Sum(value1, value2=200, value3=300):
    return value1 + value2 + value3

print(Sum(100))
print(Sum(value1=100))
```
```sh
$ python3 4.py
600
600
```

## キー名を複数回指定できない

いかなる引数も値を複数回は受け取れません。

### 必須引数

5.py
```python
def Sum(value1, value2=200, value3=300):
    return value1 + value2 + value3

print(Sum(value1=100, value1=123))
```
```sh
SyntaxError: keyword argument repeated
```

### オプション引数

6.py
```python
def Sum(value1, value2=200, value3=300):
    return value1 + value2 + value3

print(Sum(value2=200, value2=222))
```
```sh
SyntaxError: keyword argument repeated
```

## 任意引数リスト

C言語で言う可変長引数。好きなだけ引数を渡せる。

`def func(*args, **kwargs):`のように定義する。

`def func(arg, opt=1, *args, **kwargs):`の順に定義する。

```python
def func(arg, opt=1, *args, **kwargs):
    print(arg, opt, args, kwargs)

func(0)
func(0, 10)
func(0, 10, 20)
func(0, 10, 20, 30)
func(0, 10, 20, 30, key='value')
func(0, 10, 20, 30, key='value', key2='v2')
```
```sh
$ python3 7.py
0 1 () {}
0 10 () {}
0 10 (20,) {}
0 10 (20, 30) {}
0 10 (20, 30) {'key': 'value'}
0 10 (20, 30) {'key2': 'v2', 'key': 'value'}
```

