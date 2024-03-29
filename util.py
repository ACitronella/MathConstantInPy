
from decimal import Decimal
from functools import reduce
from math import prod
import copy

CONSTANTS = {
    "pi" : "3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489549303819644288109756659334461284756482337867831652712019091456485669234603486104543266482133936072602491412737245870066063155881748815209209628292540917153643678925903600113305305488204665213841469519415116094330572703657595919530921861173819326117931051185480744623799627495673518857527248912279381830119491298336733624406566430860213949463952247371907021798609437027705392171762931767523846748184676694051320005681271452635608277857713427577896091736371787214684409012249534301465495853710507922796892589235420199561121290219608640344181598136297747713099605187072113499999983729780499510597317328160963185950244594553469083026425223082533446850352619311881710100031378387528865875332083814206171776691473035982534904287554687311595628638823537875937519577818577805321712268066130019278766111959092164201989",
    "e" : "2.71828182845904523536028747135266249775724709369995957496696762772407663035354759457138217852516642742746639193200305992181741359662904357290033429526059563073813232862794349076323382988075319525101901157383418793070215408914993488416750924476146066808226480016847741185374234544243710753907774499206955170276183860626133138458300075204493382656029760673711320070932870912744374704723069697720931014169283681902551510865746377211125238978442505695369677078544996996794686445490598793163688923009879312773617821542499922957635148220826989519366803318252886939849646510582093923982948879332036250944311730123819706841614039701983767932068328237646480429531180232878250981945581530175671736133206981125099618188159304169"
}

def factorial(n):
    """
    เreturn n!
    """
    return prod(range(1, n+1))

def how_much_many_decimal_place_match(x:Decimal, ref:str, verbose:bool=False):
    ref_str = CONSTANTS[ref]
    x_str = str(x)
    return string_match_upto(x_str, ref_str, verbose)

def string_match_upto(x:str, ref:str, verbose:bool=False):
    for idx, (xi, refi) in enumerate(zip(x, ref)):
        if xi == ".":
            continue
        if xi != refi:
            if verbose:
                if idx+5 < len(ref) and idx-5 >= 0: print("expected:  ", ref[idx-5: idx+5]); print("calculated:", x[idx-5:idx+5]); 
                elif idx+5 < len(ref) and not(idx-5 >= 0): print("expected:  ", ref[:idx+5]); print("calculated:", x[:idx+5])
                elif not(idx+5 < len(ref)) and idx-5 >= 0: print("expected:  ", ref[idx-5:]); print("calculated:", x[idx-5:])
                else: print("expected:  ", ref); print("calcualted:", x)
            return idx
    if verbose:
        print("matched all")
    return -1

def sequence_forward_different(seq:list) -> list:
    assert len(seq) > 1
    return list(map(lambda x0, x1: x1 - x0, seq, seq[1:]))

def main(fn_list, val:str):
    for idx, fn in enumerate(fn_list):
        print("%d: %s (%s)" % (idx, fn.__name__, fn.__doc__))
    while (not (idx:=input("Select how you calculate %s: " % val)).isnumeric()) or (int(idx) >= len(fn_list)): 
        if idx == "":break
        print("invalid input")
    while (not (n:=input("how many iteration: ")).isnumeric()) or (int(n) <= 0): 
        if n == "":break
        print("invalid input")
    while (not (prec:=input("how many precision: ")).isnumeric()) or (int(prec) <= 0): 
        if prec == "":break
        print("invalid input")

    # setting default values
    if idx == "": idx = len(fn_list) - 1 
    if n == "": n = 1000
    if prec == "": prec = 100

    idx = int(idx); n = int(n); prec = int(prec)
    x = fn_list[idx](n, prec)
    print("Output: ", x)
    print(how_much_many_decimal_place_match(x, val, verbose=True))

def trapezoidal_rule(dx:Decimal, y:"list[Decimal]"):
    """assume uniform grid. https://en.wikipedia.org/wiki/Trapezoidal_rule"""
    return ((y[0] + y[-1])/2 + reduce(lambda a, b : a + b, y[1:-1])) * dx
