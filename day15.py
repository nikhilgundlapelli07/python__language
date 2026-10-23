#List Comprehension
#for
a = []
for x in range(1, 11):
    a.append(x)
print(a)
#create with list comprehension

#for-if
a = []
for x in range(1,11):
    if x % 2 == 0:
        a.append(x) 
print(a)
#create with list comprehension

#for-if-for-if 
a = []
for x in range(1,5):
    if x % 2 == 0:
        for y in range(1,4):
            if x + y == 5:
                a.append((x,y))
print(a)
#create with list comprehension

#set comprehension: create a set with even numbers from 1 to 20
#dict comprehension: create a dict with numbers and their squares from 1 to 10 

#function
def numbers():
    return 1 
    return 2 
n = numbers()
print(n)
print(type(n))

#generators
def numbers():
    yield 1 
    yield 2 
    yield 3 
    yield 4 
n = numbers() 
print(n)
print(type(n))
print(next(n))
print(next(n))
print(n.__next__())
print(n.__next__())

def evennumbers():
    for x in range(1, 10):
        if x % 2 == 0:
            yield x 
n = evennumbers()
print(next(n))
print(n.__next__())
for x in n:
    print(x)