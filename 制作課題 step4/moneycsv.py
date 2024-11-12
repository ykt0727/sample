from moneytxt import MoneyTxt
from filecsv import FileCsv
class MoneyCsv(MoneyTxt):
    def __init__(self, balance_path, history_path):
        self.balance_init(balance_path)
        self.history_init(history_path)
    
    def history_init(self, history_path):
        try:
            self.fileCsv = FileCsv(history_path)
            self.history = self.fileCsv.get_csv()
        except:
            self.history = []
        
    def save(self):
        super().save()
        self.fileCsv.set_csv(self.history)