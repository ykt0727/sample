""" 
以下のクラス図(別紙参照)のようにMoreCalcクラスはCalculatorクラスを継承したクラスです。
CalculatorクラスのCalcSumメソッドは2つの引数の合計値を返し、CalcAveメソッドは2つの引数の平均値を返し、
CalcMoreクラスのCalcPowメソッドは引数の累乗を求めて返すメソッドです。
MoreCalcクラスのインスタンスを生成して、以下の実行例を参考に、
入力した2つの整数の合計値、平均値、累乗を画面に表示するプログラムを作成してください。

【クラス図】
別紙参照

【実行例】
整数を入力してください: 2
整数を入力してください: 4
Sum 2 and 4 = 6
Average 2 and 4 = 3
Power 2 of 4 = 16
"""
class Calculator:
    def calSum(self, x, y):
        return x + y
    
    def calAve(self, x, y):
        return (x + y) / 2
    
class MoreCalc(Calculator):
    def calPow(self, x, y):
        return x ** y

x = int(input('整数を入力してください:'))
y = int(input('整数を入力してください:'))
A = MoreCalc()
print(f'Sum {x} and {y} = {A.calSum(x, y)}')
print(f'Average {x} and {y} = {A.calAve(x, y)}')
print(f'Power {x} of {y} = {A.calPow(x, y)}')