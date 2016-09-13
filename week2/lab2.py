#################################################
# Lab2
# Collaborator:zhengx,zhouy1
#################################################

from cs112_f16_wk2 import assertEqual, assertAlmostEqual, lintAll, testAll
import math

#################################################
# Helper functions
#################################################

def almostEqual(d1, d2, epsilon=10**-7):
    # note: use math.isclose() outside 15-112 with Python version 3.5 or later
    return (abs(d2 - d1) < epsilon)

import decimal
def roundHalfUp(d):
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

#################################################
# Problems
#################################################

def reverseNumber(n):
    total=0
    while(n>0):
        lastdigit=n%10
        n=n//10
        total=total*10+lastdigit
    return total

def isPrime(n):
    if (n < 2):
        return False
    if (n == 2):
        return True
    if (n % 2 == 0):
        return False
    maxFactor = roundHalfUp(n**0.5)
    for factor in range(3,maxFactor+1,2):
        if (n % factor == 0):
            return False
    return True
    
def isEmirpsPrime(n):
    if isPrime(n):
        if (isPrime(reverseNumber(n))and reverseNumber(n)!=n):
            return True  
    
def nthEmirpsPrime(n):
    guess=0
    found=0
    while(found<=n):
        guess+=1
        if(isEmirpsPrime(guess)):
            found+=1
    return guess

def findZeroWithBisection(f,x0,x1,epsilon):    
    if almostEqual(f(x0),0):return x0
    if almostEqual(f(x1),0):return x1
    elif f(x0)*f(x1)>0:return False
    while (almostEqual(f(x0),0)==False or almostEqual(f(x1),0)==False):
        a=(x0+x1)/2
        if f(a)*f(x0)>0:x0=a
        if f(a)*f(x1)>0:x1=a
    return a

def carrylessAdd(x,y):
    total=0
    i=0
    while(x>0 or y>0):
        d=(x%10+y%10)%10
        x//=10
        y//=10
        total=total+d*10**i
        i+=1
    return total

def numberOfDigit(n):
    n=n**2
    count=0
    while(n>0):
        n//=10
        count+=1
    return count

def isKaprekarNumber(n):
    if(n<=0):return False
    square = n**2
    first = numberOfDigit(n)//2
    second = numberOfDigit(n)-first
    secondHalf = square % 10**second
    firstHalf = (square - secondHalf)//10**second
    total = secondHalf+firstHalf
    return total == n

def nthKaprekarNumber(n):
    guess=0
    found=0
    while(found<=n):
        guess+=1
        if(isKaprekarNumber(guess)):
            found+=1
    return guess

def integral(f, a, b, N):
    distance=(b-a)/N
    area=0
    for i in range(N):
        area+=(f(a+i*distance)+f(a+(i+1)*distance))*distance/2
    return area
        

#################################################
# Test Functions
#################################################

def testNthEmirpsPrime():
    print('Testing nthEmirpsPrime()...', end='')
    assertEqual(nthEmirpsPrime(0), 13)
    assertEqual(nthEmirpsPrime(8), 107)
    assertEqual(nthEmirpsPrime(10), 149)
    assertEqual(nthEmirpsPrime(20), 701)
    print('Passed.')

def testFindZerosWithBisection():
    print('Testing findZerosWithBisection()...', end='')
    def f1(x): return x*x - 2 # root at x=sqrt(2)
    x = findZeroWithBisection(f1, 0, 2, 0.000000001)
    assertAlmostEqual(x, math.sqrt(2))
    def f2(x): return x**2 - (x + 1) # root at x=phi
    x = findZeroWithBisection(f2, 0, 2, 0.000000001)
    phi = (1 + 5**0.5)/2             # the actual value
    assertAlmostEqual(x, phi)
    def f3(x): return x**5 - 2**x # f(1)<0, f(2)>0
    x = findZeroWithBisection(f3, 1, 2, 0.000000001)
    assert(almostEqual(f3(x), 0))
    print('Passed.')

def testCarrylessAdd():
    print('Testing carrylessAdd()...', end='')
    assertEqual(carrylessAdd(785, 376), 51)
    assertEqual(carrylessAdd(12345678900, 38984034003), 40229602903)
    print('Passed.')

def testNthKaprekarNumber():
    print('Testing nthKaprekarNumber()...', end='')
    assertEqual(nthKaprekarNumber(0), 1)
    assertEqual(nthKaprekarNumber(1), 9)
    assertEqual(nthKaprekarNumber(2), 45)
    assertEqual(nthKaprekarNumber(3), 55)
    assertEqual(nthKaprekarNumber(4), 99)
    assertEqual(nthKaprekarNumber(5), 297)
    assertEqual(nthKaprekarNumber(6), 703)
    assertEqual(nthKaprekarNumber(7), 999)
    print('Passed.')

def f1(x): return 42
def i1(x): return 42*x 
def f2(x): return 2*x  + 1
def i2(x): return x**2 + x
def f3(x): return 9*x**2
def i3(x): return 3*x**3
def f4(x): return math.cos(x)
def i4(x): return math.sin(x)
def testIntegral():
    print('Testing integral()...', end='')
    epsilon = 10**-4
    assertAlmostEqual(integral(f1, -5, +5, 1), (i1(+5)-i1(-5)),
                      epsilon=epsilon)
    assertAlmostEqual(integral(f1, -5, +5, 10), (i1(+5)-i1(-5)),
                      epsilon=epsilon)
    assertAlmostEqual(integral(f2, 1, 2, 1), 4,
                      epsilon=epsilon)
    assertAlmostEqual(integral(f2, 1, 2, 250), (i2(2)-i2(1)),
                      epsilon=epsilon)
    assertAlmostEqual(integral(f3, 4, 5, 250), (i3(5)-i3(4)),
                      epsilon=epsilon)
    assertAlmostEqual(integral(f4, 1, 2, 250), (i4(2)-i4(1)),
                      epsilon=epsilon)
    print("Passed!")

#################################################
# Main
#################################################
def main():
    testAll(
        testNthEmirpsPrime,
        testFindZerosWithBisection,
        testCarrylessAdd,
        testNthKaprekarNumber,
        testIntegral,
    )

if __name__ == '__main__':
    main()
