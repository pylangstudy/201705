# [3.1.1. 数](https://docs.python.jp/3/tutorial/introduction.html#numbers)

< [3.1. Python を電卓として使う](https://docs.python.jp/3/tutorial/introduction.html#using-python-as-a-calculator) < [3. 形式ばらない Python の紹介](https://docs.python.jp/3/tutorial/introduction.html#an-informal-introduction-to-python) < [Python チュートリアル](https://docs.python.jp/3/tutorial/index.html)

## 対話モードによる数値演算

```python
$ python
>>> 1+2
3
```

## Pythonの演算子一覧

演算子|説明
------|----
`+`|加算。足し算。
`-`|減算。引き算。
`*`|乗算。掛け算。
`/`|除算。割り算。浮動少数値になる。`100.0/3`=`33.333333333333336`
`%`|剰余。割った余り。
`**`|冪乗。べき乗。`2**8`=`256`。別言語では`a^b`と表現されることも。
`//`|除算。小数点以下を切り捨てる。`100.0//3`=`33.0`

[参考](http://www.tohoho-web.com/python/operators.html)

## 変数への代入

```python
>>> num = 100
>>> num
100
>>> num / 5
20
```

代入することで変数の宣言も同時に行われる。

### 未定義エラー

`aaa`が未定義のとき、以下のエラーになる。

```python
>>> aaa
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'aaa' is not defined
```

### 変数`_`

> 対話モードでは、最後に表示された結果は変数 _ に代入されます。

```python
>>> _
20
```

#### 変数`_`へ代入すると利用不可になる

> ユーザはこの変数を読取り専用の値として扱うべきです。この変数に明示的な代入を行ってはいけません — そんなことをすれば、同じ名前で元の特別な動作をする組み込み変数を覆い隠してしまうような、別のローカルな変数が生成されてしまいます。

別のローカル変数が生成されると何かまずいの？と思ったのでやってみた。

```python
>>> _ = 999
>>> _
999
>>> 3+3
6
>>> _
999
```

一度`_`に代入すると「最後の計算結果」を参照できなくなってしまう。なので「代入するな」と言っている。なら言語レベルでリードオンリーにして欲しい。ミスしうる時点でバグの元。使わないほうが良さそう。

## 数値型

> int と float に加え、 Python は Decimal や Fraction のような他の数値型をサポートしています。 Python はビルトインで 複素数 もサポートし、 j もしくは J 接尾辞を使って虚部を示します (例。 3+5j)。

### Decimal

```python
>>> import decimal
>>> v = decimal.Decimal(1.4)
>>> v
Decimal('1.399999999999999911182158029987476766109466552734375')
```

`1.4`になってくれない。どうすればいいのか不明。

### Fraction

```python
>>> 3+5j
(3+5j)
```

* [複素数とは？](http://atarimae.biz/archives/500)
    * 虚数とは想像上の数である
    * 「1つの数字で方向(座標)を表す」のに便利
        * `i`をかけることは「原点を中心に反時計回りに90度回転させる」

Pythonでは`i`でなく`j`や`J`で表すらしいが。

