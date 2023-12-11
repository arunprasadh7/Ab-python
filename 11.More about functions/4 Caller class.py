# Caller class

# demo with classes 
class Department:
  
  def __init__(self):
    self.depts = {
      'hr' : 'Human Resources',
      'acc' : 'Accounts & Finance',
      'sd' : 'Sales & Distribution',
      'mkt' : 'Marketing'
    }
  
  def __call__(self,dept) :
    print('This method will be auto called on function call')
    return self.depts[dept]


d1 = Department()

print(d1('hr'))
print(d1('acc'))
print(d1('sd'))
print(d1('mkt'))

# caller function without classes

def departments():
  depts = {
      'hr' : 'Human Resources Department',
      'acc' : 'Accounts & Finance Department',
      'sd' : 'Sales & Distribution Department',
      'mkt' : 'Marketing Department'
    }
  
  def dname(dept):
    return depts[dept]
  
  return dname

n = departments()

n1 = n('hr')
print(n1)

print(n('acc'))
print(n('sd'))
print(n('mkt'))