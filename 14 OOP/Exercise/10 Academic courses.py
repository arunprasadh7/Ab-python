# 10 Acadedmic courses 
# inner and outer class 

class Course:
    
    def __init__(self,name,duration,*books):
        self.name = name
        self.duration = duration
        
        self.books = [self.Book(b) for b in books]
        
    def show_details(self):
        print('Name :',self.name)
        print('Duration(days) :',self.duration)
        print('Suggested books !!')
        
        for b in self.books:
            print(b)
            
            
    class Book:
        def __init__(self,title):
            self.title = title
        
        def __str__(self):
            return self.title
        
c1 = Course('Python',90, 'Core python', 'Python Django','Python Flask')
c1.show_details()

c2 = Course('Java',45,'Java Core','Java Springboot')
c2.show_details()