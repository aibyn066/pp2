'''
Input number of sides: 4
Input the length of a side: 25
The area of the polygon is: 625
'''
import math

print("Input number of sides:")
s = int(input())
print("Input the length of a side:")
l = int(input())

area = (s*l**2)/(4*math.tan(math.pi/s))
print("The area of the polygon is:" + str(area))


