#!/bin/python3
#python3
def sum_of_multiples(n):
    total = 0
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total

# Test with N = 10
N = 10
N1=100
result = sum_of_multiples(N)
print(result)
result = sum_of_multiples(N1)
print(result)
