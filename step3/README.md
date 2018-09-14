# SlackBot を作ろう

## Slack とは

![slack-chat-image](./image/WHAT_IS_SLACK_Slack_overview.png)

詳しく知りたい方は [Slack はじめてガイド](https://get.slack.help/hc/ja/articles/115004071768) を参照してください。


## Bot とは

Bot(ボット)とはロボットのことです。
この資料の中で Bot と言った場合にはすべてチャットボットのことを指します。
チャットボットとは、会話を自動的に行うプログラムです。

チャットボットは単なるおしゃべりロボットだけではなく、ビジネスの場でも使われ始めています。

つまり、SlackBot とは、Slack 上で動くチャットボットのことですね。


# Bot を動かす準備

bot を動かす準備をしましょう。
step3 のディレクトリは以下のようになっています。

```bash
step3/
├── README.md
├── image/
├── requirements.txt
├── samplebot/
│   ├── __init__.py
│   ├── plugins/
│   ├── run.py
│   └── slackbot_settings.py
├── setup.py
└── test/
```


## モジュールをインストール

`step3` ディレクトリに移動して、必要なモジュールをインストールします。

```bash
$ cd step3
$ pip3 install -r requirements.txt
```

`slackbot` というモジュールが追加されます。

```bash
$ pip3 list
...
slackbot            0.5.3
slacker             0.9.65
...
```


## bot の動かし方を確認

`run.py` を実行すると、Bot を起動することができます。

```bash
step3/
└── samplebot/
    └── run.py
```

`samplebot` ディレクトリに移動しておきましょう。

``` bash
$ cd samplebot
```

とにかく、Bot を動かしてみよう。以下のコマンドを実行します。

```bash
$ python3 run.py
```

まだ、Bot が Slack にアクセスする設定をしていないので、こんなメッセージが出てプログラムが終了します。

```bash
$ python run.py
start slackbot
Traceback (most recent call last):
  File "run.py", line 13, in <module>
    main()
  File "run.py", line 7, in main
    bot = Bot()
  File ".../slackbot/bot.py", line 25, in __init__
    'BOT_EMOJI') else None
  File ".../slackbot/slackclient.py", line 37, in __init__
    self.rtm_connect()
  File ".../slackbot/slackclient.py", line 40, in rtm_connect
    reply = self.webapi.rtm.start().body
  File ".../slacker/__init__.py", line 666, in start
    'mpim_aware': int(mpim_aware),
  File ".../slacker/__init__.py", line 117, in get
    api, **kwargs
  File ".../slacker/__init__.py", line 99, in _request
    raise Error(response.error)
slacker.Error: invalid_auth
```

エラーメッセージの最後の行に注目してください。Auth とは認証のことです。
"invalid\_auth" とは不正な認証。つまり認証に失敗していることがわかります。

```bash
slacker.Error: invalid_auth
```

認証の設定を追加して、Slack 上で Bot が動作するようにしましょう。


# Slack に Bot を登録する

手順にしたがって Slack に Bot を登録しましょう。


## Slack の PyCon 2018 tutorial ワークスペースに参加

メールアドレスを使って、Slack に参加しましょう。
招待用の URL は講師から案内します。

<https://goo.gl/*****>

![join slack](./image/join-input-mail.png)

入力したメール宛に Slack ワークスペース参加用の URL が送信されます。クリックして参加しましょう。


## チャンネルの作成

チャンネル `#general`、 `#random` には全員が参加していて、みんなでワイワイお喋りをする場に向いています。

今回は、他の人のメッセージで邪魔されないように bot 動かすための自分専用のチャンネルを作ります。チャンネルの `+` ボタンをクリックして自分だけのチャンネルを作ってみましょう。

![img](./image/add-channel.png)

名前を入力して「チャンネルを作成する」をクリックします。名前は `bot-<ユニークな名前>` にしましょう。
**\<ユニークな名前\>** の部分にアルファベットで自分の好きな名前を入れましょう。「ユニーク」というのは「他の人と違う」という意味です。
自分の名前、ペットの名前、好きなキャラクターの名前など、他の人が思いつかないような名前をつけてください。

![img](./image/add-channel-name.png)


## Bot の登録

Slack で動かすために、Bot を Slack にアプリとして登録をしましょう。
以下の URL にアクセスします。

<https://api.slack.com/apps>

画面を開いたら右上の方にある「Create an App」ボタンをクリックします。

![img](./image/create-app.png)

アプリ(App name)の名前は先程のチャンネル名と同じが良いでしょう。ユニークな名前をつけてください。
ワークスペース(Development Slack Workspace)には **pycon2018-tutorial** を選択します。

![img](./image/create-app-popup.png)

アプリを Bot として設定しましょう。「Bots」をクリックします。

![img](./image/bot-user-button.png)

Bot user を作成します。これは Slack チャンネル上でユーザー名として見える部分です。
「Add a Bot User」をクリックします。
先程のアプリ名と同じ名前が入っていると思いますのでそのまま「Add a Bot User」をクリックして登録します。

![img](./image/bot-user-form.png)

Bot を「PyconJP 2018 チュートリアル」Workspace に追加します。
以下の順でリンクをクリックしてください。

1. Basic information
2. Install your apps to workspace
3. Install App to Workspace

![img](./image/add-bot-to-workspace-goto.png)

「許可する」ボタンをクリックします。

![img](./image/add-bot-to-workspace.png)


## Bot をチャンネルに参加させる

Slack のアプリに戻りましょう。タブを消してしまった場合は講師から共有された URL をクリックすれば、表示できます。

左側のチャンネルタブから自分が作成したチャンネルを探してクリックします。

![img](./image/how-to-open-channel.png)

チャンネルが開いたら、左上の歯車ボタンからユーザーを追加します。

![img](./image/how-to-add-user.png)

作成した bot のユーザー名で検索して「招待する」をクリックします。

![img](./image/search-bot-user.png)

チャンネルに招待されたユーザー一覧は右上の `( i )` マークのアイコンから確認できます。

![img](./image/how-to-show-info.png)

![img](./image/show-channel-users.png)


## Bot Api Token を取得

Bot を Slack に認証するための Api Token を取得します。
タブを閉じてしまった人は <https://api.slack.com/apps> にアクセスして、自分の Bot の設定を開きましょう。

Bot 用の認証 Token をコピーします。以下の順番で画面をクリックしてコピーしましょう。

1. OAuth & Permissions
2. Bot User OAuth Access Token の 「Copy」ボタン

![img](./image/oauth-tokens.png)

コピーした Api Token をプログラムに貼り付けます。 `slackbot_settings.py` をエディタで開きましょう。

``` bash
step3/
├── README.md
└── samplebot/
    └── slackbot_settings.py  ←
```

ファイルの 1 行目に以下のように貼り付けます。

```python
API_TOKEN = "xoxb-xxxxxxxxxxx-xxxxxxxxxxxx-xxxxxxxxxxxxxxxxxxxxxxxx"
```


# ① Hello SlackBot

SlackBot が「こんにちは」というメンションに反応して「こんにちは」を返事することを確認しながら、機能を追加します。

```bash
step3/
└── samplebot/
    ├── run.py
    ...
```

予め `step3/samplebot` ディレクトリに移動しておきましょう。

```bash
$ cd step3/samplebot
```


## Bot を起動する

Bot を動かしてみましょう。 `run.py` を実行することで Bot を起動します。

```bash
$ python3 run.py
start slackbot
```

実行してもコマンドライン上では何も起こりませんが、エラーが発生していなければ正常に実行されています。 この状態で `Ctrl + c` を入力すると停止します。


## 「こんにちは」を言ってみよう

`@ユーザー名` を付けてメッセージを投稿すると、その人に宛てたメッセージとして扱われます。
これを、Slack ではメンションといいます。

![img](./image/input-hello.png)

Bot を起動した状態で「こんにちは」とメンションすると、返事をします。

![img](./image/bot-says-hello.png)


## [解説] : メンションを反応させる

この機能は `hello.py` です。ファイルを開いてみましょう。

```bash
step3/
└── samplebot/
    ├── plugins/
    │   ├── hello.py  ←
    ...
```

bot をメンションに反応させるには、 `@respond_to` デコレータを使います。

```python
from slackbot.bot import respond_to

@respond_to('こんにちは')  # ← 反応させたい文字列
def hello(message):
    message.reply('こんにちは')  # ← 返事の内容
```

![img](./image/how-work-slackbot.png)


## [課題] : リアクションを追加してみましょう


### リアクションとは？

Slack ではメンションの他に絵文字で気持ちを表す機能があり、 **リアクション** といいます。

![img](./image/how-to-reaction.png)


### Bot からリアクションする

リアクションに使用する各絵文字にはコード(例: `+1` )が割り振られています。コードは絵文字パレットから確認できます。

![img](./image/reaction-code.png)


### コードの追加

`hello()` 関数の末尾にリアクションを追加しましょう

```python
def hello(message):
    message.reply('こんにちは')
    message.react('+1')  # ← この行を追加した
```


### Bot を再起動する

変更を適用するには Bot を再起動する必要があります。Bot を再起動するには `Ctrl + c` を入力して一度 Bot を停止し、再度 `python3 run.py` を実行します。

Bot へのメンションがリアクションされることを確認しましょう。

![img](./image/reaction-from-bot.png)


## [課題] : デフォルトの返事を設定してみましょう

Bot は知らない言葉に対して返事をすることができません。

![img](./image/bot-bad-command.png)


### デフォルトの返事を追加する

デフォルトの返事をさせるには関数に `@default_reply` デコレータを追加します。
デフォルトの返事をする関数を新しく作ってみましょう。

```python
from slackbot.bot import respond_to, default_reply  # ← default_reply を新しく import した

# ↓ 新しい関数を追加した
@default_reply
def reply_default_message(message):
    message.reply('その言葉はわかりません')
```

追加したら bot を再実行して返事を確認してみましょう。


### こんにちはをデフォルトの返事にする

「こんにちは」の返事がデフォルトの返事を兼ねることもできます。

```python
@default_reply
@respond_to('こんにちは')
def hello(message):
    message.reply('こんにちは')
```

設定できる `@default_reply` は 1 つだけです。他の関数に付けている `@default_reply` は消しましょう。


# ② おみくじ

bot が起動していない場合は、起動しておきましょう。

```bash
$ python3 run.py
start slackbot
```


## おみくじを引いてみよう

「おみくじ」とメンションすると結果を返事します。

![img](./image/omikuji-pick.png)

おみくじを引くたびに結果が変わります。

![img](./image/omikuji-pick2.png)


## [解説] : ランダムにおみくじを引く

結果をランダムに変えるときには `random` モジュールを使います。 `random.choice()` 関数は、リストの中からランダムに 1 つだけ選んで値を返します。

`random` モジュールを試してみましょう。

ターミナル上で `python3` コマンドを **ファイル名なし** で実行すると、その場で python を試せます。対話(インタラクティブ)モードといいます。

```python
$ python3
Python 3.6.6 (default, Aug 20 2018, 13:50:58)
[GCC 4.2.1 Compatible Apple LLVM 9.1.0 (clang-902.0.39.2)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

対話モードでは、1 行ごとにコマンドが実行され、結果が次の行に表示されます。同じ関数を何度も実行して試せます。

```python
>>> import random
>>> nums = [1, 2, 3, 4, 5]
>>> random.choice(nums)  # リストからランダムに値を取り出しました
2
>>> random.choice(nums)  # 方向キー ↑ を押すと前のコマンドをもう一度実行できます
3
>>> random.choice(nums)  # 値は毎回変わります
3
>>> random.choice(nums)
2
```

この機能は `omikuji.py` です。ファイルを開いてみましょう。

```bash
step3/
└── samplebot/
    ├── plugins/
    │   ├── omikuji.py  ←
    ...
```

おみくじ機能では、リストの中におみくじの結果が入っています。

```python
OMIKUJI_LIST = [
    '大吉',
    '中吉',
    '吉',
    '末吉',
    '凶',
    '大凶',
]

@respond_to('おみくじ')
def omikuji(message):
    message.reply(random.choice(OMIKUJI_LIST))
```


## [課題] : 「ランチは何食べる？」 機能を追加してみよう

「ランチ」とメンションすると何を食べたらいいかを返事する機能を作ってみましょう。

リストを用意して、 `random.choice()` 関数を使って値をランダムに取り出しましょう。例えば、以下のようになります。

```python
LUNCH_TYPE = [
    '中華',
    '和食',
    'イタリアン',
]

@respond_to('ランチ')
def lunch(message):
    message.reply(random.choice(LUNCH_TYPE))
```

プログラムを書き換えたら、Bot を再起動して動作を確認しましょう。


# ③ じゃんけん

Bot が起動していない場合は、起動しておきましょう。

```bash
$ python3 run.py
start slackbot
```


## じゃんけんをしてみよう

「ぐー」 「チョキ」 「パー」のどれかをメンションするとじゃんけんの手を返事します。

![img](./image/janken-play.png)


## [解説] : 「ぐー」 「チョキ」 「パー」のどれにも返事をする

いろいろなメンションに対して同じ返事をするには、関数の数を増やせば作れます。
しかし、同じコードを何度も書いてしまっていて効率が悪いですね。

```python
@respond_to('グー')
def janken_gu(message):
    message.reply(choice())

@respond_to('チョキ')
def janken_choki(message):
    message.reply(choice())

@respond_to('パー')
def janken_pa(message):
    message.reply(choice())
```

`slackbot` モジュールは **正規表現** に対応していて、特別な書き方をすると 1 つの文字列でいろいろなパターンに返事をできるようになります。

以下のように書くと `|` で区切った文字列のどれか 1 つに当てはまれば良い。という意味です。どれかに当てはまることを、 **マッチ** するといいます。 `|` は `Shift + \` で入力できます。

```python
'グー｜チョキ｜パー'
```

`()` で囲まれた部分にマッチすると、マッチした文字列を引数として受け取れます。

```python
@respond_to('(グー|チョキ|パー)')
def janken(message, shape):  # ← 引数 shape に「グー」「チョキ」「パー」のどれかが入る
    message.reply(choice())
```

Python の正規表現について詳しく知りたい方は [正規表現操作](https://docs.python.jp/3/library/re.html) のページを見てください。


## [課題] : じゃんけんに勝てるようにしよう

例のプログラムは、じゃんけんの手をランダムに返しているだけです。じゃんけんに勝てるように変更してみましょう。

`shape` 変数の中身を見れば、メンションした人がどの手を出したのかがわかります。 `if` 条件分岐を使用すれば、相手の手の内容を見て、勝ち手を選んで出せそうです。

```python
@respond_to('(グー|チョキ|パー)')
def janken(message, shape):
    if shape == 'グー':
        message.reply(JANKEN_CHOICES['パー'])
        return
    if shape == 'チョキ':
        message.reply(JANKEN_CHOICES['グー'])
        return
    if shape == 'パー':
        message.reply(JANKEN_CHOICES['チョキ'])
        return
```

プログラムを書き換えたら、Bot を再起動して動作を確認しましょう。


# ④ メッセージの中身

bot が起動していない場合は、起動しておきましょう。

```bash
$ python3 run.py
start slackbot
```


## bot が受信するメッセージ

これまで、bot が受信したメッセージオブジェクトを使ってユーザーに返事したり、リアクションしたりしました。

```python
@respond_to('こんにちは')
def hello(message):
    message.reply('こんにちは')  # 引数の message オブジェクトを使って返事をしている
```

これ以外にも、受信した `message` オブジェクトにはいろいろな情報が詰まっているので、それを見ていきましょう。


## メッセージの中身を覗いてみよう

Bot に「debug」とメンションしてみましょう。 受信したメッセージの中身を解析して返事をしてくれます。

![img](./image/debug-message.png)

大きく分けて `message.body` と `message.user` があります。これらは辞書(dict)ですから、以下のようにすれば簡単にアクセスできます。

```python
message.body['text']  # メンションしたメッセージの内容

message.user['name']  # ユーザーの名前
message.user['profile']['display_name']  # チャットに表示されている名前
message.user['profile']['email']  # ユーザーのメールアドレス
```

今回の課題はありません。次のステップに進みましょう。


# ⑤ 人数カウント

bot が起動していない場合は、起動しておきましょう。

```bash
$ python3 run.py
start slackbot
```


## Bot に人数を数えてもらおう

1.  「カウント ○○」とメンションすると人数のカウントを始めます。
2.  Bot は「はい」と言った人の人数を数えます。
3.  カウントを始めた人が「締切」とメンションするとカウントをやめて合計人数を返事します。

![img](./image/count-play.png)


## [解説]: 人数を数える、メンション以外に反応する


### PeopleCounter クラス

今回は複数回のメッセージのやり取りで状態を保持しておく必要がるので、クラスを作成しました。 関連する状態をまとめて管理するために、クラスを使うと便利になることがあります。

`PeopleCounter` クラスは以下のように使います。

```python
people = PeopleCounter()

# カウント機能を呼び出した人を設定する
people.setup('John', 'ランチに行く人！')

# 参加したい人がいたら追加する
people.add('Alice')
people.add('Bob')
people.add('John')

# 人数を確認する
print(people.count()) # 3

# 参加者を確認する
print(people.list()) # John, Alice, Bob
```

このクラスは今までと比べて行数が多いですが、よく見るとほとんどがコメント行で説明文です。 クラスの中身を隅々まで読まなくても、Bot を実行している関数 `start_count()` や `add_member()` を見て理解すだけで、全体的な動作は十分理解できます。


### メンション以外にも反応する

気がついたかもしれませんが、今回の機能はメンション以外にも反応しています。

![img](./image/count-play-hai.png)

`@listen_to` デコレータを使うとメンション以外のメッセージに反応することができます。

```python
from slackbot.bot import listen_to

@listen_to('はい')
def add_member(message):
    ...
```

`@listen_to` はメンション以外のどんなメッセージにも反応するので、注意が必要です。 今回は「はい」を含むメッセージに反応していますが、反応するのはカウント機能が実行中のときだけです。 それ以外の時、誰かが「はい」と言っても無視します。


## [課題]: 「やっぱり参加できなくなった…」機能を追加してみよう

今の機能では、一度「はい」と返事してしまったら取り消すことができません。途中で参加できなくなったときに参加を取り消せるように、機能を追加してみましょう。

例えば、「いいえ」とメンションされたときに参加者を削除したい場合は、「はい」のときとほとんど同じ方法で実現できそうです。

```python
@listen_to('いいえ')
def remove_member(message):
    if people.caller is not None:
        people.remove(message.user['name'])  # add を remove に変えた
        message.react('ok')
```

変数 `people` 、つまり `PeopleCounter` クラスにはまだ `remove()` メソッドが無いので、これを作る必要があります。

```python
class PeopleCounter:

    ...

    def remove(self, name):
        """参加できなくなったメンバーを削除する

        Args:
            name: 削除する人の名前
        """
        if name in self.members:
            self.members.remove(name)
```

プログラムを書き換えたら bot を再起動して、動作を確認しましょう。

`set` は重複する要素を勝手に削除してくれます。これのおかげで、同じ人が何度返事をしても一人としてカウントします。
`list` では要素を追加するのに `list.append()` を使いましたが、 `set` の場合は `set.add()` メソッドです。気になる人は対話モードで動作を確認しましょう。

``` python
$ python3
>>> a = {1,2,3,3,3}  # set の宣言には {} または set() を使います。
>>> a
{1, 2, 3}
>>> a.add(4)
>>> a
{1, 2, 3, 4}
>>> a.add(3)
>>> a
{1, 2, 3, 4}
```


# ⑥ 三目並べ

Bot が起動していない場合は、起動しておきましょう。

```bash
$ python3 run.py
start slackbot
```


## 三目並べとは

![img](./image/tictactoe-image.png)

3 マス x 3 マス のボード上で 2 人のプレイヤーが交互に ○、✕ を書いていき、 タテ・ヨコ・ナナメのどれかの方向に同じマークが揃った人の勝ちというゲームです。


## 三目並べで遊ぶ

「三目並べ」とメンションすると、三目並べが始まります。

続けて番号をメンションすると、その場所に自分のマーク「○」を置くことができます。bot はランダムで選んだ場所にマーク「✕」を置きます。

![img](./image/tictactoe-play.png)

ゲームが終わると、bot は結果を返事します。

![img](./image/tictactoe-won.png)


## [課題]: 中身を覗いてみよう


### samplebot をインストール

samplebot をモジュールとしてインストールすることで、対話モードでも動作を確認できます。step3 ディレクトリに移動して、インストールしてみましょう。

```bash
$ cd ..
$ pwd
(...)/PyConTutorialSampleCode/step3
$ pip install -e .
```

`.` でカレントディレクトリの `setup.py` を指定しています。 `-e` オプションは開発者モードでインストールするという意味です。


### Board クラス

`Board` クラスは三目並べのボード管理します。ボードを管理すると簡単に言っても実際やることは多いです。

- 今は誰がプレイしている？
- プレイヤーはどのマスにマークを置ける？
- どのプレイヤーが勝った？
- など…

対話モードを起動して、動作を確認します。

```bash
$ python3
>>>
```

まずは、 `Board` を初期化しましょう。

```python
>>> from samplebot.plugins.libs.tictactoe import Board, Player
>>> board = Board()
>>> player1 = Player('o')
>>> player2 = Player('x')
>>> board.setup(size=3, players=[player1, player2])
>>> print(board)
:zero::one::two:
:three::four::five:
:six::seven::eight:
```

`board` の出力は Slack の絵文字に最適化されているので、 `is_slack` フラグを変更して コマンドラインでも見やすいようにします。

```python
>>> board.is_slack = False
>>> print(board)
 0 1 2
 3 4 5
 6 7 8
```

`board.player` を見ると、プレイ中のプレイヤーを確認できます。 マークを置いたときに、このプレイヤーのマークが置かれます。

```python
>>> print(board.player)
o
```

`put_n()` メソッドでマークを置けます。 `board` を見ると、 `2` が `o` に変わりました。

```python
>>> board.put_n(2)
'o'
>>> print(board)
 0 1 o
 3 4 5
 6 7 8
```

`swtich_player_turn()` メソッドで次のプレイヤーに交代します。

```python
>>> board.switch_player_turn()
<samplebot.plugins.libs.tictactoe.Player object at 0x102fe4400>
>>> print(board.player)
x
>>> board.put_n(0)
'x'
>>> print(board)
 x 1 o
 3 4 5
 6 7 8
```

`won()` メソッドで今のプレイヤーが勝ったかどうかがわかります。

```python
>>> board.won()
False
>>> board.put_n(3)
'x'
>>> board.put_n(6)
'x'
>>> print(board)
 x 1 o
 x 4 5
 x 7 8
>>> board.won()
True
```


## [課題]: ゲームの設定を変更してみよう

`Board` クラスの `setup()` メソッドを変更すれば、ゲームの設定を変更することができます。

`setup()` メソッドを探し出して、 引数を `size=4` に変更してみましょう。

```python
game.board.setup(size=4, players=[Player(':o:'), Player(':x:')])
```

プログラム変更したら、Bot を再起動して、動作を確認しましょう。
