# n = int(input())
# arr = map(int, input().split())
#
# arr1 = list(arr)
# max_value = max(arr1)
# new_list = []
# for ele in arr1:
#     if ele != max_value:
#         new_list.append(ele)
#
# print(max(new_list))

nested_list = []

for _ in range(int(input("Enter the number of Students\t"))):
    name = input("Enter the student name\t")
    score = float(input("Enter the Score of student \t"))
    nested_list.append([name, score])


for list1 in nested_list:
    for index in list1:
        print(list1[1][index])