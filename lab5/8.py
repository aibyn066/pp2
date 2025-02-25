import re

a = 'HelloWorld'

x = re.findall(r'[A-Z][a-z]*',a)
print(x)