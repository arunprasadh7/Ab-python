# 3 Book Details 
# title, author, price 
# show_details()

class BookDetail:
    
    def __init__(self,title,author,price):
        self.title = title
        self.author = author
        self.price = price
        
    
    def show_details(self):
        title = f'Title : {self.title}.'
        author = f'Author : {self.author}'
        price = f'Price : {self.price}'
        
        return f'{title} \n{author} \n{price}'
    
b1 = BookDetail('HarryPotter','JK Rowling', '500')
print(b1.show_details())