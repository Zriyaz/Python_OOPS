class Person(object):
  def __init__(self,name):
    self.name=name
  
  def getName(self):
    return self.name
  
  def isEmployee(self):
    return False

class Employee(Person):
  
  def isEmployee(self):
    return True

emp=Person("Riyaz")
print(emp.getName(),emp.isEmployee())
emp1=Employee("Kazmi")
print(emp1.getName(),emp1.isEmployee())

#How to check if a class is subclass of another?
class Base(object):
  pass #Empty class


class Derived(Base):
  pass #empty class

print(issubclass(Derived, Base)) 
print(issubclass(Base, Derived)) 
b=Base()
d=Derived()

# b is not an instance of Derived 
print(isinstance(b, Derived)) 
  
# But d is an instance of Base 
print(isinstance(d, Base)) 
