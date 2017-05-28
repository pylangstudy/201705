# [3.1.3. リスト型 (list)](https://docs.python.jp/3/tutorial/introduction.html#lists)

< [3.1. Python を電卓として使う](https://docs.python.jp/3/tutorial/introduction.html#using-python-as-a-calculator) < [3. 形式ばらない Python の紹介](https://docs.python.jp/3/tutorial/introduction.html#an-informal-introduction-to-python) < [Python チュートリアル](https://docs.python.jp/3/tutorial/index.html)

3.1.2, 3.1.3では電卓として使っていない。3.1に包含されていない。3.1.1だけは電卓として使っていた。

## 書式

コンマ区切りの値 (要素) の並びを角括弧で囲んだものとして書き表されます。

```python
>>> l = [1,2,3]
>>> l
[1, 2, 3]
```

## 型不同

> リストは異なる型の要素を含むこともあります

```python
>>> l = [1,'a',False,None]
>>> l
[1, 'a', False, None]
```

## スライス

```python
>>> l[0]
1
>>> l[1]
2
>>> l[2]
3
>>> l[-1]
3
>>> l[-2]
2
>>> l[-3]
1
>>> l[1:]
[2, 3]
```

## 浅いコピー

```python
>>> m = l[:]
```
```python
>>> l
[1, 2, 3]
>>> m = l[:]
>>> m
[1, 2, 3]
>>> m[0] = 2
>>> m
[2, 2, 3]
>>> l
[1, 2, 3]
```

## 連結

```python
>>> l + m
[1, 2, 3, 2, 2, 3]
```
```python
>>> l + [100,200,300]
[1, 2, 3, 100, 200, 300]
```
```python
>>> [1,3,5] + [7,9,11]
[1, 3, 5, 7, 9, 11]
```

## リストは可変([mutable](https://docs.python.jp/3/glossary.html#term-mutable))である

> 不変 ([immutable](https://docs.python.jp/3/glossary.html#term-immutable)) な文字列とは違って、リストは可変 ([mutable](https://docs.python.jp/3/glossary.html#term-mutable)) 型、つまり含んでいる要素を取り替えることができます

```python
>>> l
[1, 2, 3]
>>> l[0] = 100
>>> l
[100, 2, 3]
```

## append()

> 末尾に新しい要素を追加する

```python
>>> l
[1, 2, 3]
>>> l.append(4)
>>> l
[1, 2, 3, 4]
```

## スライスに代入

```python
>>> l = [1,2,3,4,5]
>>> l
[1, 2, 3, 4, 5]
>>> l[1:3] = [20,30]
>>> l
[1, 20, 30, 4, 5]
```

## len()

```python
>>> l = [1,2,3,4,5]
>>> len(l)
5
```

## ネスト

```python
>>> l = [[1,2],[3,4],[5,6]]
>>> l
[[1, 2], [3, 4], [5, 6]]
>>> l[0]
[1, 2]
>>> l[0][0]
1
```

## 挿入

`append()`で末尾追加、代入やスライス代入で上書き。ならば指定位置に挿入はどうするのか？`insert()`を使うらしい。

```python
>>> l = [1,2,3]
>>> l.insert(1,100)
>>> l
[1, 100, 2, 3]
```

https://docs.python.jp/3/tutorial/datastructures.html

他の関数についてはいずれ。

