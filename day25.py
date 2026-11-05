# import re

# # Match Object Methods
# text = 'abc123'
# match = re.search(r'\d+', text)
# print(match)             
# print(match.group())    
# print(match.start())    
# print(match.end())     
# print(match.span())     
# print()


# # Match Object group()
# text = 'Name: Rakesh, Age: 25'
# match = re.search(r'Name: (\w+), Age: (\d+)', text)
# print(match.group())  
# print(match.group(1))  
# print(match.group(2)) 
# print(match.groups()) 
# print()


# # re.match()
# match = re.match(r'abc', 'abcdef')
# print(match)         
# print(match.group()) 
# print()

# match = re.match(r'abc', 'xyzabc')
# print(match)         
# print()


# # re.search()
# match = re.search(r'abc', 'xyzabc123')
# print(match)        
# print(match.group())  
# print()


# # re.fullmatch()
# print(re.fullmatch(r'\d+', '12345'))  
# print(re.fullmatch(r'\d+', '123abc'))
# print()


# # re.findall()
# print(re.findall(r'\d+', '10 20 30'))       
# print(re.findall(r'[A-Z]', 'Python JAVA C++')) 
# print()


# # re.finditer()
# text = 'abc123 xyz456'
# for match in re.finditer(r'\d+', text):
#     print(match)
#     print(match.group())
#     print(match.start())
#     print(match.end())
#     print()


# # re.split()
# text = 'apple,banana;orange'
# print(re.split(r'[,;]', text)) 
# print()


# # re.sub()
# text = 'Python is easy. Python is powerful.'
# print(re.sub(r'Python', 'Java', text))  
# print()


# # re.subn()
# text = 'cat dog cat cat'
# print(re.subn(r'cat', 'lion', text)) 
# print()


# # re.compile()
# pattern = re.compile(r'\d+')
# print(pattern.search('abc123'))
# print(pattern.findall('10 20 30'))
# print()