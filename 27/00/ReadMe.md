# [1. やる気を高めよう](https://docs.python.jp/3/tutorial/appetite.html)

## Pythonは作業の自動化に適した言語

> 自動化したい作業が出てくるでしょう。
> Pythonはそんなあなたのための言語です。
> あなたの作業を素早く行う助けになる

まさに自動化したいからPythonを選んだ。ピッタリらしい。

## やる気はとくに高まらなかった

* 文字ばかりで飽きた
    * 端的なコードで「スゲー！」と思わせてくれたほうがやる気が出る
* やる気を出さねば使えないのか。無気力でも気軽に使いたい
    * なにせ面倒な作業の自動化が目的なので

たぶん予備知識がないと価値が想像しづらいのだろう。無知な愚者はインパクトを求めてしまうが、どこにもない。

個人的には以下のコードでHTTP要求できると知ってやる気が出た。標準ライブラリではないが。

```python
import requests
r = requests.get('https://www.google.co.jp')
print(r.text)
```

## C言語と比較して自慢されても…

> コンパイルやリンクが必要ないので、プログラムを開発する際にかなりの時間を節約できます。

shell, Ruby, C#, Javaなど多くの言語でもC言語ほど時間のかかるコンパイルはしない。むしろPythonにはコンパイルエラーが出ないことで実行時エラーが多く、かなりの時間を浪費させられた記憶が……。

## コンパクトで読みやすいプログラム？

> とてもコンパクトで読みやすいプログラムを書けます。

> * 高レベルのデータ型によって、複雑な操作を一つの実行文で表現できます。

> * 実行文のグループ化を、グループの開始や終了の括弧ではなくインデントで行えます。

> * 変数や引数の宣言が不要です。

たしかにPythonは文字数が少ない。タイピング時間は短い。エディタの補助なしに少ないタイプ数で済むのはとても嬉しい。しかし「読みやすい」かは微妙。また、別の副作用を伴う。

### 「短い語で高レベル」にした弊害の一例

* `printf("\n")` が `print()` で書ける。しかし改行を取り払うことはできない
* インデントは一つでもスペースの数が違うとエラーになる
* 静的型付ができず実行時エラーが増える

### 「短い＝読みやすい」ではない

キーワードは短いが「読みやすい」かは微妙。たとえば以下のような `os.path` のメソッド名など。短くするため暗号的になる。パッと見よくわからない。

* `os.path.isdir()`
* `os.path.dirname()`
* `os.path.basename()`
* `os.path.abspath()`
* `os.path.abspath(os.path.dirname(__file__))`

すべて小文字のせいもある。ライブラリによって名前の付け方も統一されていない。C#のほうが読みやすく書きやすい気もする。

また、C#のようによく分類された名前空間名でないから思い出しづらい。パッケージ名やメソッド名など何度もググることになる。長いがわかりやすいのと、短いがわかりにくいの、どちらが「読みやすい」のかは一概に言えない。

## 書き捨てプログラムが簡単に書ける

> 書き捨てのプログラムを書いたり

これも嬉しい。欲を言えば以下の点が面倒。

* Python2,3のバージョンを使い分ける必要がある
    * ソースコード1行目に `#!python3` と書く
    * 実行コマンドが `python` だと2, `python3` だと3が実行される
* 文字コードを指定する必要がある
    * python3ならUTF-8がデフォルトらしいがPython2は違う?

ファイルの先頭に以下を書くのが面倒。

```python
#!python3
#encoding: utf-8
```

## あまりワクワクしなかった

> Python にワクワクして、もうちょっと詳しく調べてみたくなったはずです。

C言語と比べられても……。ワクワクというより、時短できることを推していたような。文章だけではつまらない。HTML/CSS/JSのPlaygroundのように動くものが見えないと。

なんとか自力でワクワクさせてみよう。

以下のコードをご覧あれ。PythonはC言語に比べて超コンパクトで読みやすい！すごい！偉い！ワクワク！

hello.py
```python
print('Hello Python !!')
```
[![ideone](http://www.google.com/s2/favicons?domain=ideone.com)](http://ideone.com/Df5yfz)

hello.c
```python
#include <stdio.h>
int main(void) {
	printf("Hello World !!\n");
	return 0;
}
```
[![ideone](http://www.google.com/s2/favicons?domain=ideone.com)](http://ideone.com/opXMHg)
