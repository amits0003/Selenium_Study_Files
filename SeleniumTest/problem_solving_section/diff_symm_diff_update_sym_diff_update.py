# A = int(input("Enter the length of set"))
# A = input("Enter the elements sepereated by comma")
# N = int(input("input the number of other sets"))
# list_of_set = []
# while(N!=0):
#     other_set = input("enter the nummers seperated by comma, press enter when done etnering one set")
#     list_of_set.append(other_set)
#     N = N-1
#
# print(list_of_set)
#
# for index, ele in enumerate(list_of_set):
#     ele = set(ele)
#     set(A).intersection_update(ele)
#     print('intersection_update',len(A))
#     print(A)
#     set(A).update(ele)
#     print('update',len(A))
#     print(A)
#     set(A).symmetric_difference_update(ele)
#     print('symmetric_difference_update',len(A))
#     print(A)
#     set(A).difference_update(ele)
#     print('difference_update',len(A))
#     print(A)
A = '1 2 3 4 5 6 7 8 9 10 11 12 13 14 24 52'
new_a = A.split(" ")
set_a = set(new_a)
B = '2 3 5 6 8 9 1 4 7 11'
new_b = B.split(" ")
set_b = set(new_b)
C = '55 66'
new_c = C.split(" ")
set_c = set(new_c)
D = '22 7 35 62 58'
new_d = D.split(" ")
set_d = set(new_d)
E = '11 22 35 55 58 62 66'
new_e = E.split(" ")
set_e = set(new_e)

set_a.intersection_update(set_b)
print(set_a)
set_a.update(set_c)
print(set_a)
set_a.symmetric_difference_update(set_d)
print(set_a)
set_a.difference_update(set_e)
print(set_a)


