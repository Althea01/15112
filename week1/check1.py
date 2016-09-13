#################################################
# Check1
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
# Problems
#################################################

def distance(x1, y1, x2, y2):
    return 42

def circlesIntersect(x1, y1, r1, x2, y2, r2):
    return 42

def getInRange(x, bound1, bound2):
    return 42

def eggCartons(eggs):
    return 42

def pascalsTriangleValue(row, col):
    return 42

#################################################
# Test Functions
#################################################

def testDistance():
    print('Testing distance()... ', end='')
    assertAlmostEqual(distance(0, 0, 3, 4), 5)
    assertAlmostEqual(distance(-1, -2, 3, 1), 5)
    assertAlmostEqual(distance(-.5, .5, .5, -.5), 2**0.5)
    print('Passed.')

def testCirclesIntersect():
    print('Testing circlesIntersect()... ', end='')
    assertEqual(circlesIntersect(0, 0, 2, 3, 0, 2), True)
    assertEqual(circlesIntersect(0, 0, 2, 4, 0, 2), True)
    assertEqual(circlesIntersect(0, 0, 2, 5, 0, 2), False)
    assertEqual(circlesIntersect(3, 3, 3, 3, -3, 3), True)
    assertEqual(circlesIntersect(3, 3, 3, 3,- 3, 2.99), False)
    print('Passed.')

def testGetInRange():
    print('Testing getInRange()... ', end='')
    assertEqual(getInRange(5, 1, 10), 5)
    assertEqual(getInRange(5, 5, 10), 5)
    assertEqual(getInRange(5, 9, 10), 9)
    assertEqual(getInRange(5, 10, 10), 10)
    assertEqual(getInRange(5, 10, 1), 5)
    assertEqual(getInRange(5, 10, 5), 5)
    assertEqual(getInRange(5, 10, 9), 9)
    assertEqual(getInRange(0, -20, -30), -20)
    assertAlmostEqual(getInRange(0, -20.25, -30.33), -20.25)
    print('Passed.')

def testEggCartons():
    print('Testing eggCartons()... ', end='')
    assertEqual(eggCartons(0), 0)
    assertEqual(eggCartons(1), 1)
    assertEqual(eggCartons(12), 1)
    assertEqual(eggCartons(13), 2)
    assertEqual(eggCartons(24), 2)
    assertEqual(eggCartons(25), 3)
    print('Passed.')

def testPascalsTriangleValue():
    print('Testing pascalsTriangleValue()... ', end='')
    assertEqual(pascalsTriangleValue(3,0), 1)
    assertEqual(pascalsTriangleValue(3,1), 3)
    assertEqual(pascalsTriangleValue(3,2), 3)
    assertEqual(pascalsTriangleValue(3,3), 1)
    assertEqual(pascalsTriangleValue(1234,0), 1)
    assertEqual(pascalsTriangleValue(1234,1), 1234)
    assertEqual(pascalsTriangleValue(1234,2), 760761)
    assertEqual(pascalsTriangleValue(3,-1), None)
    assertEqual(pascalsTriangleValue(3,4), None)
    assertEqual(pascalsTriangleValue(-3,2), None)
    print('Passed.')

#################################################
# Main
#################################################

def main():
    lintAll() # check style rules
    testAll(
        testDistance,
        testCirclesIntersect,
        testGetInRange,
        testEggCartons,
        testPascalsTriangleValue,
    )

if __name__ == '__main__':
    main()
