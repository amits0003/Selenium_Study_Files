"""
2
.*\+
.*+
"""
import re

res = ".*\+"

T = int(input("Enter number"))

for _ in range(T):
    s = input("Enter string")
    s_new  = r".*\+"
    try:
        re.compile(s)
        print(True)
    except re.error as e:
        print(False)

    #print(flag)
