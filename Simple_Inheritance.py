class pet:
  def __init__(self,name,age):
    self.name=name
    self.age=age
class cat(pet):
  def __int__(self,name,age):
    super().__init__(name,age)
def Main():
  thepet=pet("pet",1)
  jess=cat("jess",3)
  print("Is jess a cat? " +str(isinstance(jess, cat))) 
  print("Is jess a pet? " +str(isinstance(jess, pet))) 
  print("Is the pet a cat? "+str(isinstance(thepet, cat))) 
  print("Is thePet a Pet? " +str(isinstance(thepet, pet))) 
  print(jess.name)
if(__name__=='__main__'):
  Main() 