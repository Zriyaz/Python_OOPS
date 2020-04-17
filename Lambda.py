# lambda

def fun(n):return n**3
print(fun(5))

lam=lambda x:x**3
print(lam(5))

l=lambda p , y , z : p+y+z
print(l(1,2,3))

def write():
  title='Sir'
  name= (lambda x: title + ' ' + x )
  return name

who=write()
print(who('i am Riyaz'))

def f1(x): return x ** 2
def f2(x): return x ** 3 
def f3(x): return x ** 4
l=[f1,f2,f3]
for i in l:
  print(i(5))

min1=(lambda x,y:x if(x,y) else y)
print(min1(2,5))


