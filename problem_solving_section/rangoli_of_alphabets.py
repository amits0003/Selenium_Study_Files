import string

n: int = 5
print(string.ascii_lowercase)
list_alpha = []
for ele in string.ascii_lowercase:
    list_alpha.append(ele)
print(list_alpha)

index = 0

endl = n
endm = n


# while endl != 1:
#     print(list_alpha[endl-1], end='-')
#     endl = endl-1
#
# while index <5:
#     print(list_alpha[index], end='-')
#     index = index+1

list_str = []
asc = string.ascii_lowercase
for idx1 in range(n):
    str1 = "-".join(asc[idx1:n])
    list_str.append((str1[::-1]+str1[1:]).center((4*n)-3, '-'))
print('\n'.join(list_str[:0:-1]+list_str))
