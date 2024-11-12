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

#Animalクラスの定義
class Animal:
    def __init__(self, name):
        self.name = name

    def move(self, distance):
        print(f'{self.name}は、{distance}メートル移動しました。')


#Dogクラスの定義
class Dog(Animal):
    #Animalクラスのmoveメソッドをオーバライド（上書き）
    def move(self, distance):
        print(f'{self.name}は、{distance}メートル走りました。')

#Birdクラスの定義
class Bird(Animal):
    #Animalクラスのmoveメソッドをオーバライド（上書き）
    def move(self, distance):
        print(f'{self.name}は、{distance}メートル飛びました。')

#Whaleクラスの定義
class Whale(Animal):
    #Animalクラスのmoveメソッドをオーバライド（上書き）
    def move(self, distance):
        print(f'{self.name}は、{distance}キロメートル泳ぎました。')

#犬オブジェクトの生成
dog = Dog('犬')
#鳥オブジェクトの生成
bird = Bird('鳥')
#クジラオブジェクトの生成
whale = Whale('クジラ')

#moveメソッドの実行
dog.move(10)
bird.move(1000)
whale.move(50)