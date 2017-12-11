import math
a = input("enter the side a: ")
b = input("enter the side b: ")
c = input("enter the side c: ")
s = (a+b+c)/2
area = math.sqrt(s*(s-a)*(s-b)*(s-c))
print "Area of the traingle is" +str(area)