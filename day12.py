def add(a, b):
    print('add function')
    c = a + b 
    return c 
    pirnt('HI')
def sub(a, b):
    print('sub function')
    c = a - b
    return 
def div(a, b):
    print('div function')
    c = a / b 
x = add(10, 15)   
y = sub(20, 10)   
z = div(25, 10)   
print(x)
print(y)
print(z)
print()

# #Type of arguments
def detail(name, age, rollno):
    print(f'My name is {name}')
    print(f'My age is {age}')
    print(f'My rollno is {rollno}')
detail('rakesh', 20, 'A101')
detail(20, 'A101', 'rakesh')
detail(age=20, rollno='A101', name='rakesh')
detail(rollno='A101', age=20, name='rakesh')
def add(a, b=10, c=20):
    return a + b + c 
print(add(1))
print(add(1,2))
print(add(1,2,3))
print(add(c=3, a=1, b=2))

