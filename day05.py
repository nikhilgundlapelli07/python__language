#strip, lstrip, rstrip
a = '   python   '
b = a.strip()       
c = a.lstrip()
d = a.rstrip()
print(a, len(a))  
print(b, len(b))   
print(c, len(c))  
print(d, len(d))   

# #replace
a = 'python is simple, python is easy to learn, python is all rounder'
b = a.replace('python', 'java')
print(a)  
print(b)  

# #upper, lower, swapcase, title, capitalize
a = 'PYTHON is simple, PYTHON is easy to LEARN'
b = a.lower()
c = a.upper()
d = a.swapcase()
e = a.title()       
f = a.capitalize()   
print('original', a)       
print('lower:', b)         
print('upper:', c)         
print('swapcase:', d)      
print('title:', e)         
print('capitalize:', f)    

#count, startswith, endswith
s = 'python is python'
print(s.count('th'))      
print(s.startswith('py'))   
print(s.endswith('onn'))   
 
#find, index: 
#    0123456789 
s = 'abdcdefdgh'
print(s.find('d'))          
print(s.find('d', 5))       
print(s.find('d', 5, 7))   
print(s.index('d'))        
print(s.index('d', 5))      
print()
print()

#rfind, rindex
#    0123456789 
s = 'abdcdefdgh'
print(s.rfind('d'))          
print(s.rfind('d', 5))       
print(s.rfind('d', 5, 7))   
print(s.rindex('d'))        
print(s.rindex('d', 5))     
 
 

#isalpha: 
a = 'aBcD'
b = 'abc1'
c = ''
print(a.isalpha())  
print(b.isalpha()) 
print(c.isalpha())  
print() 
print()

#isdigit
a = '123'
b = '12.3'
c = '-123'
print(a.isdigit()) 
print(b.isdigit())  
print(c.isdigit()) 
print() 
print()

#isalnum: 
a = 'Abc123'
b = 'Abc@123'
c = ' '
print(a.isalnum())  
print(b.isalnum())  
print(c.isalnum())  
print()
print()

#isupper: 
a = 'ABC@123'
b = '123'
c = 'ABC123a'
print(a.isupper()) 
print(b.isupper())  
print(c.isupper())  
print()
print()

#islower: 
a = 'abc@123'
b = '123'
c = 'abc123A'
print(a.islower()) 
print(b.islower())  
print(c.islower()) 

#split
s = 'abaca'
print(s.split('a'))   
s = '   '
print(s.split(' '))  
print(s.split())    
  
# #join
a = [1,2,3,4]
b = ['1', '2', '3']
print('@'.join(b))