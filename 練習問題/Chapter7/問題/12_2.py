""" 
以下のクラス図(別紙参照)のように人の基本的な情報を管理するPersonクラスと
Personクラスを継承した、教師の情報を管理するTeacherクラスとコックの情報を管理するCookクラスを定義します。
各クラスは自身の情報を画面に表示するintroduceメソッドを持つ。
TeacherクラスとCookクラスのインスタンスを生成し、以下の実行結果となるようにプログラムを作成しなさい。

【クラス図】
別紙参照

【実行結果】
氏名: 近藤勇
職業: 教員
担当科目: Go言語

氏名: 沖田総司
職業: シェフ
得意料理: オムライス
"""
class Person:
    def __init__(self, name, job):
        self.name = name
        self.job = job
    
    def introduce(self):
        print(f'氏名:{self.name}')
        print(f'職業:{self.job}')
    
class Teacher(Person):
    def __init__(self, name, job, subject):
        super().__init__(name, job)
        self.subject = subject
    
    def introduce(self):
        super().introduce()
        print(f'担当科目:{self.subject}')
    
class Cook(Person):
    def __init__(self, name, job, specialities):
        super().__init__(name, job)
        self.specialities = specialities 
    
    def introduce(self):
        super().introduce()
        print(f'得意料理:{self.specialities}')

A = Teacher('近藤勇', '教員', 'Go言語')
B = Cook('沖田総司', 'シェフ', 'オムライス')
A.introduce()
print()
B.introduce()