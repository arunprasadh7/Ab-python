# 4 Details of an Employee 

class EmployeeDetails:
    
    emp_id = 101
    
    def __init__(self,name,salary,designation):
        self.name = name
        self.emp_id = 'e' + str(EmployeeDetails.emp_id)
        self.salary = salary
        self.designation = designation
        
        EmployeeDetails.emp_id += 1
        
    
    def show_details(self):
        print(f'Employee name : {self.name}')
        print(f'Employee id : {self.emp_id}')
        print(f'Employee salary : {self.salary}')
        print(f'Employee designation : {self.designation}')
        
    @classmethod    
    def total_emp(cls):
        total = cls.emp_id - 101
        print(f'Total employee count : {total}')
        
e1 = EmployeeDetails('Invoker',5000,'Python Developer')
e2 = EmployeeDetails('Arc',10000,'Java Developer')
e3 = EmployeeDetails('Storm',8000,'C# Developer')

e1.show_details()
e2.show_details()
e3.show_details()

EmployeeDetails.total_emp()


