#multiple Inheritance
class Base1(object):
  def __init__(self):
    self.str1='Md'
    print("Base1")
class base2(object):

  def __init__(self):
    self.str2='Riyaz'
    print("Base2")
class Derived(Base1,base2):

  def __init__(self):
    Base1.__init__(self)
    base2.__init__(self)
    print("Derived")
  def printstr(self):
    print(self.str1,self.str2)

dobj=Derived() #derived Class Object
dobj.printstr()


#How to access parent members in a subclass?
class Base(object):
  def __init__(self,x):
    self.x=x

class Derived(Base):
  def __init__(self,x,y):
    Base.x=x
    self.y=y
  def printXY(self):
    print(self.x,self.y)#this will also print
    print(Base.x,self.y)

d=Derived(10 , 20)
d.printXY()

#Using super()
#We can also access parent class members using super.
class Base(object):
  def __init__(self,x):
    self.x=x

class Derived(Base):
  def __init__(self,x,y):
    #Base.x=x
    ''' In Python 3.x, "super().__init__(name)" 
            also works''' 
    super(Derived,self).__init__(x)
    self.y=y
  def printXY(self):
    print(self.x,self.y)
    # Note that Base.x won't work here 
    # because super() is used in constructor 
    #print(Base.x,self.y)

d=Derived(10 , 20)
d.printXY()

#Example Predict the Output 
class X(object): 
    def __init__(self, a): 
        self.num = a 
    def doubleup(self): 
        self.num *= 2
  
class Y(X): 
    def __init__(self, a): 
        X.__init__(self, a) 
    def tripleup(self): 
        self.num *= 3
  
obj = Y(4) 
print(obj.num) 
  
obj.doubleup() 
print(obj.num) 
  
obj.tripleup() 
print(obj.num) 










