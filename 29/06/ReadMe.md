# [4.5. pass 文](https://docs.python.jp/3/tutorial/controlflow.html#pass-statements)

< [4. その他の制御フローツール](https://docs.python.jp/3/tutorial/controlflow.html#more-control-flow-tools) < [Python チュートリアル](https://docs.python.jp/3/tutorial/index.html) < [ドキュメント](https://docs.python.jp/3/index.html)

## `pass`文

> pass 文は何もしません。 pass は、文を書くことが構文上要求されているが、プログラム上何の動作もする必要がない時に使われます:

## `while`

> プログラム上何の動作もする必要がない時に使われます

0.py
```python
while True:
    pass # Busy-wait for keyboard interrupt (Ctrl+C, Ctrl+D, Ctrl+Z)```
```sh
$ python3 0.py
```

`Ctrl+Z`キー押下で無限ループを終了させる。

## `class`

> 最小のクラスを作るときによく使われる

1.py
```python
class MyClass:
    pass
c = MyClass()
print(c)
```
```sh
$ python3 1.py
<__main__.MyClass object at 0xb7169eec>
```

## `def`

> 具体的なコードを書かないで抽象的なレベルで考えることができます。

2.py
```python
def MyFunc():
    pass
MyFunc()
```
```sh
$ python3 2.py
```

ただメソッドの名前だけを用意するときに使う。戻り値すら書かないので、この関数をスタブだのモックだのと呼べるかどうかは不明。

http://qiita.com/7of9/items/8e2cb2070f2b2ea4e5ec

