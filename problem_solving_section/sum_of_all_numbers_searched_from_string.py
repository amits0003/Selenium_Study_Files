"""
Problem Statement  :- Count the total of numbers in alphanumeric String
 Input:- abc123xyz23mno04pqr08
 Output:- 158
#
"""
import re
str1 = 'abc123xyz23mno04pqr08'

index = 0
lista = []

number = [ele for idx, ele in enumerate(str1) if ele.isdigit()]

print(number)
list_of_numbers = []
# for index,element in enumerate(str1):
#     temp = ''
#     if str1[index].isdigit():
#         temp += str1[index]
#         index +=1
#     else:
#         pass
#     print(temp)
temp = re.findall(r'\d+', str1)
print(temp)
#res = list(map(int, temp))

#print(res)







