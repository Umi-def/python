notion-extensionsを開発する前の練習
###################################

=======================
poetry/pyenvで環境構築
=======================

Powershell上にて

::

    $ poetry install
    $ pyenv global 3.9.6

これで準備は完了．

あとはコーディングしてください

=======
task A
=======

あべこべになるような計算クラスを作る

側は既に作ってあるので，class Abekobeの配下にあるdocstringを見ながら，期待の計算結果が得られるような実装してください

テストケースを作ったので以下を実行し，特にエラーが出てなさそうならクリアです

::

    poetry shell
    pytest tests/test_yumin.py

検討を祈ります．


========
task B
========

これから作成します．

予定としてはpythonのライブラリrequestsを利用してAPIを叩きます．