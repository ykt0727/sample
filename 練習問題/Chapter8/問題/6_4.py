""" 
1から10までの数の中で奇数のみを表示するプログラムを作成しなさい。
ただしジェネレータを用いること。
【実行結果】
1 3 5 7 9
"""
for x in (i for i in range(1, 10, 2)):
    print(x)