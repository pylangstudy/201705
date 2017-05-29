# [4.4. break 文と continue 文とループの else 節](https://docs.python.jp/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops)

< [4. その他の制御フローツール](https://docs.python.jp/3/tutorial/controlflow.html#more-control-flow-tools) < [Python チュートリアル](https://docs.python.jp/3/tutorial/index.html) < [ドキュメント](https://docs.python.jp/3/index.html)

## break文

> break 文は、C 言語と同じく、最も内側の for または while ループを中断します。

0.py
```python
for i in range(5):
    print(i)
    if i == 2: break
```
```python
$ python3 0.py
0
1
2
```

### ネスト

1.py
```python
for i in range(2):
    for j in range(4):
        if i == 0 and j == 1: break;
        print(i, j)
```
```sh
$ python3 1.py
0 0
1 0
1 1
1 2
1 3
```

### for-else文

> 反復処理対象のリストを使い切ってループが終了したとき、または (while で) 条件が偽になったときに実行されます

2.py
```python
for i in range(3):
    print(i)
else:
    print('for end.')
```
```sh
$ python3 2.py
0
1
2
for end.
```

> break 文でループが終了したときは実行されません。

3.py
```python
for i in range(5):
    if i == 2: break;
    print(i)
else:
    print('for end.')
```
```sh
$ python3 3.py
0
1
```

`else`といえば`if`文だが、Pythonでは`for`文, `try`文でも使えるらしい。

#### なぜelseなのか

elseは`他`という意味らしい。breakせずに完了したときに行う文を`else`で表現するのがよくわからない。

#### いつ使うのか

* `break`文を内包しているとき
* `break`しなかった場合の処理を書きたいとき

どんなときに使うのがいいのかわからなかった。少なくとも以下の場合、`break`でなく直接`return`したほうが見やすい。

4.py
```python
def IsContains(item):
    for i in ['abc','def','ghi']:
        if i == item:
            return True
    return False
print(IsContains('ghi'))
```

無理やりbreak-elseを使ってみた。冗長。
5.py
```python
def IsContains(item):
    for i in ['abc','def','ghi']:
        if i == item:
            break
    else:
        return False
    return True
print(IsContains('ghi'))
```

breakを使わずelseを使うこともできた。しかし 4.py に`else:`を付与する理由がよくわからない。

6.py
```python
def IsContains(item):
    for i in ['abc','def','ghi']:
        if i == item:
            return True
    else:
        return False
print(IsContains('ghi'))
```

`for-else`文は使わなくてもいいか。

## continue文

ループの先頭に戻る。

```python
for i in range(5):
    if i == 3:
        continue
    print(i)
```
```sh
$ python3 7.py
0
1
2
4
```

