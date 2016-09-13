#################################################
# Lab1 Partners: zhengx, cjye
#################################################

from cs112_f16_wk1 import assertEqual, assertAlmostEqual, lintAll, testAll
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
# Lab1 problems
#################################################

def nearestOdd(n):
    n1 = int(n)
    lower = n1-1
    upper = n1+1
    if (n1%2 == 1): return n1
    else:
        if(abs(lower-n)<=abs(upper-n)):return lower
        else:
            return upper

def rectanglesOverlap(x1, y1, w1, h1, x2, y2, w2, h2):
    if (x1-x2-w2<=0 and x1+w1-x2>=0):
        if (y1-y2-h2<=0 and y1+h1-y2>=0):
            return True
        else:
            return False
    else:
        return False

def isInteger(n):
    return n-int(n)==0

def isPerfectSquare(n):
    if(isinstance(n,int) and n>=0 and isInteger(n**0.5)):
        return True
    else:
        return False

def getKthDigit(n, k):
    n=abs(n)
    n=n//10**k
    return n%10

def setKthDigit(n, k, d):
    if n>=0:
        afterDelete = n-getKthDigit(n,k)*10**k
        return afterDelete + d*10**k
    else:
        afterDelete = n+getKthDigit(n,k)*10**k
        return afterDelete - d*10**k

def riverCruiseUpstreamTime(totalTime, totalDistance, riverCurrent):
    a = totalTime
    b = totalDistance
    c = riverCurrent
    boatSpeed = (b+(b**2+4*a**2*c**2)**0.5)/(2*a)
    upStreamSpeed = boatSpeed - c
    return b/2/upStreamSpeed

#################################################
# Lab1 Test Functions
################################################

def testNearestOdd():
    print('Testing nearestOdd()... ', end='')
    assertEqual(nearestOdd(13), 13)
    assertEqual(nearestOdd(12.001), 13)
    assertEqual(nearestOdd(12), 11)
    assertEqual(nearestOdd(11.999), 11)
    assertEqual(nearestOdd(-13), -13)
    assertEqual(nearestOdd(-12.001), -13)
    assertEqual(nearestOdd(-12), -13)
    assertEqual(nearestOdd(-11.999), -11)
    print('Passed.')

def testRectanglesOverlap():
    print('Testing rectanglesOverlap()...', end='')
    assertEqual(rectanglesOverlap(1, 1, 2, 2, 2, 2, 2, 2), True)
    assertEqual(rectanglesOverlap(1, 1, 2, 2, -2, -2, 6, 6), True)
    assertEqual(rectanglesOverlap(1, 1, 2, 2, 3, 3, 1, 1), True)
    assertEqual(rectanglesOverlap(1, 1, 2, 2, 3.1, 3, 1, 1), False)
    assertEqual(rectanglesOverlap(1, 1, 1, 1, 1.9, -1, 0.2, 1.9), False)
    assertEqual(rectanglesOverlap(1, 1, 1, 1, 1.9, -1, 0.2, 2), True)
    assertEqual(rectanglesOverlap(1, 1, 2, 2, 2, 2, 2, 6), True)
    assertEqual(rectanglesOverlap(1, 1, 2, 2, 3,4,5,6), False)
    print('Passed.')

def testIsPerfectSquare():
    print('Testing isPerfectSquare()... ', end='')
    assertEqual(isPerfectSquare(0), True)
    assertEqual(isPerfectSquare(1), True)
    assertEqual(isPerfectSquare(16), True)
    assertEqual(isPerfectSquare(1234**2), True)
    assertEqual(isPerfectSquare(15), False)
    assertEqual(isPerfectSquare(17), False)
    assertEqual(isPerfectSquare(-16), False)
    assertEqual(isPerfectSquare(1234**2+1), False)
    assertEqual(isPerfectSquare(1234**2-1), False)
    assertEqual(isPerfectSquare(4.0000001), False)
    assertEqual(isPerfectSquare('Do not crash here!'), False)
    print('Passed.')

def testGetKthDigit():
    print('Testing getKthDigit()... ', end='')
    assertEqual(getKthDigit(809, 0), 9)
    assertEqual(getKthDigit(809, 1), 0)
    assertEqual(getKthDigit(809, 2), 8)
    assertEqual(getKthDigit(809, 3), 0)
    assertEqual(getKthDigit(0, 100), 0)
    assertEqual(getKthDigit(-809, 0), 9)
    print('Passed.')

def testSetKthDigit():
    print('Testing setKthDigit()... ', end='')
    assertEqual(setKthDigit(809, 0, 7), 807)
    assertEqual(setKthDigit(809, 1, 7), 879)
    assertEqual(setKthDigit(809, 2, 7), 709)
    assertEqual(setKthDigit(809, 3, 7), 7809)
    assertEqual(setKthDigit(0, 4, 7), 70000)
    assertEqual(setKthDigit(-809, 0, 7), -807)
    print('Passed.')

def testRiverCruiseUpstreamTime():
    print('Testing riverCruiseUpstreamTime()... ', end='')
    # example from the source notes:
    totalTime = 3 # hours
    totalDistance = 30 # 15km up, 15km back down
    riverCurrent = 2 # km/hour
    assertAlmostEqual(riverCruiseUpstreamTime(totalTime,
                                              totalDistance,
                                              riverCurrent),
                       1.7888736053508778) # 1.79 in notes
    # another simple example
    totalTime = 3 # hours
    totalDistance = 30 # 15km up, 15km back down
    riverCurrent = 0 # km/hour
    assertAlmostEqual(riverCruiseUpstreamTime(totalTime,
                                              totalDistance,
                                              riverCurrent),
                       1.5)
    assertAlmostEqual(riverCruiseUpstreamTime(4,56,2),2.2801098892805185)
    print('Passed.')

#################################################
# Lab1 Main
################################################

def main():
    lintAll() # check style rules
    testAll(
        testNearestOdd,
        testRectanglesOverlap,
        testIsPerfectSquare,
        testGetKthDigit,
        testSetKthDigit,
        testRiverCruiseUpstreamTime
    )

if __name__ == '__main__':
    main()
