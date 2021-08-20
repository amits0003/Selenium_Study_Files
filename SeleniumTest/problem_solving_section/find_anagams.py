
str = [2,3,9,6,4,7]

max_value = 0
list_new = []
for element in str:
    if element > max_value:
        max_value = element

for index, value in enumerate(str):
    if value != max_value:
        list_new.append(value)

str.remove(9)

print(list_new)




