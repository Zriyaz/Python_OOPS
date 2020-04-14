class Hide_info:
  password="code24"

myobj=Hide_info()
print(myobj.password) # output : code24

# how to Access Private class Variable
class Hide_info:
  __password="code24"

myobj=Hide_info()
print(myobj._Hide_info__password) #Oputput: code24
class MyClass: 

	# Hidden member of MyClass 
	__hiddenVariable = 0
	
	# A member method that changes 
	# __hiddenVariable 
	def add(self, increment): 
		self.__hiddenVariable += increment 
		print (self.__hiddenVariable) 

# Driver code 
myObject = MyClass()	 
myObject.add(2) 
myObject.add(5) 

# This line causes error 
print (myObject.__hiddenVariable) 





