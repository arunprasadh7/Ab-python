# 7 Currency Converter 
# accessor and mutator  

class CurrencyConverter:
    
    amount = 100
    
    def __init__(self,currency,rate):
        self.currency = currency
        self.rate = rate
        
    def set_currency(self,currency):
        self.currency = currency
    
    def get_currency(self):
        return self.currency
    
    def get_rate(self):
        return self.rate
    
    def set_rate(self,rate):
        self.rate = rate
        

    def convert(self):
        return self.amount * self.rate
    

c1 = CurrencyConverter('usd',80)
print(c1.convert())

c1.set_currency('AUD')
c1.set_rate(50)
print(c1.get_currency())
print(c1.convert())