#Example of inbuilt polymorphic functions :

print(len("Riyaz"))
print(len([1,2,3,4,5,6,7,8,9,10]))

#Examples of used defined polymorphic functions :
def add(x,y,z=0):
  return x + y + z

print(add(5,4))
print(add(4,3,1))

#Polymorphism with class methods:
class India(): 
    def capital(self): 
      print("New Delhi is the capital of India.") 
  
    def language(self): 
      print("Hindi is the most widely spoken language of India.") 
  
    def type(self): 
      print("India is a developing country.") 
  
class USA(): 
    def capital(self): 
     print("Washington, D.C. is the capital of USA.") 
  
    def language(self): 
      print("English is the primary language of USA.") 
  
    def type(self): 
      print("USA is a developed country.") 
obj_ind = India() 
obj_usa = USA()
for country in (obj_ind, obj_usa): 
  country.capital() 
  country.language() 
  country.type()  
print()

#Polymorphism with Inheritance:

class Bird: 
  def intro(self): 
    print("There are many types of birds.") 
      
  def flight(self): 
    print("Most of the birds can fly but some cannot.") 
    
class sparrow(Bird): 
  def flight(self): 
    print("Sparrows can fly.") 
      
class ostrich(Bird): 
  def flight(self): 
    print("Ostriches cannot fly.") 

obj_bird = Bird() 
obj_spr = sparrow() 
obj_ost = ostrich() 

obj_bird.intro() 
obj_bird.flight() 
print()

obj_spr.intro() 
obj_spr.flight() 
print()

obj_ost.intro() 
obj_ost.flight() 
print()

#Polymorphism with a Function and objects:
class India(): 
    def capital(self): 
      print("New Delhi is the capital of India.") 
  
    def language(self): 
      print("Hindi is the most widely spoken language of India.") 
  
    def type(self): 
      print("India is a developing country.") 
  
class USA(): 
    def capital(self): 
     print("Washington, D.C. is the capital of USA.") 
  
    def language(self): 
      print("English is the primary language of USA.") 
  
    def type(self): 
      print("USA is a developed country.") 
def func(obj):
  obj.capital()
  obj.language()
  obj.type()

obj_ind=India()
obj_usa=USA()
func(obj_ind)
print()
func(obj_usa)
