#local, global variable
a = 1
def f1():
    b = 2
    print(a)     
    print(b)    
def f2():
    c = 2 
    print(a)  
    print(c)  
f1()
f2()
print(a)               

#call by value, call by reference
# call by value 
def f1(a):
    a = 100
a = 4
f1(a)
print(a)      

#call by reference
def f2(a):
    a = [10, 20, 30]
    a[2] = 200
a = [1, 2, 3]
f2(a)
print(a)    

def f3(a):
    a[2] = 200
a = [1, 2, 3]
f3(a)
print(a)    

