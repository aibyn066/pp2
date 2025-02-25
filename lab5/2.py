import re
txt = input()
x = re.findall(r'a[b]*',txt)
print(x)

x = re.findall(r'a[b]{2,3}',txt)
print(x)

x = re.findall(r'[a-z]_[a-z]',txt)
print(x)

x = re.findall(r'[A-Z]_[a-z]',txt)
print(x)

x = re.findall(r'\ba*b\b',txt)
print(x)

x = re.sub(r'[,. ]',':',txt)
print(x)


