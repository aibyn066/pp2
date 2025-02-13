'''
Напишите программу с использованием генератора, которая
выведет чётные числа от 0 до n через запятую, где n вводится с консоли.
'''
def even_numb(n):
    for x in range(n+1):
        if x%2==0:
            yield x

a = int(input())
abs = []
for ans in even_numb(a):
    abs.append(str(ans))

print(", ".join(abs))

