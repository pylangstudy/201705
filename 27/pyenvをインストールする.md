# pyenvをインストールする

* 前回: [Python学習環境を用意する](https://github.com/pylangstudy/201705/27/Python学習環境を用意する.md)

## 目的

pyenvを入手してバージョン違いのPythonをインストールできるようにする。

## pyenvインストール

```sh
$ curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash
```

上記でインストールが終わると以下のような警告がされる。

```sh
WARNING: seems you still have not added 'pyenv' to the load path.

# Load pyenv automatically by adding
# the following to ~/.bash_profile:

export PATH="/home/{user}/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```

pyenvには毎回初期化が必要。自動化するにはシェルスクリプトに書いてやるのがいい。

#### pyenvの初期化

```sh
$ echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
$ echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
$ echo 'eval "$(pyenv init -)"' >> ~/.bash_profile
$ exec $SHELL -l
```

`~/.bash_profile` に以下の内容が書き込まれた。

```
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
```

#### pyenv初期化の実行

初期化はターミナル起動するごとに実行する。以下のコマンドで。

```sh
$ exec $SHELL -l
```

もしくは以下。

```sh
$ bash -l
```

たぶん以下でも可能。

```sh
$ source ~/.bash_profile
```

### pyenv実行確認

```sh
$ pyenv -v
pyenv 1.0.10
```

# まとめ

以後、ターミナル起動するたびに以下のコマンドを実行するとpyenvが有効化する。

```sh
bash -l
```

