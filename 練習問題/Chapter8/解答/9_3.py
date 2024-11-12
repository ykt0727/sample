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
#ラムダ式で関数を定義
display = lambda str, num: [print(str) for _ in range(num)]

display('Hello', 3)
display('Good morning', 6)