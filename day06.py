# #append()
l = ['a', 'b', 'c']
l.append(34)
l.append(34.3)
l.append(4+3j)
l.append(True)
l.append(None)
l.append([0,1,2])
l.append((3,4,5))
l.append({6,7,8})
l.append({9:'a', 10:'b', 11:'c'})
l.append('rakesh')
l.append(range(12,15))
print(l)

# extend() 
l = ['a', 'b', 'c']
l.extend
l.extend([0,1,2])
l.extend((3,4,5))
l.extend({6,7,8})
l.extend({9:'a', 10:'b', 11:'c'})
l.extend('rakesh')
l.extend(range(12,15))
print(l)

# insert() 
#positive index
l = ['a', 'b', 'c', 'd']
l.insert(2, 'hi')
print(l)
l.insert(10, 'hi')
print(l)

#negative index
l = ['a', 'b', 'c', 'd', 'e']
l.insert(-2, 'hi')
print(l)
l.insert(-100, 'hi')
print(l)

#pop()
l = [1, 2, 3, 4, 5]
a = l.pop()
print(a, l)
b = l.pop(2)
print(b, l)
del l[0]
print(l)

# remove()
l = [1, 2, 3, 4]
a  = l.remove(3)
print(a, l)

# clear()  
l = [1, 2, 3, 4, 5]
l.clear()
print(l)

# reverse() 
l = [1, 2, 3, 4, 5]
print(id(l))
a = l.reverse()
print(a, l)
print(id(l))

# sort()  
l = [1,4,2,6,5,3]
print(id(l))
a = l.sort() 
print(a, l)
print(id(l))
l = [50,10,40,20,30]
print(l.sort(reverse=True))
print(l)


# index() 
l = [1, 2, 1, 4, 6, 1, 7]
print(l.index(1))
print(l.index(1, 3))


# count() 
l = [1, 2, 1, 4, 1, 6, 7, 1]
print(l.count(1))
print(l.count(9))


# index() 
l = (1, 2, 1, 4, 6, 1, 7)
print(l.index(1))
print(l.index(1, 3))

# count() 
l = (1, 2, 1, 4, 1, 6, 7, 1)
print(l.count(1))
print(l.count(9))