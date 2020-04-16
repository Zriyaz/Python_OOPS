  
#Example of default constructor :
class Test:
  name=""
  def __init__(self): # default constructor 
    self.name="Md Riyaz Ansari"
  
  def Print(self):
    print("Name : " , self.name)

obj=Test()
obj.Print()


#Example of parameterized constructor :
class Test:
  first=0
  second=0
  ans=0
  def __init__(self,f,s):
    self.first=f
    self.second=s
  def Display(self):
    print("First number = " + str(self.first)) 
    print("Second number = " + str(self.second)) 
    print("Addition of two numbers = " + str(self.ans))
  def Calculate(self):
    self.ans=self.first + self.second

obj =Test(100,200)
obj.Calculate()
obj.Display()



