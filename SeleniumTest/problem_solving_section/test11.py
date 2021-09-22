"""
scenario : Test Scenario for : -ve, +ve case. automate the testcase , Load Testing
covin- app, pin-code, city name -
hospitals, age wise slots, free and paid slots.
"""

"""
TC 1 - +ve 
    1. 6 Digit Pincode. - checking repsonse - 1. Hopsital Na
    -ve 
    2. less digit  Pincode 5 digits ,   - -resppone, 
            4 , 3, 2, 1
    3. passing null as pin code , paassing emptty stringas pin doe 
    4. characters used in pin code - 
    
    2. +ve,1 - full city naem , abbriviation, 
    3. pass incorrect city names -  response. 
    """

stringa = 'aaabbbbxxx'
"""
'a3b4x3'
"""

def getResult(stringB):
    count = 0
    res = ''
    for ele in stringB:
        if ele not in res:
            count = stringB.count(ele)
            res = res + ele + str(count)
    return res


print(getResult(stringa))

print(getResult('abababababc'))
print(getResult('bbbbaaaxxx'))
print(getResult('aaa0bbb1xx4'))
print(getResult('ababbbaxxx'))
print(getResult(''))
print(getResult(True))


