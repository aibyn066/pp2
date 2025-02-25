a = input()
b = ""
i = 0
while i<len(a):
    if a[i] == "_":
        if i+1 < len(a):
            b+= a[i+1].upper()
        i+=1
    else:
        b+=a[i]
        
    i+=1

print(b)
        


