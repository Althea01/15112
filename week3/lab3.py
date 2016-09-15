#################################################
# Lab3 Collaborator: ruohaig
#################################################

from cs112_f16_wk3 import assertEqual, assertAlmostEqual, lintAll, testAll
import math, string

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

def leastFrequentLetters(s):
    t=s.lower() #To get rid of the uppercases
    result=""
    min=10*10**10 #To make sure the first count is less than min
    count=0
    for letter in string.ascii_lowercase: 
    #loop through 26 alphabets to maintain the order
        if t.count(letter)!=0: # == letter is in the string
            count=t.count(letter)
            if count<min:
                min=count
                result=letter #last letter is not the least frequent,replaced
            if count==min:
                min=count
                if result.count(letter)==0:
                    result+=letter
            #Dont need count>min because won't be least frequent
    return(result)

def bestStudentAndAvg(gradebook):
    currentHighestAverage=-10000 #a value that average cannot reach at first
    currentStudent=""
    for students in gradebook.splitlines():
        sum=0
        average=0
        count=0
        if (students.startswith("#")):
            students = ""
        #Each line should return one student with his or her grades
        for items in students.split(","):
            if (items.isalpha()):
                currentStudent=items
            if (items.isdigit() or items.startswith("-")):
                count+=1
                sum += int(items)
                average = sum/count
        if average >= currentHighestAverage:
            currentHighestAverage = average
            bestStudent=currentStudent #change beststudent with higher avg
    return "%s:%d"%(bestStudent,currentHighestAverage)

#################################################
# Test Functions
#################################################

def testLeastFrequentLetters():
    print('Testing leastFrequentLetters()... ', end='')
    assertEqual(leastFrequentLetters('abc def! GFE"cag!!!'), 'bd')
    assertEqual(leastFrequentLetters('abc def! GFE"cag!!!'.lower()), 'bd')
    assertEqual(leastFrequentLetters('abc def! GFE"cag!!!'.upper()), 'bd')
    assertEqual(leastFrequentLetters(''), '')
    assertEqual(leastFrequentLetters(string.punctuation), '')
    assertEqual(leastFrequentLetters(string.whitespace), '')
    assertEqual(leastFrequentLetters(string.ascii_lowercase),
                string.ascii_lowercase)
    assertEqual(leastFrequentLetters(string.ascii_uppercase),
                string.ascii_lowercase)
    noq = string.ascii_lowercase.replace('q','')
    nor = string.ascii_lowercase.replace('r','')
    nos = string.ascii_lowercase.replace('s','')
    assertEqual(leastFrequentLetters(string.ascii_lowercase + noq), 'q')
    assertEqual(leastFrequentLetters(nor + string.ascii_lowercase), 'r')
    assertEqual(leastFrequentLetters(nos + nor + ' aaa ' +
                                     5*string.ascii_lowercase), 'rs')
    print('Passed.')

def testBestStudentAndAvg():
    print("Testing bestStudentAndAvg()...", end="")
    gradebook = """
# ignore  blank lines and lines starting  with  #'s
wilma,91,93
fred,80,85,90,95,100
betty,88
"""
    assertEqual(bestStudentAndAvg(gradebook), "wilma:92")
    gradebook   =   """
#   ignore  blank   lines   and lines   starting    with    #'s
wilma,93,95

fred,80,85,90,95,100
betty,88
"""
    assertEqual(bestStudentAndAvg(gradebook), "wilma:94")
    gradebook = "fred,0"
    assertEqual(bestStudentAndAvg(gradebook), "fred:0")
    gradebook = "fred,-1\nwilma,-2"
    assertEqual(bestStudentAndAvg(gradebook), "fred:-1")
    gradebook = "fred,100"
    assertEqual(bestStudentAndAvg(gradebook), "fred:100")
    gradebook = "fred,100,110"
    assertEqual(bestStudentAndAvg(gradebook), "fred:105")
    gradebook = "fred,49\nwilma" + ",50"*50
    assertEqual(bestStudentAndAvg(gradebook), "wilma:50")
    print("Passed!")

#################################################
# Main
#################################################

def main():
    lintAll()
    testAll(
        testLeastFrequentLetters,
        testBestStudentAndAvg,
    )

if __name__ == '__main__':
    main()
