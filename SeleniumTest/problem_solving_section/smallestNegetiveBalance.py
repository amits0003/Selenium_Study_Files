# debts_rows = int(input('Rows').strip())
# debts_columns = int(input('Columns').strip())
#
# debts = []
#
# for _ in range(debts_rows):
#     debts.append(input("enter value").rstrip().split())
debt = [['blake', 'alex', 7], ['blake', 'alex', 3], ['alex', 'blake', 4],['blake', 'alex', 1], ['alex', 'blake', 7]]
left_name_arr = []
right_name_arr = []
left_unique_name_arr= []
right_unique_name_arr= []

for index, value in enumerate(debt):
    left_name_arr.append(value[0])
    right_name_arr.append(value[1])

for ele in left_name_arr:
    if ele not in left_unique_name_arr:
        left_unique_name_arr.append(ele)
for ele in right_name_arr:
    if ele not in right_unique_name_arr:
        right_unique_name_arr.append(ele)

sum_array = []
len_debt = len(debt)
sum = 0
for index,ele in enumerate(debt):
    for value in left_unique_name_arr:
        if value == ele[0]:
            sum += int(debt[index][2])




# print(left_name_arr)
# print(right_name_arr)
#
# print(right_unique_name_arr)
# print(left_unique_name_arr)

