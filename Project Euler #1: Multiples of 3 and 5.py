#!/bin/python3
#python3
def ap(x):
    result=x*(x+1)//2
    return result

n=int(input())
while n!=0:
     nu=int(input())
     nu-=1
     a=nu//3
     b=nu//5
     c=nu//15
     print(3*ap(a)+5*ap(b)-15*ap(c))
     n-=1
