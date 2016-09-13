#################################################
# Hw2
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

def sumOfSquaresOfDigits(n):
    n=abs(n)
    total=0
    while (n>0):
        squareOfDigit=(n%10)**2
        total+=squareOfDigit
        n//=10
    return (total)

def isHappyNumber(n):
    if (n<1):return False
    n=abs(n)
    while(n>0):
        n=sumOfSquaresOfDigits(n)
        if n==1: return True
        if n==4: return False
        
def nthHappyNumber(n):
    n=abs(n)
    number=0
    while(n>-1):
        number+=1
        if(isHappyNumber(number)):
            n-=1
    return number

def isPrimeNumber(n):
    if (n < 2):
        return False
    if (n == 2):
        return True
    if (n % 2 == 0):
        return False
    maxFactor = round(n**0.5)
    for factor in range(3,maxFactor+1,2):
        if (n % factor == 0):
            return False
    return True
    
def nthHappyPrime(n):
    n=abs(n)
    number=0
    while(n>-1):
        number+=1
        if(isHappyNumber(number) and isPrimeNumber(number)):
            n-=1
    return number

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

def nearestKaprekarNumber(n):
    lower=int(n)
    upper=math.ceil(n)
    while(isKaprekarNumber(lower)==False and isKaprekarNumber(upper)==False):
        lower-=1
        upper+=1
    if isKaprekarNumber(lower):
        if (isKaprekarNumber(upper) and ((upper-n)<(n-lower))):
            return upper
        return lower
    else:
        if isKaprekarNumber(upper):return upper

def numberOfDigits(n):
    n=abs(n)
    count=0
    if(n==0):return 1
    while(n>0):
        n//=10
        count+=1
    return count

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
    
def carrylessMultiply(x1,x2):
    total=0
    y=x1
    for x in range(numberOfDigits(x2)):
        x1=y
        for i in range(numberOfDigits(x1)):
            d=(x1%10*x2%10)%10
            x1//=10
            total=carrylessAdd(total,d*10**(i+x))
        
        x2//=10
    return total
        

def sumOfDigits(n):
    total=0
    while(n>0):
        d=n%10
        total+=d
        n//=10
    return total

def isSmithNumber(n):
    factor=2
    total=0
    original=n
    if (isPrimeNumber(original)):return False
    while(n>1):
        if n%factor==0:
            total+=sumOfDigits(factor)
            n//=factor
            factor-=1
        factor+=1
    
    if total==sumOfDigits(original):
        return True
        
def nthSmithNumber(n):
    guess=0
    found=0
    while(found<=n):
        guess+=1
        if(isSmithNumber(guess)):
            found+=1
    return guess

###### BONUS #######


