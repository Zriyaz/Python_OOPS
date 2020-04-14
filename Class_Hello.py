class Test:
  def fun(self):
    print("Hello")

obj=Test()
obj.fun()

#self is not a keyword
class Test:
  def fun(hi):
    print("Hello")

obj=Test()
obj.fun()

#__init__ is a constructor
#Passing Arguments in user_defined function
class Test:
  def fun(self,name,Roll):
    self.name=name
    self.Roll=Roll
    print("Hello ,",self.name, " \n" + str(self.Roll))

obj=Test()
obj.fun("Riyaz Ansari","18MCR014")

#__init__ is a constructor
class Test:
  def __init__(self,name,Roll):
    self.name=name
    self.Roll=Roll
    print("Hello , ",self.name, " \n" + str(self.Roll))
  def myfun(self):
    print("bye Riyaz\nSee you later")

obj=Test("Riyaz Ansari","18MCR014")
obj.myfun()

