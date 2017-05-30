# [4.7.4. 引数リストのアンパック](https://docs.python.jp/3/tutorial/controlflow.html#unpacking-argument-lists)

< [4.7. 関数定義についてもう少し](https://docs.python.jp/3/tutorial/controlflow.html#more-on-defining-functions) < [4. その他の制御フローツール](https://docs.python.jp/3/tutorial/controlflow.html#more-control-flow-tools) < [Python チュートリアル](https://docs.python.jp/3/tutorial/index.html) < [ドキュメント](https://docs.python.jp/3/index.html)

## アンパック

前回、[引数リスト](https://github.com/pylangstudy/201705/tree/master/30/00#%E4%BB%BB%E6%84%8F%E5%BC%95%E6%95%B0%E3%83%AA%E3%82%B9%E3%83%88%E3%81%A8%E3%81%AF)と[引数辞書](https://github.com/pylangstudy/201705/tree/master/30/00#%E4%BB%BB%E6%84%8F%E5%BC%95%E6%95%B0%E8%BE%9E%E6%9B%B8-kwargs)について学んだ通り。`*`, `**`演算子を使ってリストや辞書の変数を引数に渡せる。

## range()

rangeオブジェクトのコンストラクタ`range()`でも`*`演算子を使って渡せる。

```python
>>> list(range(*[0,100,7]))
[0, 7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98]
```

