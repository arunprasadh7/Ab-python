# Abstract class and interface 
# we cannot directly create an object for abstract class 
# to share some code and forcing child methods to overide them 
# abstract class may have some concrete method and abstract method
# interface only has abstract method that the child can overide 
# concrete - method having some body 


from abc import ABC,abstractmethod

class Parent(ABC):
    
    @abstractmethod
    def show(self): #method with no body
        pass
    
    def display(self):  #concrete - method with body
        print('Parent display')
        

# creating child class 
class Child(Parent):
    def show(self):
        print('Shown from Child class')
        

c1 = Child()
c1.show()
c1.display()

