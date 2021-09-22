
List1 = [2, 4, 6, 2, 7, 4, 2, 7, 6, 6, 2, 8]

List2 = []

for ele in List1:
    if ele not in List2:
        List2.append(ele)

print(List2)

"""
Output should be 
Dict1= {2:4, 4:2,6:3,7:2, 8:1}
"""

dict2 = {}

for ele in List1:
    if ele in dict2:
        dict2[ele] = dict2[ele]+1
    else:
        dict2[ele] = 1

print(dict2)

