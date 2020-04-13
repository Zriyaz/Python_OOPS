class Myclass:
  RollNumber=0
  Name=" "
def Main():
  My_Object=Myclass()
  My_Object.RollNumber=14
  My_Object.Name="Md Riyaz Ansari"
  print(My_Object.Name + " " + str(My_Object.RollNumber))
if (__name__ == '__main__'):
  Main()
