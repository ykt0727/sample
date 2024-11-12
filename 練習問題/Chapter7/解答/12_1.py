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

#Calculatorクラスの定義
class Calculator:
    #合計を求めるメソッド
    def calcSum(self, num1, num2):
        return num1 + num2
    
    #平均を求めるメソッド
    def calcAve(self, num1, num2):
        return (num1 + num2) / 2


#MoreCalcクラスの定義（Calculatorクラスを継承)
class MoreCalc(Calculator):
    #累乗を求めるメソッド
    def calcPow(self, num1, num2):
        return num1 ** num2


#MoreCalcクラスのオブジェクトを生成
calc = MoreCalc()

#整数を入力させる処理
num1 = int(input('整数を入力してください: '))
num2 = int(input('整数を入力してください: '))

#calcSum, calcAve, calcPowメソッドの呼び出し
sum = calc.calcSum(num1, num2)
ave = calc.calcAve(num1, num2)
pow = calc.calcPow(num1, num2)

#結果の表示
print(f'Sum {num1} and {num2} = {sum}')
print(f'Average {num1} and {num2} = {ave}')
print(f'Power {num1} of {num2} = {pow}')