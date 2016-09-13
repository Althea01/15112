#################################################
# Hw1
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
# Hw1 problems
#################################################

def fabricYards(inches):
    if inches%36 == 0:
        return inches//36
    return inches//36+1
 
def fabricExcess(inches):
    if inches < 0:
        return False
    else:
        return fabricYards(inches)*36-inches

def distance(x1,y1,x2,y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5

def isRightTriangle(x1, y1, x2, y2, x3, y3):
    a = distance(x1,y1,x2,y2)
    b = distance(x1,y1,x3,y3)
    c = distance(x2,y2,x3,y3)
    if almostEqual(a**2+b**2,c**2):
        return True
    elif almostEqual(a**2+c**2,b**2):
        return True
    elif almostEqual(b**2+c**2,a**2):
        return True
    else:
        return False
    

def Number(a,b,midpoints,n):
   return roundHalfUp(a-n*(a-b)/(midpoints+1))

def colorBlender(rgb1, rgb2, midpoints, n):
    if (midpoints >= 0 and n >= 0 and n-1 <= midpoints):
        oneFirst = rgb1//1000000
        twoFirst = rgb2//1000000
        oneMiddle = (rgb1-oneFirst*1000000)//1000
        twoMiddle = (rgb2-twoFirst*1000000)//1000
        oneLast = rgb1-oneFirst*1000000-oneMiddle*1000
        twoLast = rgb2-twoFirst*1000000-twoMiddle*1000
        firstNumber = Number(oneFirst, twoFirst, midpoints,n)
        secondNumber = Number(oneMiddle,twoMiddle,midpoints,n)
        thirdNumber = Number(oneLast,twoLast,midpoints,n)
        return firstNumber*1000000+secondNumber*1000+thirdNumber
    else:
        return None
    
    

def bonusFindIntRootsOfCubic(a, b, c, d):
   p = -b/(3*a)
   q = p**3+(b*c-3*a*d)/(6*a**2)
   r = c/(3*a)
   x1 = (q+(q**2+(r-p**2)**3)**0.5)**(1/3)+(q-(q**2+(r-p**2)**3)**0.5)**(1/3)+p
   x1 = int(x1.real)
   x2 = (-b-a*x1+(b**2-4*a*c-2*a*b*x1-3*a**2*x1**2)**0.5)/(2*a)
   x2 = int(x2.real)
   x3 = (-b-a*x1-(b**2-4*a*c-2*a*b*x1-3*a**2*x1**2)**0.5)/(2*a)
   x3 = int(x3.real)
   
   root1 = min(x1,x2,x3)
   root3 = max(x1,x2,x3)
   root2 = x1+x2+x3-root1-root3
   return root1,root2,root3

#################################################
# Hw1 Test Functions
#################################################

def testFabricYards():
    print('Testing fabricYards()... ', end='')
    assertEqual(fabricYards(0), 0)
    assertEqual(fabricYards(1), 1)
    assertEqual(fabricYards(35), 1)
    assertEqual(fabricYards(36), 1)
    assertEqual(fabricYards(37), 2)
    assertEqual(fabricYards(72), 2)
    assertEqual(fabricYards(73), 3)
    assertEqual(fabricYards(108), 3)
    assertEqual(fabricYards(109), 4)
    print('Passed.')
 
def testFabricExcess():
    print('Testing fabricExcess()... ', end='')
    assertEqual(fabricExcess(0), 0)
    assertEqual(fabricExcess(1), 35)
    assertEqual(fabricExcess(35), 1)
    assertEqual(fabricExcess(36), 0)
    assertEqual(fabricExcess(37), 35)
    assertEqual(fabricExcess(72), 0)
    assertEqual(fabricExcess(73), 35)
    assertEqual(fabricExcess(108), 0)
    assertEqual(fabricExcess(109), 35)
    print('Passed.')

def testIsRightTriangle():
    print('Testing isRightTriangle()... ', end='')
    assertEqual(isRightTriangle(0, 0, 0, 3, 4, 0), True)
    assertEqual(isRightTriangle(1, 1.3, 1.4, 1, 1, 1), True)
    assertEqual(isRightTriangle(9, 9.12, 8.95, 9, 9, 9), True)
    assertEqual(isRightTriangle(0, 0, 0, math.pi, math.e, 0), True)
    assertEqual(isRightTriangle(0, 0, 1, 1, 2, 0), True)
    assertEqual(isRightTriangle(0, 0, 1, 2, 2, 0), False)
    assertEqual(isRightTriangle(1, 0, 0, 3, 4, 0), False)
    print('Passed.')

def testColorBlender():
    print('Testing colorBlender()... ', end='')
    # http://meyerweb.com/eric/tools/color-blend/#DC143C:BDFCC9:3:rgbd
    assertEqual(colorBlender(220020060, 189252201, 3, -1), None)
    assertEqual(colorBlender(220020060, 189252201, 3, 0), 220020060)
    assertEqual(colorBlender(220020060, 189252201, 3, 1), 212078095)
    assertEqual(colorBlender(220020060, 189252201, 3, 2), 205136131)
    assertEqual(colorBlender(220020060, 189252201, 3, 3), 197194166)
    assertEqual(colorBlender(220020060, 189252201, 3, 4), 189252201)
    assertEqual(colorBlender(220020060, 189252201, 3, 5), None)
    # http://meyerweb.com/eric/tools/color-blend/#0100FF:FF0280:2:rgbd
    assertEqual(colorBlender(1000255, 255002128, 2, -1), None)
    assertEqual(colorBlender(1000255, 255002128, 2, 0), 1000255)
    assertEqual(colorBlender(1000255, 255002128, 2, 1), 86001213)
    assertEqual(colorBlender(1000255, 255002128, 2, 2), 170001170)
    assertEqual(colorBlender(1000255, 255002128, 2, 3), 255002128)
    print('Passed.')

def getCubicCoeffs(k, root1, root2, root3):
    # Given roots e,f,g and vertical scale k, we can find
    # the coefficients a,b,c,d as such:
    # k(x-e)(x-f)(x-g) =
    # k(x-e)(x^2 - (f+g)x + fg)
    # kx^3 - k(e+f+g)x^2 + k(ef+fg+eg)x - kefg
    e,f,g = root1, root2, root3
    return k, -k*(e+f+g), k*(e*f+f*g+e*g), -k*e*f*g

def testFindIntRootsOfCubicCase(k, z1, z2, z3):
    a,b,c,d = getCubicCoeffs(k, z1, z2, z3)
    observed = bonusFindIntRootsOfCubic(a,b,c,d)
    m1 = min(z1, z2, z3)
    m3 = max(z1, z2, z3)
    m2 = (z1+z2+z3)-(m1+m3)
    actual = (m1, m2, m3)
    assertEqual(observed, actual)

def testBonusFindIntRootsOfCubic():
    print('Testing findIntRootsOfCubic()...', end='')
    testFindIntRootsOfCubicCase(5, 1, 3,  2)
    testFindIntRootsOfCubicCase(2, 5, 33, 7)
    testFindIntRootsOfCubicCase(-18, 24, 3, -8)
    testFindIntRootsOfCubicCase(1, 2, 3, 4)
    print('Passed.')

#################################################
# Hw1 Main
#################################################

def main():
    lintAll() # check style rules
    testAll(
        testFabricYards,
        testFabricExcess,
        testIsRightTriangle,
        testColorBlender,
        # testBonusFindIntRootsOfCubic
    )

if __name__ == '__main__':
    main()
