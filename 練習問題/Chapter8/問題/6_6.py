""" 
開始数、終了数を入力後、開始数から終了数までを全て合計し、
計算結果を画面に表示するプログラムを作成しなさい。
ただし、「リスト内包表記」を用いること。
【実行例】
開始数: 30
終了数: 100
合  計: 4615 
"""
a = int(input('開始数: '))
b = int(input('終了数: '))
x = sum([i for i in range(a, b + 1)])
print(f'合  計: {x}')