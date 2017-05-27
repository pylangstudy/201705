# [2.1. インタプリタを起動する](https://docs.python.jp/3/tutorial/interpreter.html#invoking-the-interpreter)

< [2. Python インタプリタを使う](https://docs.python.jp/3/tutorial/interpreter.html)

## 実行コマンド

以下のコマンドでインタプリタが実行できるのは知らなかった。

```sh
python3.6
```

`python`, `python3`でできることは知っていたが。試してみると私の環境では`python2`で`python2.7.6`のインタプリタが実行された。

## インストールディレクトリ

OS|インストールパス
--|---------------
Linux|`/usr/local/python`
Windows|`C:\Python36`

今回の[学習環境](https://github.com/pylangstudy/201705/blob/master/25/Python%E5%AD%A6%E7%BF%92%E7%92%B0%E5%A2%83.md)ではpyenvを使っているため`~/.pyenv/versions/`配下にインストールされていると思う。

## 環境変数パスに通す

今回の[学習環境](https://github.com/pylangstudy/201705/blob/master/25/Python%E5%AD%A6%E7%BF%92%E7%92%B0%E5%A2%83.md)ではpyenvを使っているため気にしなくていい。

## 強制終了

- [x] インタプリタは Ctrl+D, Ctrl+Z キーで強制終了できる
- [x] `quit()`で強制終了できる

`quit()`は知らなかった。

## 行編集機能

> コマンドライン編集機能がサポートされているかを最も手っ取り早く調べる方法は、おそらく最初に表示された Python プロンプトに Control-P を入力してみることでしょう。

```sh
$ python
Python 3.6.1 (default, Apr 24 2017, 22:16:16) 
[GCC 4.8.4] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```

上記で Ctrl+P キー押下してみたが、ビープ音が鳴らなかった。^P がエコーバックされることもない。何も起こっていないように見えた。

> 何も起こらないように見えるか、 ^P がエコーバックされるなら、コマンドライン編集機能は利用できません。

私の環境にはなかった。

## 実行コマンド引数`-c`

```sh
python -c command [arg] ...
```

> command に指定した文を実行します。 

知らなかった。試してみた。

### 1行だけ

```sh
$ python -c 'print("Hello Python !!")'
Hello Python !!
```

### 複数行

```sh
$ python -c 'import datetime; print(datetime.datetime.now())'
2017-05-27 17:49:06.969199
```

`;`で1文を完結できる。`;`を書かないと以下のエラーになる。

```sh
SyntaxError: invalid syntax
```

## 実行コマンド引数`-m`

```sh
python -m module [arg] ...
```

> module のソースファイルを、フルパスを指定して起動したかのように実行できます。

これはunittestモジュールにて単体テストするときに実行したことがある。

```sh
python -m unittest TestSome.py
```

## 実行コマンド引数`-i`

> スクリプトを走らせて、そのまま対話モードに入れると便利なことがあります。

どんなに便利か思いつかない。

```sh
python -i some.py
```

## ほかのコマンド

* [コマンドラインと環境](https://docs.python.jp/3/using/cmdline.html#using-on-general)

その項目をやるときに学習すればいい。今は飛ばす。

