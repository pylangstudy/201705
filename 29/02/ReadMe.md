# [4.1. if 文](https://docs.python.jp/3/tutorial/controlflow.html#if-statements)

< [4. その他の制御フローツール](https://docs.python.jp/3/tutorial/controlflow.html#more-control-flow-tools) < [Python チュートリアル](https://docs.python.jp/3/tutorial/index.html) < [ドキュメント](https://docs.python.jp/3/index.html)

## if文

0.py
```python
if True:
	print('if True.')
```
```sh
$ python3 0.py
if True.
```

> if ... elif ... elif ... は、他の言語における switch 文や case 文の代用となります。

つまりPythonにはswitch文がないということか。

### if-else

1.py
```python
if True:
	print('True!!')
else:
	print('False...')

if False:
	print('True!!')
else:
	print('False...')
```
```sh
$ python3 1.py
True!!
False...
```

### if-elif-else

2.py
```python
a = 100
if 99 == a:
	print('if')
elif 100 == a:
	print('elif')
else:
	print('else')
```
```sh
$ python3 2.py
True!!
False...
```

> キーワード ‘elif‘ は ‘else if’ を短くしたもの

### 1行表記

4.py
```python
a = 100
if 99 == a: print('if')
elif 100 == a: print('elif')
else: print('else')
```
```sh
$ python3 4.py
elif
```

a = 100
if 99 == a: print('if')
elif 100 == a: print('elif')
else: print('else')

### 三項演算子

Pythonドキュメントには無い。キーワードが違うのか？

http://qiita.com/howmuch/items/bf6d21f603d9736fb4a5

```python
変数 = Trueのときの値 if 条件 else Falseのときの値
```

5.py
```python
a = ('True!!') if (True) else ('False...')
print(a)
```
6.py
```python
a = 'True!!' if True else 'False...'
print(a)
```
```sh
True!!
```

Pythonの三項演算子はif文のときと順序が変わるためわかりにくい。覚えにくい。左辺へ代入することを見越してわざとTrue時の値を先頭にしているのだろうか？

#### C言語の三項演算子

```c
条件 ? TRUEの場合の返却値 : FALSEの場合の返却値;
```
```c
(1) ? 100 : -1;
```

`0`が偽(False)。それ以外は真(True)。上記コードは条件式が`1`で真なので`100`を返す。

C言語は順序はif文のときと同じ。`if`,`else`のキーワードを使わないため文字数が少なくて済む。しかし`?`,`:`の特殊記法を覚える必要がある。

