class Test:
  def __init__(self,a,b):
    self.a=a
    self.b=b;
  
  def __repr__(self):
    return "Test a:%s b:%s"% (self.a,self.b)
  
  def __str__(self):
    return " From str method of test : a:%s, b is  %s " % (self.a,self.b) 
obje=Test(120,240)
print(obje)
print([obje])

# define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str

car1 = Vehicle()
car1.name = "Fer"
car1.color = "red"
car1.kind = "convertible"
car1.value = 60000.00

car2 = Vehicle()
car2.name = "Jump"
car2.color = "blue"
car2.kind = "van"
car2.value = 10000.00

print(car1.description())
print(car2.description())  


