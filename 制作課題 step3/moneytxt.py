from money import Money
from filetxt import FileTxt
class MoneyTxt(Money):
    def __init__(self, balance_path):
        self.balance_init(balance_path)
        self.history = []
    
    def balance_init(self, balance_path):
        try:
            self.fileTxt = FileTxt(balance_path)
            self.balance = int(self.fileTxt.get_txt())
        except:
            self.balance = int(input('残高を入力してください:'))
    
    def save(self):
        self.fileTxt.set_txt(self.balance)