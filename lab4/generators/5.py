"""
Реализуйте генератор, который возвращает все числа от (n) до 0.
"""

def gener(n):
    for x in range(n+1):
        yield x

a = int(input())
ads = []
for rand in gener(a):
    ads.append(str(rand))

ads.reverse()
print(", ".join(ads))
