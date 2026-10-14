

# Set Methods 
#add 
s = set()
s.add(1)
s.add(1.6)
s.add(2+3j)
s.add(True)
s.add(None)
s.add((4,5,6))
s.add('rakesh')
s.add(range(13,16))
print(s)

#update
s = set()
s.update([1,2,3])
s.update((4,5,6))
s.update({7,8,9})
s.update({10:'a', 11:'b', 12:'c'})
s.update('rakesh')
s.update(range(13,16))
print(s)

#pop
s = {1,4,3,2,5,6,7,9}
print(s)
a = s.pop() 
print(a, s)
b = s.pop() 
print(b, s)

#remove
s = {4,3,2,5,8}
a = s.remove(8)
print(a, s)
print(b, s)

# discard
s = {4,3,2,5,8}
a = s.discard(8)
print(a, s)
b = s.discard(9)
print(b, s)

# clear
s = {4,3,5,2,1}
a = s.clear()
print(a, s)

# union, intersection, differece, symmetric_difference
s = {1,2,3,4}
l = [3,4,5,6]
t = (3,4,5,6)
s2 = {3,4,5,6}
d = {3:'c', 4:'d', 5:'e', 6:'f'}
r = range(3,7)
w = '3456'
print('Union:', s.union(l))
print('Intersection:', s.intersection(t))
print('Difference:', s.difference(s2))
print('Symmetric Difference:', s.symmetric_difference(d))
print('Union:', s.union(w))
print('Union:', s.union(r))


# Dict Methods 
d = {}
d.update({10:'j', 11:'k', 12:'l'})
print(d)
d.update([ [1,'a'], (2,'b'), 'ab' ])
print(d)
d.update(( 'ra', 'ke', 'sh' ))
print(d)
d.update({ (3,'c'), (4,'d') })
print(d)

# #pop 
d = {3:'c', 2:'b', 1:'a', 4:'d'}
x = d.pop(2)
print(x)
z = d.pop(100, -1)
print(z)

#popitem
d = {3:'c', 2:'b', 1:'a', 4:'d'}
x = d.popitem()
print(x, d) 
y = d.popitem()
print(y, d)

#clear
d = {3:'c', 2:'b', 1:'a', 4:'d'} 
d.clear() 
print(d)

#get 
d = {3:'c', 2:'b', 1:'a', 4:'d'}
x = d.get(2)
print(x, d)
y = d.get(100)
print(y, d)
z = d.get(100, -1)
print(z, d)

#setdefault
d = {3:'c', 2:'b', 1:'a', 4:'d'}
x = d.setdefault(2, 90)
print(x, d)
y = d.setdefault(100)
print(y, d)
z = d.setdefault(90, -1)
print(z, d)
m = d.setdefault(90, -2)
print(m, d)

#keys, values, items
d = {3:'c', 2:'b', 1:'a', 4:'d'}
dk = d.keys()
print(dk, type(dk))
dv = d.values()
print(dv, type(dv))
di = d.items() 
print(di, type(di))