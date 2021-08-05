arr = [1, 2, 3, 5, 6]
arr1 = [4, 3, 2, 5, 99,-2]

min_list = []
max_list = []
temp = 0
min_temp = []

for index, value in enumerate(arr1):
    print(index)

    if value > temp:
        temp = value
    else:
        min_list.append(value)



print(min_list)

