class Person():
  def __init__(self,name):
    self.name=name
  
  def getName(self):
    return self.name
  def isEmployee(self):
    return False

class Employee(Person):

  def __init__(self,name,Eid):
    super(Employee,self).__init__(name)
    self.Eid=Eid
  def isEmployee(self):
    return True
  
  def getId(self):
    return self.Eid

emp=Employee("Md Riyaz Ansari","18MCR014")
print(emp.getName(),emp.isEmployee(),emp.getId())