"""
def isWeaklyPrime(n):
    if (n<1):return False
    number=numberOfDigits(n)
    for x in range(0,number):
        for i in range(10):
            if (isPrimeNumber(n)==False):return False
            else:
                olddigit=(n//10**x)%10
                newNumber=n
                newNumber-=olddigit*10**x
                newNumber+=i*10**x
                if (isPrimeNumber(newNumber) and newNumber !=n):
                    return False
        newNumber=n
    return True

def nthWeaklyPrime(n):    
    guess=0
    found=0
    while(found<=n):
        guess+=1
        if(isWeaklyPrime(guess)):
            found+=1
    return guess


def play112(game):
    return 42

#################################################
# Test Functions
#################################################

def testSumOfSquaresOfDigits():
    print("Testing sumOfSquaresOfDigits()...", end="")
    assertEqual(sumOfSquaresOfDigits(5), 25)   # 5**2 = 25
    assertEqual(sumOfSquaresOfDigits(12), 5)   # 1**2 + 2**2 = 1+4 = 5
    assertEqual(sumOfSquaresOfDigits(234), 29) # 2**2 + 3**2 + 4**2 = 4 + 9 + 16 = 29
    print("Passed all tests!")

def testIsHappyNumber():
    print("Testing isHappyNumber()...", end="")
    assertEqual(isHappyNumber(-7), False)
    assertEqual(isHappyNumber(1), True)
    assertEqual(isHappyNumber(2), False)
    assertEqual(isHappyNumber(97), True)
    assertEqual(isHappyNumber(98), False)
    assertEqual(isHappyNumber(404), True)
    assertEqual(isHappyNumber(405), False)
    print("Passed all tests!")

def testNthHappyNumber():
    print("Testing nthHappyNumber()...", end="")
    assertEqual(nthHappyNumber(0), 1)
    assertEqual(nthHappyNumber(1), 7)
    assertEqual(nthHappyNumber(2), 10)
    assertEqual(nthHappyNumber(3), 13)
    assertEqual(nthHappyNumber(4), 19)
    assertEqual(nthHappyNumber(5), 23)
    assertEqual(nthHappyNumber(6), 28)
    assertEqual(nthHappyNumber(7), 31)
    print("Passed all tests!")

def testIsHappyPrime():
    print("Testing isHappyPrime()...", end="")
    assertEqual(isHappyPrime(1), False)
    assertEqual(isHappyPrime(2), False)
    assertEqual(isHappyPrime(3), False)
    assertEqual(isHappyPrime(7), True)
    assertEqual(isHappyPrime(10), False)
    assertEqual(isHappyNumber(13), True)
    print("Passed all tests!")

def testNthHappyPrime():
    print("Testing nthHappyPrime...", end="")
    assertEqual(nthHappyPrime(0), 7)
    assertEqual(nthHappyPrime(1), 13)
    assertEqual(nthHappyPrime(2), 19)
    assertEqual(nthHappyPrime(3), 23)
    assertEqual(nthHappyPrime(4), 31)
    assertEqual(nthHappyPrime(10), 167)
    assertEqual(nthHappyPrime(20), 397)
    print("Passed all tests!")

def testNearestKaprekarNumber():
    print("Testing nearestKaprekarNumber()...", end="")
    assertEqual(nearestKaprekarNumber(1), 1)
    assertEqual(nearestKaprekarNumber(0), 1)
    assertEqual(nearestKaprekarNumber(-1), 1)
    assertEqual(nearestKaprekarNumber(-2), 1)
    assertEqual(nearestKaprekarNumber(-12345), 1)
    assertEqual(nearestKaprekarNumber(1.234), 1)
    assertEqual(nearestKaprekarNumber(4.99999999), 1)
    assertEqual(nearestKaprekarNumber(5), 1)
    assertEqual(nearestKaprekarNumber(5.00000001), 9)
    assertEqual(nearestKaprekarNumber(27), 9)
    assertEqual(nearestKaprekarNumber(28), 45)
    assertEqual(nearestKaprekarNumber(45), 45)
    assertEqual(nearestKaprekarNumber(50), 45)
    assertEqual(nearestKaprekarNumber(51), 55)
    assertEqual(nearestKaprekarNumber(1611), 999)
    assertEqual(nearestKaprekarNumber(1612), 2223)
    assertEqual(nearestKaprekarNumber(2475.4), 2223)
    assertEqual(nearestKaprekarNumber(2475.5), 2223)
    assertEqual(nearestKaprekarNumber(2475.51), 2728)
    assertEqual(nearestKaprekarNumber(2475.6), 2728)
    #kaps = [1, 9, 45, 55, 99, 297, 703, 999, 2223, 2728]
    #bigKaps = [994708, 999999]
    assertEqual(nearestKaprekarNumber(995123), 994708)
    assertEqual(nearestKaprekarNumber(9376543), 9372385)
    assertEqual(nearestKaprekarNumber(13641234), 13641364)
    print("Passed!")

def testCarrylessMultiply():
    print("Testing carrylessMultiply()...", end="")
    assertEqual(carrylessMultiply(643, 59), 417)
    assertEqual(carrylessMultiply(6412, 387), 807234)
    print("Passed!")

def testNthSmithNumber():
    print('Testing nthSmithNumber()... ', end='')
    assertEqual(nthSmithNumber(0), 4)
    assertEqual(nthSmithNumber(1), 22)
    assertEqual(nthSmithNumber(2), 27)
    assertEqual(nthSmithNumber(3), 58)
    assertEqual(nthSmithNumber(4), 85)
    assertEqual(nthSmithNumber(5), 94)
    assertEqual(nthSmithNumber(6), 121)
    print('Passed.')

def testNthWeaklyPrime():
    print("Testing carrylessMultiply()...", end="")
    #assertEqual(nthWeaklyPrime(0), 294001)
    assertEqual(nthWeaklyPrime(1), 505447)
    #assertEqual(nthWeaklyPrime(2), 584141)
    print("Passed!")

def testPlay112():
    print("Testing play112()...", end="")
    assertEqual(play112( 5 ), "88888: Unfinished!")
    assertEqual(play112( 521 ), "81888: Unfinished!")
    assertEqual(play112( 52112 ), "21888: Unfinished!")
    assertEqual(play112( 5211231 ), "21188: Unfinished!")
    assertEqual(play112( 521123142 ), "21128: Player 2 wins!")
    assertEqual(play112( 521123151 ), "21181: Unfinished!")
    assertEqual(play112( 52112315142 ), "21121: Player 1 wins!")
    assertEqual(play112( 523 ), "88888: Player 1: move must be 1 or 2!")
    assertEqual(play112( 51223 ), "28888: Player 2: move must be 1 or 2!")
    assertEqual(play112( 51211 ), "28888: Player 2: occupied!")
    assertEqual(play112( 5122221 ), "22888: Player 1: occupied!")
    assertEqual(play112( 51261 ), "28888: Player 2: offboard!")
    assertEqual(play112( 51122324152 ), "12212: Tie!")
    print("Passed!")

#################################################
# Main
#################################################

def main():
    testAll(
        testSumOfSquaresOfDigits,
        testIsHappyNumber,
        testNthHappyNumber,
        testNthHappyPrime,
        testNearestKaprekarNumber,
        testCarrylessMultiply,
        testNthSmithNumber,
        # bonus: (uncomment these to test them....)
        testNthWeaklyPrime,
        # testPlay112,
    )

if __name__ == '__main__':
    main()
"""