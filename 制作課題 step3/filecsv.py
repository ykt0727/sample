from file import File
import csv
from copy import deepcopy
class FileCsv(File):
    def set_csv(self, lst):
        with open(self.path, 'w', encoding='utf-8', newline='') as f:
            csv.writer(f).writerows(lst)
    
    def get_csv(self):
        with open(self.path, encoding='utf-8') as f:
            reader = csv.reader(f)
            self.history = [row for row in reader]
            history_deepcopy = deepcopy(self.history)
            return history_deepcopy