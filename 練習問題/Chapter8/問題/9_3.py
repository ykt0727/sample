""" 
第1引数で指定された文字列を第2引数で指定された回数分表示する関数をラムダ式で定義しなさい。
その関数を利用して以下の実行結果となるように画面に表示するプログラムを作成しなさい。
【実行結果】
Hello
Hello
Hello
Good morning
Good morning
Good morning
Good morning
Good morning
Good morning
"""
a = lambda b, c: [print(b) for i in range(c)]
a('Hello', 3)
a('Good morning', 6)