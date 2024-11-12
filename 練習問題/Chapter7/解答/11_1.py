"""
Circleクラスを作成し円周の長さを求めるメソッドと面積を求めるメソッドを
それぞれインスタンスメソッドとして作成しなさい。
また、計算時に使用する円周率をCircleクラス内に定数「PI=3.1415」として定義しなさい。
入力された半径を元に、
以下の実行結果となるようにCircleクラスを使用して円周の長さと円の面積を求めるプログラムを作成しなさい。
【実行結果】
半径を整数値で入力: 3
円周の長さ: 18.849
円の面積: 28.273
"""
class Circle:
    PI = 3.1415

    #半径を初期値として設定するためのイニシャライザ
    def __init__(self, radius):
        self.radius = radius

    #円周を求める関数
    def calc_circumference(self):
        return self.radius * 2 * Circle.PI
    
    #面積を求める関数
    def calc_area(self):
        return self.radius * self.radius * Circle.PI
    
#半径の入力
radius = int(input('半径を整数値で入力: '))

#Circleクラスのオブジェクトを生成
c = Circle(radius)

#Circleクラスのcircumferenceメソッドの呼び出し
c_circumference = c.calc_circumference()

#Circleクラスのareaメソッドの呼び出し
c_area = c.calc_area()

#結果の表示
print('円周の長さ:', c_circumference)
print('円の面積:', c_area)