import sys
from task2 import zero

def primes(a, b):
    zero(a, b)
    if a > b:
        a, b = b, a
    lst = [ i for i in range(a, b + 1) if all (i % j for j in range(2, i) if i % j == 0)]
    if len(lst) is 0:
        raise Exception("NoSimpleDigits")
    else:
        return lst


