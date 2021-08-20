
import se
stringa = 'i have No items'

# some number item
# no items
# return last items if there are more than 1

list_str = stringa.split(" ")

print(list_str)
list_new = []
list_num = []

# def abc():
#     num = None
#     for index, item in enumerate(list_str):
#         if item.isdigit():
#             num = item
#             # while index != len(list_str):
#             #     if item.isdigit():
#             #         list_new.append([item, list_str[index+1]])
#             #     index = index+1
#             #     break
#         else:
#             return num
#             break
number = None
index = 0
while index != len(list_str):
    if list_str[index].isdigit():
        number = int(list_str[index])
    index = index+1


print(number)

# print(list_new)
# res = int(list_new[-1][0])

# print(res)

