
 
#Datatypes



#Integer
n = 123
print(n)         
print(type(n))   
a = 123        
a = 0b1011
b = 0o761
c = 0xF109
print(a)         
print(type(a))   
print(b)         
print(type(b))   
print(c)         
print(type(c))   

#Float
a = 12.34
b = 12.34e2
c = 12.34e-2
print(a, type(a))  #12.35 <class 'float'>
print(b, type(b))  #1234.0 <class 'float'>
print(c, type(c))  #0.1234 <class 'float'>

#Complex
a = 3 + 4j
b = 0j
c = 7
print(a, type(a), type(a.real), type(a.imag))
print(b, type(b), type(a.imag)) 
print(c)

#Bool
a = True
b = False
print(type(a))
print(type(b))
c = a + b 
print(c)
print(type(c))

#NoneType
a = None
print(a)
print(type(a))

#List
a = []
b = list() 
c = [1,2,3,4,5]
e = list((1,2,3,4,5))
f = list('rakesh')
g = list(range(1,6))
h = list({1,2,3,4})
i = list({1:'a', 2:'b', 3:'c'})
print(a, type(a))
print(b)
print(c)
print(e)
print(f)
print(g)
print(h)
print(i)

#Tuple
a = (1,2,3,4,5)
b = 1,2,3,4
c = True, 1, 3j, None
d = (5.6)
e = (1+3j)
f = (1)
g = (True)
h = (3j)
i = 1,
j = True,
k = 3j,
l = tuple() 
n = tuple([2,3,4])
o = tuple({4,5,6})
p = tuple({1:'a', 2:'b', 3:'c'})
q = tuple(range(1,6))
r = tuple('rakesh')
print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))
print(e, type(e))
print(f, type(f))
print(g, type(g))
print(h, type(h))
print(i, type(i))
print(j, type(j))
print(k, type(k))
print(type(l))
print(n)
print(o)
print(p)
print(q)
print(r)

#Set 
a = {}
b = set() 
c = {1,2,3,4}
d = {1,1,2,2,2,3,3,3,4,4,4,4}
h = {(1,2,3), 4, True} 
i = {'rakesh', 4, True}
k = set([1,2,2,3,3,3])
l = set((4,4,5,5,6,6))
m = set({1:'a', 1:'b', 1:'c'})
n = set('rraakkeesshh')
o = set(range(1,6))
print(a, type(a))
print(b, type(b))
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(i)
print(j) 
print(k)
print(l)
print(m)
print(n) 
print(o)

#Dict 
a = {}
b = dict() 
c = {1,2,3,4,5}
d = {1:'a', 2:'b', 3:'c', 4:'d'}
g = {'rakesh':'a', 2:'b'}
h = {(1,2,3):'a', 2:'b'}
i = {1:'a', 1:'b', 1:'c', 2:'x', 2:'y'}
# k = dict(1:'a', 2:'b')
l = dict({1:'a', 2:'b'})
m = dict([(1,2), [3,4], (5,6)])
n = dict( ((1,2),[3,4])) 
print(a, type(a))
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(i)
print(j)
print(k)
print(l)
print(m)
print(n)

#String
a = 'rakesh'
b = "rakesh"
c = '''r
a
k
esh'''
print(a)
print(type(a))
print(b)
print(type(b))
print(c)
print(type(c)) 

#Range
a = range(5)
b = range(3,7)
c = range(3, 9, 2)
d = range(9,3,-1)
print(a)
print(*a)
print(*b)
print(*c)
print(*d)

#Slicing
a = [4,1,2,3,5] 
print(a[:])
print(a[:3])
print(a[2:])
print(a[::-1])
print(a[:3:-1])
print(a[3::-1])
b = {3,2,4,6}
c = {1:'a', 2:'b', 3:'c'}
