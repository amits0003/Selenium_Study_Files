#--------------------prog 1---------------------
n = 6
# for i in range(1,n):
#     for j in range(i,n,1):
#         print('', end=""+'#')
#     print()

# lista = input("Enter Two integers ").split(" ")
#
# print(lista)
# res = 0
#
# for ele in lista:
#     res = res + int(ele)
#
# print(res)

# value1 = input()
#
# res1 = int(value1)//10
#
# res2 = int(value1)  - (int(res1*10))
#
# print(res2)

# value1 = input("Enter")
# len1 = len(value1)
# for index, value in enumerate(value1):
#     if index == len(value1)-1:
#         print(value)
#         break

n = int(input())
rem = 0
while(n>0):
    rem = n%10
    n = n//10

print(rem)


# number_of_tc = input("Number of TestCases")
#
# list_new = []
# for ele in range(int(number_of_tc)):
#     ele = input("Enter the Hour and Minute").split(" ")
#     list_new.append(ele)
#
# print(list_new)
#
# angle_per_minute = 3
#
# if