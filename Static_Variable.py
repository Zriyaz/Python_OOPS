class CSStudent: 
  stream = 'css'                  # Class Variable or Static variable 
  def __init__(self,name,roll): 
    self.name = name            # Instance Variable 
    self.roll = roll            # Instance Variable 

a = CSStudent('Riyaz', 14) 
b = CSStudent('Ritesh', 13) 

print(a.stream)  # prints "cse" 
print(b.stream)  # prints "cse" 
print(a.name)    # prints "Riyaz" 
print(b.name)    # prints "Ritesh" 
print(a.roll)    # prints "14" 
print(b.roll)    # prints "13" 

print(CSStudent.stream) # prints "cse" 
