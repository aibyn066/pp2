'''
Определите функцию с генератором, которая может перебирать 
числа, кратные 3 и 4, в заданном диапазоне от 0 до n.

'''

def gener_crat(n):
    for x in range(n+1):
        if x%3==0 and x%4==0:
            yield x

a = int(input())

for gen in gener_crat(a):
    print(gen)

