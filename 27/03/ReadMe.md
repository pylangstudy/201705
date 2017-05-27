# [2.1.2. 対話モード](https://docs.python.jp/3/tutorial/interpreter.html#interactive-mode)

< [2.1. インタプリタを起動する](https://docs.python.jp/3/tutorial/interpreter.html#invoking-the-interpreter) < [2. Python インタプリタを使う](https://docs.python.jp/3/tutorial/interpreter.html) < [Python チュートリアル](https://docs.python.jp/3/tutorial/index.html)

## 呼び名

> インタプリタが命令を端末 (tty) やコマンドプロンプトから読み取っている場合、インタプリタは 対話モード (interactive mode) で動作しているといいます。

「インタプリタを起動する」だと「対話モード」かどうかは定かでない。

### 一次プロンプト

`>>>`で始まる。

```sh
$ python
Python 3.6.1 (default, Apr 24 2017, 22:16:16) 
[GCC 4.8.4] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```

### 二次プロンプト

`...`で始まる。

```sh
>>> flag = True
>>> if flag:
... 
```

二次プロンプトは先頭に1つ以上のスペースを入れる必要がある。さもないと以下のエラーになる。

```sh
IndentationError: expected an indented block
```

```sh
>>> flag = True
>>> if flag:
...  print('a')
... 
a
```

終了するときは何も入力せずにEnterキー押下し空行とする。

## 詳細

[対話モード](https://docs.python.jp/3/tutorial/appendix.html#tut-interac)参照。

本項では対象外。

