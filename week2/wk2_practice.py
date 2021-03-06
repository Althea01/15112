#################################################
# Week2 Practice
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
# Tue Lecture
#################################################

def mostFrequentDigit(n):
    return 42

def isPowerfulNumber(n):
    for x in range(n**0.5):
        for i in range(n**0.4):
            if n//(x**2)*(i**3)==0:
                return True
    return False
    
print(isPowerfulNumber(1))

def nthPowerfulNumber(n):
    return 42

#################################################
# Wed Recitation
#################################################

def longestDigitRun(n):
    return 42

def longestIncreasingRun(n):
    return 42

def nthPalindromicPrime(n):
    return 42

def nthLeftTruncatablePrime(n):
    return 42

def nthCarolPrime(n):
    return 42

#################################################
# Extra Practice
#################################################

def pi(n):
    return 42

def h(n):
    return 42

def estimatedPi(n):
    return 42

def estimatedPiError(n):
    return 42

def hasOnlyOddDigits(n):
    return 42

def isRotation(x, y):
    return 42

def nthCircularPrime(n):
    return 42

#################################################
# Test Functions
#################################################

def testMostFrequentDigit():
    print('Testing mostFrequentDigit()... ', end='')
    assertEqual(mostFrequentDigit(0), 0)
    assertEqual(mostFrequentDigit(1223), 2)
    assertEqual(mostFrequentDigit(12233), 2)
    assertEqual(mostFrequentDigit(-112233), 1)
    assertEqual(mostFrequentDigit(1223322332), 2)
    assertEqual(mostFrequentDigit(123456789), 1)
    assertEqual(mostFrequentDigit(1234567789), 7)
    assertEqual(mostFrequentDigit(1000123456789), 0)
    print('Passed!')

def testNthPowerfulNumber():
    print('Testing nthPowerfulNumber()... ', end='')
    assertEqual(nthPowerfulNumber(0), 1)
    assertEqual(nthPowerfulNumber(1), 4)
    assertEqual(nthPowerfulNumber(2), 8)
    assertEqual(nthPowerfulNumber(3), 9)
    assertEqual(nthPowerfulNumber(4), 16)
    assertEqual(nthPowerfulNumber(5), 25)
    assertEqual(nthPowerfulNumber(10), 64)
    assertEqual(nthPowerfulNumber(15), 121)
    assertEqual(nthPowerfulNumber(20), 196)
    print('Passed!')

def testLongestDigitRun():
    print('Testing longestDigitRun()... ', end='')
    assertEqual(longestDigitRun(117773732), 7)
    assertEqual(longestDigitRun(-677886), 7)
    assertEqual(longestDigitRun(5544), 4)
    assertEqual(longestDigitRun(1), 1)
    assertEqual(longestDigitRun(0), 0)
    assertEqual(longestDigitRun(22222), 2)
    assertEqual(longestDigitRun(111222111), 1)
    print('Passed.')

def testLongestIncreasingRun():
    print('Testing longestIncreasingRun()... ', end='')
    assertEqual(longestIncreasingRun(27648923679), 23679)
    assertEqual(longestIncreasingRun(123345), 345)
    assertEqual(longestIncreasingRun(1232), 123)
    assertEqual(longestIncreasingRun(0), 0)
    assertEqual(longestIncreasingRun(1), 1)
    assertEqual(longestIncreasingRun(10012301230123), 123)
    assertEqual(longestIncreasingRun(12345678987654321), 123456789)
    print('Passed.')

def testNthPalindromicPrime():
    print('Testing nthPalindromicPrime()... ', end='')
    assertEqual(nthPalindromicPrime(0), 2)
    assertEqual(nthPalindromicPrime(1), 3)
    assertEqual(nthPalindromicPrime(5), 101)
    assertEqual(nthPalindromicPrime(10), 313)
    print('Passed.')

def testNthLeftTruncatablePrime():
    print('Testing nthLeftTruncatablePrime()... ', end='')
    assertAlmostEqual(nthLeftTruncatablePrime(0), 2)
    assertAlmostEqual(nthLeftTruncatablePrime(10), 53)
    assertAlmostEqual(nthLeftTruncatablePrime(1), 3)
    assertAlmostEqual(nthLeftTruncatablePrime(5), 17)
    print('Passed.')

