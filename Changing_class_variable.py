
#changing the class variable using object
class CSStudent: 
  stream = 'cse'     # Class Variable  
  def __init__(self, name, roll): 
    self.name = name  
    self.roll = roll 

a = CSStudent("Md Riyaz", 14) 
b = CSStudent("Ritesh", 13)

print("Initially")
print("a.stream =", a.stream) 
print("b.stream =", b.stream)

# This thing doesn't change class(static) variable 
# Instead creates instance variable for the object 
# 'a' that shadows class member. 
a.stream = "MCA"

print("\nAfter changing a.stream")
print("a.stream =", a.stream)
print("b.stream =", b.stream)


#changing the class variable using Class name
class CSStudent: 
  stream = 'cse'     # Class Variable  
  def __init__(self, name, roll): 
    self.name = name  
    self.roll = roll 

print("how to make changes to the class variable in Python ")
a = CSStudent("Riyaz", 14) 
print ("a.tream =", a.stream)
# Correct way to change the value of class variable 
CSStudent.stream = "MCA"
print ("\nClass variable changes to mec")
b = CSStudent("Ritesh", 13)

print ("\nValue of variable steam for each object")
print ("a.stream =", a.stream) 
print ("b.stream =", b.stream) 