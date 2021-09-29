# --------------------approach 1----------------------------------------
'''
input array : arr1 = [1, 2, 3, 4,5, 6,7,8,9]
output pattern : [9,1,8,2,7,3,6,4,5]
'''

arr = [1,2,3,4,5]

min_list = []
max_list = []
max_value = 0
min_value = 0
min_temp = []
sum_max_list = 0
sum_min_list = 0

if len(arr) <= 5:
    for index, value in enumerate(arr):
        if value > max_value:
            max_value = value
    for index, value in enumerate(arr):
        if value < arr[index-1]:
            min_value = value

    for ele in arr:
        if ele< max_value:
            min_list.append(ele)

    for ele in arr:
        if ele>min_value:
            max_list.append(ele)

    for ele in min_list:
        sum_min_list = sum_min_list+ele

    for ele in max_list:
        sum_max_list = sum_max_list+ele

    print(str(sum_min_list)+" "+str(sum_max_list))


print('max value : ', max_value)
print('min value : ', min_value)
print('max value list : ', max_list)
print('min value list :  ', min_list)

'''
# --------------------------------approach 2 ------------------------------------#
arr = [4,3,-5,-5,9]
max_value = 0
min_value = 0
list_of_sum_of_four_elements = []
temp1, temp2, temp3, temp4, temp5 = 0, 0, 0, 0, 0
if len(arr) <= 5:
    for index, value in enumerate(arr):
        print(index, value)
        if index in [1,2,3,4] :
            temp1 = temp1+value

        if index in [0,2,3,4]:
            temp2 = temp2+value

        if index in [0,1,3,4]:
            temp3 = temp3+value

        if index in [0,1,2,4]:
            temp4 = temp4+value

        if index in [0,1,2,3]:
            temp5 = temp5+value


list_of_sum_of_four_elements.append(temp1)
list_of_sum_of_four_elements.append(temp2)
list_of_sum_of_four_elements.append(temp3)
list_of_sum_of_four_elements.append(temp4)
list_of_sum_of_four_elements.append(temp5)
print(list_of_sum_of_four_elements)

# for index, value in enumerate(list_of_sum_of_four_elements):
#         if value > max_value:
#             max_value = value
# for index, value in enumerate(list_of_sum_of_four_elements):
#         if value < list_of_sum_of_four_elements[-index]:
#             min_value = value

print(max(list_of_sum_of_four_elements), min(list_of_sum_of_four_elements))

'''