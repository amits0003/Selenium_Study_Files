#
# #Rearrange sorted list in max/min form
# #Input: [1,2,3,4,5]
# #Output: [5,1,4,2,3]
#
# lista = [1,2,3,4,5]
#
# listb = []
# #
# # for _ in range(len(lista)):
# #     max_number = max(lista)
# #     listb.append(max_number)
# #     lista.remove(max_number)
# #     min_number = min(lista)
# #     listb.append(min_number)
# #     lista.remove(min_number)
#
# list_asc  = sorted(lista, reverse=False)
# list_desc = sorted(lista, reverse=True)
#
# print(list_asc)
# print(list_desc)
#
# index = 0
# while index != len(lista):
#     listb.append(list_asc[index])
#
#
# print(listb)
# import requests
# get_call = requests.get("https://reqres.in/api/users")
#
# data_ = get_call.text
#
# print(data_)

# 1 5 6 8 2 4 6 2 4 8 5 2 1 4 7 9 6 3

# str1 = "1 5 6 8 2 4 6 2 4 8 5 2 1 4 7 9 6 3"
#
# list1 = list(map(int, str1.split(" ")))
#
# print(list(set(list1)))

#1 2 3
#4 5 6
#7 8 9

# list_of_list = [[1,2,3],[4,5,6],[7,8,9]]
#
# for index, ele in enumerate(list_of_list):
#     print(ele[index])
#
# index1= len(list_of_list)
# list2 = []
# while index1 != 1:
#     list2.append(list_of_list[index1][index1])
#     index1 = index1-1
#
# print(list2)


# Enter your code here. Read input from STDIN. Print output to STDOUT



