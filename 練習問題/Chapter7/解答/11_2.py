""" 
変数xとyに値(x≦y)を代入し、xとyまでの合計値を求めるプログラムを作成しなさい。
演算実行クラスを作成し、合計値を求めるメソッドをクラス内に定義し、変数x, yは演算実行クラスのクラス変数とする。
メイン処理は演算実行クラスとは別にクラスを定義し、以下の実行結果となるようにプログラムを作成しなさい。

【実行結果】
100から200までの合計値は15150です。
"""

#演算実行クラス
class CalcSum:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def calculate(self):
        total = 0
        for i in range(self.num1, self.num2 + 1):
            total += i
        return total

#実行クラス
class Main:
    def run(self):
        # 計算実行インスタンスの生成
        calc = CalcSum(100, 200)
         # 合計値を取得
        result = calc.calculate()
        # 結果を表示
        print(f'{calc.num1}から{calc.num2}までの合計値は{result}です。')


# メインクラスの生成とメイン処理実行
e = Main()
e.run()