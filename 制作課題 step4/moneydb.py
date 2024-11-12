from moneytxt import MoneyTxt
from sqlmanager import SqlManager
class MoneyDB(MoneyTxt):
    def __init__(self, balance_path):
        self.balance_init(balance_path)
        self.history_init()
    
    def history_init(self):
        #try:
        self.A = SqlManager()
        self.history = self.A.select_all()
        #except:
            #self.history = []
    
    def save(self):
        super().save()
        self.A.insert_all(self.history)