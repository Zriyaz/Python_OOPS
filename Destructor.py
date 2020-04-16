# Destructor in Python
# Python program to illustrate destructor 
class Employee: 
  
    # Initializing 
    def __init__(self): 
      print('Employee created.') 
  
    # Deleting (Calling destructor) 
    def __del__(self): 
      print('Destructor called, Employee deleted.') 
  
obj = Employee() 
del obj 

'''Note : The destructor was called after the program ended or when all the references to object are deleted i.e when the reference count becomes zero, not when object went out of scope.'''

class Employee: 
  
    # Initializing  
    def __init__(self): 
      print('Employee created') 
  
    # Calling destructor 
    def __del__(self): 
      print("Destructor called") 
  
def Create_obj(): 
  print('Making Object...') 
  obj = Employee() 
  print('function end...') 
  return obj 
  
print('Calling Create_obj() function...') 
obj = Create_obj() 
print('Program End...') 


class A: 
  def __init__(self, bb): 
    self.b = bb 
  
class B: 
  def __init__(self): 
    self.a = A(self) 
  def __del__(self): 
    print("die") 
  
def fun():
  b = B() 
  
fun() 