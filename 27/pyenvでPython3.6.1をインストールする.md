# pyenvでPython3.6.1をインストールする

< [pyenvをインストールする](https://github.com/pylangstudy/201705/blob/master/27/pyenv%E3%82%92%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E3%81%99%E3%82%8B.md) < [Python学習環境を用意する](https://github.com/pylangstudy/201705/blob/master/27/Python%E5%AD%A6%E7%BF%92%E7%92%B0%E5%A2%83%E3%82%92%E7%94%A8%E6%84%8F%E3%81%99%E3%82%8B.md)

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

