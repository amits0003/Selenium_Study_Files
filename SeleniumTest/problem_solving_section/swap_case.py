

s = 'abs'
t = ''

for ele in s :
    if ele.islower():
        ele = ele.upper()
    elif ele.isupper():
        ele = ele.lower()
    t = t + ele


print(t)

