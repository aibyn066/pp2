import re
a = 'HelloWorld'

x = re.sub(r'([a-z])([A-Z])', r'\1 \2', a)
print(x)