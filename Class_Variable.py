class Student:
  Stream="MCA" #class variable 

  def __init__(self,name,roll): 
    #instance variables
    self.name=name
    self.roll=roll
  def details(self):
    print("Name :",self.name)
    print("Roll No. :",self.roll)
    print("Branch : ",self.Stream)

  
a=Student("Riyaz","18mcr014")
b=Student("Ritesh","18mcr013")
a.details()
b.details()
#direct access class varibale
print(a.Stream)
print("Class Variable")
#how to create Empty class
class Empty:
  pass
