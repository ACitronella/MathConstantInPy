#  3.1415926535897932384626433...
from functools import reduce
import sys
from decimal import Decimal, getcontext
from util import factorial, how_much_many_decimal_place_match, sequence_forward_different

sys.setrecursionlimit(100000)

def leibniz(n:int): #  leibniz formula for π
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

def another(n:int): #  https://math.stackexchange.com/questions/1023195/infinite-series-with-pi
    """
    parameter int n is for rounds of iteration

    as n increses
    time uses for computing is longer
    """
    sum = 0.0
    for i in range(1,n):
        sum = sum + (6/(i**2))
    return sum**(1/2) #  can be use after n > 1000000, Presion 5 digit

def Ramanujan(n:int): #  Ramanujan's formulae
    """
    parameter int n is for rounds of iteration

    as n increses
    time uses for computing is longer
    """
    sum = Decimal(0.0)
    first = Decimal((2.0*pow(2.0,(1/2)))/9801.0)
    for k in range(n):
        second = Decimal(factorial(4*k))
        third = Decimal(1103.0 + 26390.0*k)
        forth = Decimal(pow(factorial(k), 4.0))
        fifth = Decimal(pow(396.0,(4.0*k)))
        sum = sum + (second*third)/(forth*fifth)
    
    sum = sum * first
    
    return Decimal(1/sum) #  can approximate around 15 decimal digit

def Spigot(n:int): #  Spigot algorithms
    sum = 0.0
    for i in range(n):
        sum = sum + pow(1/16,i)*(4/(8*i+1)-(2/(8*i+4))-(1/(8*i+5))-(1/(8*i+6)))
    return sum

def Nilakantha(n:int):
    """
    parameter int n is for rounds of iteration

    as n increses
    time uses for computing is longer
    """
    sum = 3.0
    for i in range(1,n):
        sum = sum + pow(-1,i+1)*(4/(2*i*(2*i+1)*(2*i+2)))
    return sum

def Chudnovsky(n:int=100, prec:int=100) -> Decimal: #  https://en.wikipedia.org/wiki/Chudnovsky_algorithm
    """
    parameter 
    int n is for rounds of iteration

    as n increses
    time uses for computing increses also
    """
    getcontext().prec = prec
    sum = Decimal(0.0)
    for i in range(n):
        top = factorial(6*i)*(545140134*i+13591409)
        bottom = factorial(3*i)*factorial(i)**3*(-262537412640768000)**i 
        sum = sum + Decimal(top)/Decimal(bottom)

    return Decimal(426880)*Decimal(10005).sqrt() / sum

def Chudnovsky2(n:int=100, prec:int=100) -> Decimal: # more efficient version of Chudnovsky
    """
    parameter 
    int n is for rounds of iteration
    int prec is for amount of digits

    as all of parameter increses
    time uses for computing increses also
    """
    getcontext().prec = prec
    sum = Decimal(0.0)
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
    return Decimal(426880)*Decimal(10005).sqrt() / sum

def ratio_of_circumference_circle(n:int, prec:int=100) -> Decimal:
    """
    y(x) = (1 - x^2)^2 (top half of circle with radius 1),
    riemman integral of (1 + D_x(y(x))^2)^(1/2) from x in (-1, 1),
    suffer from sqrt and abuse of memory
    """
    getcontext().prec = prec
    x = list(map(lambda x : (Decimal(x)+1) * 2/n - 1, range(n-1)))
    y_function = lambda x : (-x*x + 1).sqrt()
    y = list(map(y_function, x))
    dx = [Decimal(2/n)]*len(y) # sequence_forward_different(x) 
    dy = sequence_forward_different(y)
    dl = list(map(lambda x, y: (x*x + y*y).sqrt(), dx, dy))
    return reduce(lambda x, y: x + y, dl)

if __name__ == "__main__":
    pi = Chudnovsky2(100)
    print(how_much_many_decimal_place_match(pi, "pi"))
    print(pi)