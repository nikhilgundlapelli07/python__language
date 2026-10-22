def add(x, y):         
    return x + y 
print(add(10,20))       
print(type(add))       

a = lambda x,y : x + y   
print(a(10,20))        
print(type(a))        

b = lambda x,y: x + y 
print(b(10,20)) 

c = lambda x,y :  x + y 
print(c(10,20))

# lambda function to return the sum of two numbers
# lambda function to return the square of a number
# lambda function to return the second element of a sequence

#tricky
a = lambda x : print(x+10), print(200), print(300)
print(a)       
print(type(a)) 

#map 
a = [1,2,3,4,5,6]
m = map(lambda x : x**2, a) 
print(m) 
print(type(m))
l = list(m)     #1 4 9 16 25 36
print(l)

#filter 
a = [1,2,3,4,5,6]
f = filter(lambda x : x % 2 == 0, a)
print(f)
print(type(f))
l = list(f)
print(l)

#reduce 
import functools 
l = [1,2,3,4,5]
r = functools.reduce(lambda x,y : x+y, l) 
print(r)         
print(type(r))