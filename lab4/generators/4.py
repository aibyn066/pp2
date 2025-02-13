"""
Реализуйте генератор под названием squares для вычисления квадратов всех чисел от (a) до (b). 
Протестируйте его с помощью цикла «for» и выведите каждое полученное значение.
"""

def squares(n,k):
    for x in range(n,k+1):
        yield x*x

a = int(input())
b = int(input())

for gen in squares(a,b):
    print(gen)



