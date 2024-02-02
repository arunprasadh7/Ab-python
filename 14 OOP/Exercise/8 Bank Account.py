# 8 Bank Account 

class MinimumBalanceError(Exception):
    pass

class Account(MinimumBalanceError):
    
    acc_number = 1001
    
    def __init__(self,name,balance):
        if balance < 1000:
            raise MinimumBalanceError('Account cannot be created')
        self.name = name
        self.balance = balance
        self.acc_number = Account.acc_number
        Account.acc_number += 1
        
    def deposit(self,amt):
        self.balance += amt
        return f'Deposit successful. Your current balance is {self.balance}'
        
        
    def withdraw(self,amt):
        total = self.balance - amt
        if total < 1000:
            raise MinimumBalanceError('Minimum balance is 1000.')
            
        return f'Withdrawl of {amt} successful. You\'re current balance is {total}'
    
    def show_details(self):
        return f'Name : {self.name} \nAcc Number : {self.acc_number} \nBalance : {self.balance}'
    

a1 = Account('Arun',6000)
a1.deposit(500)
print(a1.withdraw(1000))
print(a1.show_details())

a2 = Account('Storm', 5000)
print(a2.show_details())