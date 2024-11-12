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
    def ennsyuu(self, hannkei):
        print(f'円周の長さ: {hannkei * 2 * self.PI}')

    def mennseki(self, hannkei):
        print(f'円の面積: {hannkei ** 2 * self.PI}')

A = int(input('半径を整数値で入力: '))
B = Circle()
B.ennsyuu(A)
B.mennseki(A)