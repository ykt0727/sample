""" 
以下のクラス図（別紙参照）のようにAnimalクラスとそのクラスを継承した
Dogクラス、Birdクラス、Whaleクラスを定義する。
Animalクラスのmoveメソッドは整数の引数を受け取り、
その分だけ移動したことをメッセージで画面に表示するメソッドとする。
継承したサブクラスでmoveメソッドをオーバライドし、
そのクラスにふさわしいメッセージに書き換えるようにしなさい。
サブクラスのインスタンスをそれぞれ1つずつ生成し、以下の実行結果となるようにプログラムを作成しなさい。

【クラス図】
別紙参照

【実行結果】
犬は、10メートル走りました。
鳥は、1000メートル飛びました。
クジラは、50キロメートル泳ぎました。
"""
class Animal:
    def __init__(self, name):
        self.name = name
    
    def move(self, length):
        print(f'{self.name}は、{length}メートル移動しました。')

class Dog(Animal):
    def move(self, length):
        print(f'{self.name}は、{length}メートル走りました。')

class Bird(Animal):
    def move(self, length):
        print(f'{self.name}は、{length}メートル飛びました。')

class Whale(Animal):
    def move(self, length):
        print(f'{self.name}は、{length}キロメートル泳ぎました。')

A = Dog('犬')
B = Bird('鳥')
C = Whale('鯨')

A.move(10)
B.move(1000)
C.move(50)