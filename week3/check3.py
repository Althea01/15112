import string

def vowelCount(s):
    num=0
    x=0
    t=s.lower()
    
    while x < len(s):
        if t[x]=="a" or t[x]=="e" or t[x]=="i" or t[x]=="o" or t[x]=="u":
            num+=1
        x+=1
    return num
    
def interleave(s1,s2):
    x=0
    string = ""
    num=min(len(s1),len(s2))
    
    while x < num:
        string += s1[x]+s2[x]
        x+=1
    return string + s1[num:len(s1)]+s2[num:len(s2)]
    
def testVowelCount():
    print("Testing vowelCount()...", end="")
    assert(vowelCount("abcdefg") == 2)
    assert(vowelCount("ABCDEFG") == 2)
    assert(vowelCount("") == 0)
    assert(vowelCount("This is a test.  12345.") == 4)
    assert(vowelCount(string.ascii_lowercase) == 5)
    assert(vowelCount(string.ascii_lowercase*100) == 500)
    assert(vowelCount(string.ascii_uppercase) == 5)
    assert(vowelCount(string.punctuation) == 0)
    assert(vowelCount(string.whitespace) == 0)
    print("Passed!")
    
def testInterleave():
    print("Testing interleave()...", end="")
    assert(interleave("abcdefg", "abcdefg") == "aabbccddeeffgg")
    assert(interleave("abcde", "abcdefgh") == "aabbccddeefgh")
    assert(interleave("abcdefgh","abcde") == "aabbccddeefgh")
    assert(interleave("Smlksgeneg n a!", "a ie re gsadhm") ==
                      "Sam likes green eggs and ham!")
    assert(interleave("","") == "")
    print("Passed!")

testInterleave()

testVowelCount()
    
        