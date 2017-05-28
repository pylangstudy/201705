# [3.1.2. 文字列型 (string)](https://docs.python.jp/3/tutorial/introduction.html#strings)

< [3.1. Python を電卓として使う](https://docs.python.jp/3/tutorial/introduction.html#using-python-as-a-calculator) < [3. 形式ばらない Python の紹介](https://docs.python.jp/3/tutorial/introduction.html#an-informal-introduction-to-python) < [Python チュートリアル](https://docs.python.jp/3/tutorial/index.html)

## リテラル

> 文字列は単引用符 ('...') もしくは二重引用符 ("...") で囲み

```python
>>> 'abc'
'abc'
>>> "abc"
'abc'
>>> var = 'abc'
>>> var
'abc'
>>> var = "abc"
>>> var
'abc'
>>> print(var)
abc
```

### ネストでエスケープ不要

`''`と`""`の2種類あるからネストするときお互いを`\`エスケープせずに済む。

```python
>>> var = 'title="AAA"'
>>> var
'title="AAA"'
>>> print(var)
title="AAA"
```
```python
>>> var = "title='AAA'"
>>> var
"title='AAA'"
>>> print(var)
title='AAA'
>>> 

C言語の場合、`""`しかないから、以下のようになる。

```c
char *var = "\"AAA\""; // "AAA"
```
```c
char *var = "'AAA'"; // 'AAA'
```

## エスケープ

> \ は引用符をエスケープするのに使います

```python
>>> var = "abc\"def\""
>>> var
'abc"def"'
>>> print(var)
abc"def"
```
```python
>>> var = 'abc\'def\''
>>> var
"abc'def'"
>>> print(var)
abc'def'
```

### `\n`

改行コード。

```python
>>> var = 'abc\ndef'
>>> var
'abc\ndef'
>>> print(var)
abc
def
```

### `\t`

TABコード。

```python
>>> var = 'abc\tdef'
>>> var
'abc\tdef'
>>> print(var)
abc	def
>>> 
```

### エスケープ記号`\`を文字として解釈する

上記は`\n`が改行コードとして解釈されてしまう。

```python
>>> print('C:\num')
C:
um
```

引用符の前に`r`を付与すると`\`を文字として解釈する。

```python
>>> print(r'C:\num')
C:\num
```

## 三連引用符

`\n`と入力せずとも改行できる。

```python
>>> print('''abc
... def''')
abc
def
```
```python
>>> print("""abc
... def""")
abc
def
```

## 文字列の連結

### `+`

```python
>>> 'abc' + 'def'
'abcdef'
```

### ` `(space)

```python
>>> 'abc' 'def'
'abcdef'
```

### `*`

```python
>>> 'abc' * 3
'abcabcabc'
```

### 複数行にまたがるリテラル

```python
>>> ('abc'
... 'def')
'abcdef'
```

```python
>>> ('abc' + 
... 'def')
'abcdef'
```

### 変数と結合

文字列を指定回数くりかえす。

```python
>>> var = 'abc'
>>> var
'abc'
>>> var + 'def'
'abcdef'
```
```python
>>> var * 3
'abcabcabc'
```

ただしスペースでの結合はできない。
```python
>>> var 'def'
  File "<stdin>", line 1
    var 'def'
            ^
```

## インデックス

### 正数

先頭1文字目を`0`として数える。

```python
>>> var = 'abc'
>>> var[0]
'a'
>>> var[1]
'b'
>>> var[2]
'c'
>>> var[3]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range
```
```python
>>> varJ = '日本語'
>>> varJ[0]
'日'
>>> varJ[1]
'本'
>>> varJ[2]
'語'
```

### 負数

末尾1文字目を`-1`として数える。

```python
>>> var[-1]
'c'
>>> var[-2]
'b'
>>> var[-3]
'a'
>>> var[-4]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range
```
```python
>>> varJ = '日本語'
>>> varJ[-1]
'語'
>>> varJ[-2]
'本'
>>> varJ[-3]
'日'
```

### ゼロ

```python
>>> var[-0]
'a'
>>> var[0]
'a'
```
```python
>>> varJ[0]
'日'
>>> varJ[-0]
'日'
```

## スライス

指定したインデックス範囲の部分文字列を取得する。

```python
>>> var = 'abcdefg'
>>> varJ = '日本語ですが何か？'
```

コード|var|varJ|説明
------|---|----|----
`[2:]`|'cdefg'|'語ですが何か？'|var[2]とそれ以降を含んだ部分文字列を返す。
`var[:2]`|'ab'|'日本'|先頭からvar[2]までを含んだ部分文字列を返す。
`var[2:5]`|'cde'|'語です'|2〜4文字目までの部分文字列を返す。

### 文字列は変更できない

> Python の文字列は変更できません – つまり不変 ([immutable](https://docs.python.jp/3/glossary.html#term-immutable)) なのです。

> 文字列のインデクスで指定したある場所に代入を行うとエラーが発生します

```python
>>> var = 'abcdefg'
>>> var[0] = 'A'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
```

## 長さ

```python
>>> var = 'abcdefg'
>>> len(var)
7
>>> len(varJ)
9
``` 

組込み関数[len()](https://docs.python.jp/3/library/functions.html#len)。バイト長でなく文字数が取得される。

## 参考

* [テキストシーケンス型 — str](https://docs.python.jp/3/library/stdtypes.html#textseq)
* [文字列メソッド](https://docs.python.jp/3/library/stdtypes.html#string-methods)
* [フォーマット済み文字列リテラル](https://docs.python.jp/3/reference/lexical_analysis.html#f-strings)
* [書式指定文字列の文法](https://docs.python.jp/3/library/string.html#formatstrings)
* [printf 形式の文字列書式化](https://docs.python.jp/3/library/stdtypes.html#old-string-formatting)

各項での学習に持ち越す。

