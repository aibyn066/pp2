import re

txt = 'Abc Adbmy,nikra.abb dkawf abb abbb awdawd a_b_c_d aabbcc aa acb'
#1
x = re.findall(r'a[b]*', txt)
print(x)
#2
x = re.findall(r'a[b]{2,3}', txt)
print(x)
#3
x = re.findall(r'\w[_]+\w',txt)
print(x)
#4
x = re.findall(r'\b[A-Z][a-z]*\b',txt)
print(x)
#5
x = re.findall(r'\ba\w*b\b',txt)
print(x)
#6
x = re.sub(r'[{}., ]',':',txt)
print(x)
#8
txt = 'HelloWorldExample'
x = re.findall(r'[A-Z][a-z]*',txt)
print(x)
#9
x = re.sub(r'([A-Z])', r' \1',txt)
print(x)