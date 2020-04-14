from datetime import date
class Person:
  def __init__(self,name,age):
    self.name=name
    self.age=age

  @classmethod
  def FromBirthYear(cls,name,year):
    return(cls,date.today().year-year)
  
  @staticmethod
  def isAdult(age):
    return age > 18

person1=Person("Riyaz", 1995)
person2=Person("Abdul",2011)

print(person1.age,person1.name)
print(person2.age,person2.name)

print(person1.isAdult(22))
print(person2.isAdult(12))


