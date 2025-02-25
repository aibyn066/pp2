import re
#HelloWorld
#Hello_World

import re
a = input()
b = ""
i = 1
b+=a[0]
while(i<len(a)):
    
    if ord(a[i])>=65 and ord(a[i])<=90:
        b += '_'
        b += a[i]
    else:
        b+=a[i]
    i += 1

print(b)

    
        




