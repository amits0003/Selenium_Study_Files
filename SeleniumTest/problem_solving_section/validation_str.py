# Given a string s containing just the characters
# '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

s = input("Enter the Sentence starting with the bracket")

if s.startswith('(') and s.endswith(')'):
    print(True)
elif s.startswith('{') and s.endswith('}'):
    print(True)
elif s.startswith('[') and s.endswith(']'):
    print(True)
else:
    if s.startswith('{'):
        if not s.endswith('}'):
            print("} is missing")
    elif s.startswith('['):
        if not s.endswith(']'):
            print("] is missing")
    elif s.startswith('('):
        if not s.endswith(')'):
            print(") is missing")

    if s.endswith('}') :
        if not s.startswith('{'):
            print("{ is missing")
    elif s.endswith(']') :
        if not s.startswith('['):
            print("[ is missing")

    if s.endswith(')') :
        if not s.startswith('('):
            print("( is missing")

var1, var2, var3, var4, var5, var6 = '{'
list_se = []
for ele in s :
    if ele not in list_se:
        list_se.append(ele)
        if ele



