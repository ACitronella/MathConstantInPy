#  3.1415926535897932384626433...
import math
import sys
from decimal import *

sys.setrecursionlimit(100000)


def factorial(n):
    """
    return n!
    using recurrsion method
    """
    if n == 1 or n == 0:
        return 1
    return n*factorial(n-1)

def leibniz(n): #  leibniz formula for π
    """
    parameter int n is for rounds of iteration

    as n increses
    time uses for computing is longer
    """
    sum = 0.0
    for i in range(1,n):
        denominator = 2*i - 1
        sum = sum + (-1)**(i-1)*(4/denominator)
    return sum #  can be use after n > 1000000, Presion 5 digit

def another(n): #  https://math.stackexchange.com/questions/1023195/infinite-series-with-pi
    """
    parameter int n is for rounds of iteration

    as n increses
    time uses for computing is longer
    """
    sum = 0.0
    for i in range(1,n):
        sum = sum + (6/(i**2))
    return sum**(1/2) #  can be use after n > 1000000, Presion 5 digit

def Ramanujan(n): #  Ramanujan's formulae
    """
    parameter int n is for rounds of iteration

    as n increses
    time uses for computing is longer
    """
    sum = Decimal(0.0)
    getcontext().prec = 100
    first = Decimal((2.0*pow(2.0,(1/2)))/9801.0)
    for k in range(n):
        second = Decimal(factorial(4*k))
        third = Decimal(1103.0 + 26390.0*k)
        forth = Decimal(pow(factorial(k), 4.0))
        fifth = Decimal(pow(396.0,(4.0*k)))
        sum = sum + (second*third)/(forth*fifth)
    
    sum = sum * first
    
    return Decimal(1/sum) #  can approximate around 15 decimal digit

def Spigot(n): #  Spigot algorithms
    sum = 0.0
    for i in range(n):
        sum = sum + pow(1/16,i)*(4/(8*i+1)-(2/(8*i+4))-(1/(8*i+5))-(1/(8*i+6)))
    return sum

def Nilakantha(n):
    """
    parameter int n is for rounds of iteration

    as n increses
    time uses for computing is longer
    """
    sum = 3.0
    for i in range(1,n):
        sum = sum + pow(-1,i+1)*(4/(2*i*(2*i+1)*(2*i+2)))
    return sum

def Chudnovsky(n): #  https://en.wikipedia.org/wiki/Chudnovsky_algorithm
    """
    parameter 
    int n is for rounds of iteration

    as n increses
    time uses for computing increses also
    """
    sum = Decimal(0.0)
    getcontext().prec = 2000
    for i in range(n):
        top = factorial(6*i)*(545140134*i+13591409)
        bottom = factorial(3*i)*factorial(i)**3*(-262537412640768000)**i 
        sum = sum + Decimal(top)/Decimal(bottom)

    return str(Decimal(426880)*Decimal(10005).sqrt() / Decimal(sum))[:n]

def Chudnovsky2(n = 500, prec = 5000): # more efficient version of Chudnovsky
    """
    parameter 
    int n is for rounds of iteration
    int prec is for amount of digits

    as all of parameter increses
    time uses for computing increses also
    """
    sum = Decimal(0.0)
    prec = prec + 5
    getcontext().prec = prec + 3
    M = 1
    L = 13591409
    X = Decimal(1)
    K = 6
    for i in range(1, n):
        sum = sum + M*L/X
       
        M = M*Decimal(K**3-16*K)/Decimal((i)**3)
        K = K + 12
        L = L + 545140134
        X = X * -262537412640768000
    
    prec = prec - 3 
    return str(426880*Decimal(10005).sqrt() / sum)[:prec]

print(Chudnovsky2()) 