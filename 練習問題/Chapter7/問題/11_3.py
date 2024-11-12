"""  
500円、100円、50円、10円、5円、1円がそれぞれ何枚あるか管理する小銭入れクラスを定義しなさい。
この小銭れクラスに、指定した硬貨の枚数を追加するaddCoinsメソッド、
引数で指定した硬貨が何枚あるか返却するgetCountメソッド、
小銭入れクラスの総額を返すgetAmountメソッドの3つのメソッドを定義する。
この小銭入れクラスのインスタンスを生成し、addCoinsメソッドで10回ランダムに選択したコインを追加した後、
各硬貨が何枚あるかと総額を画面に表示するプログラムを作りなさい。

【実行例】
1円:2枚 5円:0枚 10円:1枚 50円:1枚 100円:1枚 500円:5枚 
総額: 2,662円

"""
import random

class Coin:
    def __init__(self):
        self.A = 0
        self.B = 0
        self.C = 0
        self.D = 0
        self.E = 0
        self.F = 0
    def addCoins(self, coin):
        if coin == 1:
            self.A += 1
        elif coin == 2:
            self.B += 1
        elif coin == 3:
            self.C += 1
        elif coin == 4:
            self.D += 1
        elif coin == 5:
            self.E += 1
        elif coin == 6:
            self.F += 1
    def getCount(self):
        print(f'1円:{self.A}枚 5円:{self.B}枚 10円:{self.C}枚 50円:{self.D}枚 100円:{self.E}枚 500円:{self.F}枚')
    
    def getAmount(self):
        print(f'総額: {self.A + self.B * 5 + self.C * 10 + self.D * 50 + self.E * 100 + self.F * 500}円')

G = Coin()
for i in range(10):
    n = random.randint(1, 6)
    G.addCoins(n)
G.getCount()
G.getAmount()