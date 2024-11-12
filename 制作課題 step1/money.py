from copy import deepcopy
class Money:
    def __init__(self, balance):
        self.balance = balance
        self.history = []
    
    def set_withdrawal(self, subject, money):
        if self.balance < money:
            return False
        else:
            self.balance -= money
            self.history.append('出金')
            self.history.append(subject)
            self.history.append(money)
            return True
    
    def set_payment(self, subject, money):
        self.balance += money
        self.history.append('入金')
        self.history.append(subject)
        self.history.append(money)
    
    def get_history(self):
        history_deepcopy = deepcopy(self.history)
        return history_deepcopy

    def get_balance(self):
        return self.balance