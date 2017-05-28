# [2.2.1. ソースコードの文字コード](https://docs.python.jp/3/tutorial/interpreter.html#source-code-encoding)

< [2.2. インタプリタとその環境](https://docs.python.jp/3/tutorial/interpreter.html#the-interpreter-and-its-environment) < [2. Python インタプリタを使う](https://docs.python.jp/3/tutorial/interpreter.html) < [Python チュートリアル](https://docs.python.jp/3/tutorial/index.html)

## UTF-8であると言いつつASCII文字のみにすべきと言う

> デフォルトでは、Python のソースコードは UTF-8 でエンコードされているものとして扱われます。
> ただし、標準ライブラリは識別子に ASCII 文字のみを利用していて、その他のポータブルなコードもその慣習に従うべきです。

日本語は一切使うすべきでないと。何のためのUTF-8なのか。たとえば以下のコードはNG。困る。

```python
# 日本語ダメ
print('日本語ダメ。ASCII文字だけ使え。')
```

### なぜか

> そのファイルに含まれている文字を全てサポートしたフォントを使わなければなりません。

「日本語フォントが無い環境ではコードを閲覧できないから」ということか？

### どうすればいいのか

* 公開するときは日本語をすべてテキストなどに外出しして参照するようにする

かなり手間がかかる。Pythonは国際化の対応をうまいことやってくれないということか？ググったら[見つけた](https://docs.python.jp/3/library/i18n.html)。ライブラリの項に持ち越す。

## マジックコメント

マジックコメントと呼ばれる特殊なコメントにより、デフォルト文字コードを指定する。

### 書式

ファイルの先頭または2行目に以下の様な書式で記入する。

```python
# -*- coding: encoding -*-
```

[7.2.3. 標準エンコーディング](https://docs.python.jp/3/library/codecs.html#standard-encodings)でサポートされているものが使える。`utf-8`なら以下。

```python
# -*- coding: utf-8 -*-
```

#### Shebang

1行目にShebangがあるときは2行目に書く。ShebangとはUNIXスクリプト`#!`で始まる1行目のこと。[参考](http://qiita.com/sesame/items/47d2694616eadb35d4bc#shebang%E3%81%A8%E3%83%9E%E3%82%B8%E3%83%83%E3%82%AF%E3%82%B3%E3%83%A1%E3%83%B3%E3%83%88)

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
```

#### 他の書式

```python
# coding: utf-8
```
```python
# encoding: utf-8
```

* [参考](http://qiita.com/jnchito/items/8f44a3c52d4669fefa93)

このほうが簡単に書ける。

