
#http://www.dreamincode.net/code/snippet2911.htm
from math import *
n=input("Enter number of points:")
sum_x=0
sum_y=0
sum_xx=0
sum_xy=0
for i in range(1,n+1):
    print "For point %s"%i
    x=input("Enter x:")
    y=input("Enter y:")
    sum_x=sum_x+x
    sum_y=sum_y+y
    xx=pow(x,2)
    sum_xx=sum_xx+xx
    xy=x*y
    sum_xy=sum_xy+xy

#Calculating the coefficients
a=(-sum_x*sum_xy+sum_xx*sum_y)/(n*sum_xx-sum_x*sum_x)
b=(-sum_x*sum_y+n*sum_xy)/(n*sum_xx-sum_x*sum_x)

print "The required straight line is Y=%sX+(%s)"%(b,a)


