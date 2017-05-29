# [4.2. for 文](https://docs.python.jp/3/tutorial/controlflow.html#for-statements)

< [4. その他の制御フローツール](https://docs.python.jp/3/tutorial/controlflow.html#more-control-flow-tools) < [Python チュートリアル](https://docs.python.jp/3/tutorial/index.html) < [ドキュメント](https://docs.python.jp/3/index.html)

## for文

Pythonのfor文はC言語のfor文とは違う。for-each文である。

0.py
```python
for i in ['ab', 'cd', 'ef']:
    print(i)
```
```sh
$ python3 0.py
ab
cd
ef
```

C言語のfor文と比べると以下の点が問題になるかもしれない。

* カウンタ変数がない
* 指定回数くりかえす

### カウンタ変数

#### 自力で用意する

ダサい…。

1.py
```python
index = 0
for item in ['ab', 'cd', 'ef']:
    print("{0}: {1}".format(index, item))
    index += 1
```

```sh
$ python3 1.py
0: ab
1: cd
2: ef
```

#### `enumerate()`

スマート！

2.py
```python
for index, item in enumerate(['ab', 'cd', 'ef']):
    print("{0}: {1}".format(index, item))
```

```sh
$ python3 2.py
0: ab
1: cd
2: ef
```

http://qiita.com/sotoshigoto/items/4e13193581e468c02f1b

### tuple型

tuple型でも使える。

3.py
```python
for index, item in enumerate(('ab', 'cd', 'ef')):
    print("{0}: {1}".format(index, item))
```    
```sh
$ python3 3.py
0: ab
1: cd
2: ef
```

### dict型

まだドキュメントに出てないが、dict型でも使える。

4.py
```python
d = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
for key in d.keys():
    print("{0}: {1}".format(key, d[key]))
```
```sh
$ python3 4.py
key2: value2
key1: value1
key3: value3
```

dict型は順序が保持されない。

### collections.OrderedDict型

5.py
```python
from collections import OrderedDict
d = OrderedDict()
d['key1'] = 'value1'
d['key2'] = 'value2'
d['key3'] = 'value3'
for key in d.keys():
    print("{0}: {1}".format(key, d[key]))
```
```sh
$ python3 5.py
key1: value1
key2: value2
key3: value3
```

#### コンストラクタでは順序が保たれない罠

なんと、コンストラクタで初期化すると順序が保たれない……。残念すぎる。バグの元。

```python
d = OrderedDict({'key1': 'value1', 'key2': 'value2', 'key3': 'value3'})
d = OrderedDict(key1='value1', key2='value2', key3='value3')
```

```python
from collections import OrderedDict
d = OrderedDict({'key1': 'value1', 'key2': 'value2', 'key3': 'value3'})
for key in d.keys():
    print("{0}: {1}".format(key, d[key]))
```
```sh
$ python3 6.py 
key3: value3
key1: value1
key2: value2
```

```python
from collections import OrderedDict
d = OrderedDict(key1='value1', key2='value2', key3='value3')
for key in d.keys():
    print("{0}: {1}".format(key, d[key]))
```
```sh
$ python3 7.py 
key1: value1
key3: value3
key2: value2
```

#### 順序を保って代入せずに初期化したい

代入するのは冗長。もっと楽にリテラルで初期化できないか。

```python
from collections import OrderedDict
d = OrderedDict( (('key1','value1'), ('key2','value2'), ('key3','value3')) )
for key in d.keys():
    print("{0}: {1}".format(key, d[key]))
```
```python
$ python3 8.py 
key1: value1
key2: value2
key3: value3
```

http://shannon-lab.org/?p=1743

