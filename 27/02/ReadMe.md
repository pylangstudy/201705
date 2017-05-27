# [2.1.1. 引数の受け渡し](https://docs.python.jp/3/tutorial/interpreter.html#argument-passing)

< [2.1. インタプリタを起動する](https://docs.python.jp/3/tutorial/interpreter.html#invoking-the-interpreter) < [2. Python インタプリタを使う](https://docs.python.jp/3/tutorial/interpreter.html)

## 起動引数

### ファイル実行

0.py
```python
import sys
print(sys.argv)
```

```sh
$ python 0.py
['0.py']
```

```sh
$ python 0.py param1 param2 param3
['0.py', 'param1', 'param2', 'param3']
```

### インライン実行

> -c command を使うと、 sys.argv[0] は '-c' になります。

```sh
$ python -c 'import sys;print(sys.argv)'
['-c']
```

### インタプリタ実行

> スクリプト名も引数も指定しなければ sys.argv[0] は空の文字列になります。

```sh
$ python
>>> import sys
>>> print(sys.argv)
['']
```

> スクリプト名の代わりに '-' (標準入力を意味します) を指定すると、 sys.argv[0] は '-' になります。

```sh
$ python -
>>> import sys
>>> print(sys.argv)
['-']
>>> 
```

### モジュール実行

> -m module を使った場合、 sys.argv[0] はモジュールのフルパスになります

```sh
$ python -m 0
['/tmp/0.py']
```

### 2つ目以降の`-c`や`-m`は実行されずテキストとして引数になる

> -c command や -m module の後ろにオプションを指定した場合、 Python インタプリタ自体はこれらの引数を処理せず、 sys.argv を介して command や module から扱えるようになります。

```sh
$ python -c 'import sys;print(sys.argv)' -m 0
['-c', '-m', '0']
```

```sh
$ python -m 0 -c 'print("a")'
['/tmp/0.py', '-c', 'print("a")']
```

