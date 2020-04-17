#% operator

print("I am using %s %d.%d" %('python',3,2))

m = 9.876543210
print('%e %E %f %g'%(m,m,m,m))

#convert string
print('%s' %m ,str(m))

#precision
print('%.1f , %.3f' %(m,m))

# date and Time 

t='{0},{1},{2}'
print(t.format('Apral',"17","2020"))

t='{Month},{Day},{Year}'
print(t.format(Month='April',Day='17',Year='2020'))

# String Method 
s='black holes are where God divided by zero'
s2='simple.txt'
print(s.capitalize())
print(s.center(50,'*'))

print(s.count('i'))
print(s.count('hole'))
a=list(map(s.count,s))
print(a)

print(s.endswith('txt'))
print(s2.endswith('txt'))

S = 'aaaaaSPYbbbbSPYcccc'
print(S.find('SPY'))

alpha='abc123'
print(alpha.isalnum())
alpha='abcde'
print(alpha.isalnum())
alpha='abc def'
print(alpha.isalnum())

alpha='abc'
print(alpha.isalpha())
alpha='abc2'
print(alpha.isalpha())

d='123'
print(d.isdigit())
d='123b'
print(d.isdigit())
l='abc'
print(l.islower())
l='ABC'
print(l.islower())

sp='1riyaz  ansari'
print(sp.isspace())
#sp='mdriyaz'
#print(sp.isspace())
up='MD RIYAZ'
print(up.isupper())

seq=['a','b','c','d','e']
print(''.join(seq))
print('-'.join(seq))

print('-'.join(['x' for x in range(101)]))

u='MD RIYAZ ANSARI'
print(u.lower())
u='md riyaz ansari'
print(u.upper())

s='     too much left side space  '
print(s)
print(s.strip())
p='www.bogotobogo.com'
print(p.strip('w.'))


#Replace 
S = 'beetles'
S = S[:3] + 'xx' + S[5:]
print(S)
S = 'beetles'
print(S.replace('ee','xx'))



