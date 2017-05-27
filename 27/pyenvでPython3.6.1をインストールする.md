# pyenvでPython3.6.1をインストールする

< [pyenvをインストールする](https://github.com/pylangstudy/201705/27/pyenvをインストールする.md) < [Python学習環境を用意する](https://github.com/pylangstudy/201705/27/Python学習環境を用意する.md)

## Pythonのコンパイルに必要なライブラリをインストールする

```sh
$ sudo apt-get install libbz2-dev libreadline-dev libsqlite3-dev
```

Pythonをインストールする前に必要。これ以外にもライブラリが必要なら後でエラーになる。エラーログを目視で解析して必要なツールを探しインストールせねばならない。そこが最も難しく苦労する。

## pyenvを起動する

```sh
$ bash -l
$ pyenv -v
pyenv 1.0.10
```

### Python3.6.1をインストールする

```sh
$ pyenv install 3.6.1
```

### pyenvで利用するバージョンを指定する

```sh
$ pyenv global 3.6.1
$ python -V
Python 3.6.1
```

### HelloWorld

test.py
```python
#!python3
#encoding: utf-8
print('Hello World !!')
```

```sh
$ python test.py
Hello World !!
```

Pythonコードが実行された。環境構築完了。

# 完了

環境構築終了。

