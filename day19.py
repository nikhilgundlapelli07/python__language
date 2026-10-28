#opening (path relative to command prompt)
f = open('a.txt', 'w')

#closing
with open('a.txt', 'w') as f:
   print(f.closed)        #False
print(f.closed)           #True 
print()

#write
f = open('a.txt', 'w')
f.write('ab')
f.write('c\n')
f.write('d\ne\nf')

#writelines
f = open('b.txt', 'w')
f.writelines('Guntur')  
# f.writelines('Guntur', 'Hyderabad', 'Vizag') 
f.writelines(('Guntur', 'Hyderabad', 'Vizag')) 
f.writelines(['Guntur\n', 'Hyderabad\n', 'Vizag\n'])  

#read
f = open('a.txt', 'r')    
print(f.read()) 
print(f.read(4)) 
f = open('a.txt', 'r')
print(f.read(5)) 
print(f.read())

#readline
f = open('c.txt', 'w+') 
f.writelines(['abc\n', 'def\n', 'ghi\n']) 
print(f.readline(), 'end')    
f = open('c.txt', 'r') 
print(f.readline(), 'end')  
print(f.readline(2), 'end')  
print(f.readline(10), 'end')  
print(f.readline(), 'end')  
 
# readlines
f = open('d.txt', 'w+') 
f.writelines(['abc\n', 'def\n', 'ghi\n', 'jkl'])
f = open('d.txt', 'r')
print(f.read(1))
print(f.readlines(4))
print(f.readlines(2))  
print(f.readlines(0))   

# for loop
f = open('e.txt', 'w')
f.writelines(['abc\n', 'def\n', 'ghi\n', 'jkl'])
f = open('e.txt', 'r')
print(next(f))  
for x in f:
    print(x)