def testCarolPrime():
    print('Testing nthCarolPrime()... ', end='')
    assertAlmostEqual(nthCarolPrime(0), 7)
    assertAlmostEqual(nthCarolPrime(1), 47)
    assertAlmostEqual(nthCarolPrime(3), 3967)
    assertAlmostEqual(nthCarolPrime(6), 16769023)
    print('Passed.')

def testPi():
    print('Testing pi()... ', end='')
    assertEqual(pi(1), 0)
    assertEqual(pi(2), 1)
    assertEqual(pi(3), 2)
    assertEqual(pi(4), 2)
    assertEqual(pi(5), 3)
    assertEqual(pi(100), 25)  # there are 25 primes in the range [2,100]
    print('Passed.')

def testH():
    print('Testing h()... ', end='')
    assertAlmostEqual(h(0),0)
    assertAlmostEqual(h(1),1/1            )  # h(1) = 1/1
    assertAlmostEqual(h(2),1/1 + 1/2      )  # h(2) = 1/1 + 1/2
    assertAlmostEqual(h(3),1/1 + 1/2 + 1/3)  # h(3) = 1/1 + 1/2 + 1/3
    print('Passed.')

def testEstimatedPi():
    print('Testing estimatedPi()... ', end='')
    assertEqual(estimatedPi(100), 27)
    print('Passed.')

def testEstimatedPiError():
    print('Testing estimatedPi()... ', end='')
    assertEqual(estimatedPiError(100), 2) # pi(100) = 25, estimatedPi(100) = 27
    assertEqual(estimatedPiError(200), 0) # pi(200) = 46, estimatedPi(200) = 46
    assertEqual(estimatedPiError(300), 1) # pi(300) = 62, estimatedPi(300) = 63
    assertEqual(estimatedPiError(400), 1) # pi(400) = 78, estimatedPi(400) = 79
    assertEqual(estimatedPiError(500), 1) # pi(500) = 95, estimatedPi(500) = 94
    print('Passed.')

def testHasOnlyOddDigits():
    print('Testing hasOnlyOddDigits()... ', end='')
    assertEqual(hasOnlyOddDigits(1), True)
    assertEqual(hasOnlyOddDigits(13579), True)
    assertEqual(hasOnlyOddDigits(111111), True)
    assertEqual(hasOnlyOddDigits(-999999999999), True)
    assertEqual(hasOnlyOddDigits(0), False)
    assertEqual(hasOnlyOddDigits(10), False)
    assertEqual(hasOnlyOddDigits(13579297531), False)
    assertEqual(hasOnlyOddDigits(-13579297531), False)
    print('Passed.')

def testIsRotation():
    print('Testing isRotation()... ', end='')
    assertEqual(isRotation(1, 1), True)
    assertEqual(isRotation(1234, 4123), True)
    assertEqual(isRotation(1234, 3412), True)
    assertEqual(isRotation(1234, 2341), True)
    assertEqual(isRotation(1234, 1234), True)
    assertEqual(isRotation(1234, -1234), False)
    assertEqual(isRotation(1234, 123), False)
    assertEqual(isRotation(1234, 12345), False)
    assertEqual(isRotation(1234, 1235), False)
    assertEqual(isRotation(1234, 1243), False)
    print('Passed.')

def testNthCircularPrime():
    print('Testing nthCircularPrime()... ', end='')
    assertEqual(nthCircularPrime(0), 2)
    assertEqual(nthCircularPrime(1), 3)
    assertEqual(nthCircularPrime(2), 5)
    assertEqual(nthCircularPrime(10), 73)
    assertEqual(nthCircularPrime(15), 197)
    assertEqual(nthCircularPrime(16), 199)
    print('Passed.')

#################################################
# Main
#################################################

def main():
    testAll(
        testMostFrequentDigit,
        testNthPowerfulNumber,
        testLongestDigitRun,
        testLongestIncreasingRun,
        testNthPalindromicPrime,
        testNthLeftTruncatablePrime,
        testCarolPrime,
        testPi,
        testH,
        testEstimatedPi,
        testEstimatedPiError,
        testHasOnlyOddDigits,
        testIsRotation,
        testNthCircularPrime,
    )

if __name__ == '__main__':
    main()
