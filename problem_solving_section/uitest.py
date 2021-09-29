
'''

'''
# lista = [1,2,43,20,21,30]
#
# max_num = max(lista)
# listb = []
#
# for ele in lista:
#     if ele!= max_num:
#         listb.append(ele)
#
# print(max(listb))

stra = 'abcbab'
strb = ''
index = len(stra)
print(index)

while index != 0:
    strb = strb + stra[index-1]
    index = index-1

if stra == strb:
    print("pallindrome")
else:
    print('not pallidrome')

str1 = 'abcds'
list3 = []
for ele in str1:
    list3.append(ele)

print(list3)

str4 = ''

for ele in list3:
    str4 = str4 + str(ele)

print(str4)

def hello(func):
    print("Hello")


def hellob():
    print("hellob")


hellob()