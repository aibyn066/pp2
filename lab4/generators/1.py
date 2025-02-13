def square_s(n):
    for x in range(0,n+1):
        yield x*x

a = int(input())

for sq in square_s(a):
    print(sq)