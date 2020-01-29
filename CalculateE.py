#2.71828182845904523536028747135266249775724709369995
from decimal import *

def Bernoulli(n): # https://en.wikipedia.org/wiki/E_(mathematical_constant)
    """
    not effient at all
    at n = 1000000000000000000000000000
    return 2.7182818284590452353602874 69993521583527724476019815...
    """
    getcontext().prec = 1000
    return str((Decimal(1) + Decimal(1)/Decimal(n))**n)

def factorial(n):
    sum = 1
    F = 1
    for i in range (1,n):
        pass