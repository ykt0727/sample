from money import Money
from filetxt import FileTxt
class MoneyTxt(Money):
    def __init__(self, balance_path):
        self.balance_path = balance_path
        self.balance_init(self.balance_path)
    
    def balance_init(self, balance_path):
        self.A = FileTxt(balance_path)
        try:
            self.balance = int(self.A.get_txt())
        except:
            self.balance = int(input('残高を入力してください:'))
    
    def save(self):
        self.A.set_txt(self.balance)