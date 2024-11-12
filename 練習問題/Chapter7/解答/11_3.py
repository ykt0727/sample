"""  
500円、100円、50円、10円、5円、1円がそれぞれ何枚あるか管理する小銭入れクラスを定義しなさい。
この小銭れクラスに、指定した硬貨の枚数を追加するaddCoinsメソッド、
引数で指定した硬貨が何枚あるか返却するgetCountメソッド、
小銭入れクラスの総額を返すgetAmountメソッドの3つのメソッドを定義する。
この小銭入れクラスのインスタンスを生成し、addCoinsメソッドで10回ランダムに選択したコインを追加した後、
各硬貨が何枚あるかと総額を画面に表示するプログラムを作りなさい。

【実行例】

"""
import random

#コインケースクラスの定義
class Coin:
    #コインの種類と枚数を対応付ける辞書
    def __init__(self):
        self.coins_dict = {1:0, 5:0, 10:0, 50:0, 100:0, 500:0}

    #coin(コインの種類)、num(コインの枚数)で追加する関数
    def addCoins(self, coin, num):
        self.coins_dict[coin] += num
    
    #引数で指定したコインの種類(coin)の枚数を返す関数
    def getCount(self, coin):
        return self.coins_dict[coin]
    
    #全硬貨の総額を返却する関数
    def getAmount(self):
        amount = 0
        for kye,value in self.coins_dict.items():
            amount += kye*value
        return amount

# Coinクラスのインスタンス生成 
c = Coin()

# ランダムに硬貨を追加
for _  in range(10):
    num = random.randint(0, 5)
    if num == 0:
        c.addCoins(1, 1)
    elif num == 1:
        c.addCoins(5, 1)
    elif num == 2:
        c.addCoins(10, 1)
    elif num == 3:
        c.addCoins(50, 1)
    elif num == 4:
        c.addCoins(100, 1)
    elif num == 5:
        c.addCoins(500, 1)

# コインケースの情報を表示
for key, value in c.coins_dict.items():
    print(f'{key}円:{value}枚', end=' ')

print()

print(f'総額: {c.getAmount() :,}円')