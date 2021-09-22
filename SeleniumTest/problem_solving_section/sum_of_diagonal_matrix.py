arr1 = [[1, -2, 3], [4, 55, 6], [-7, 8, 9]]

list_a = []
list_b = []

for index, value in enumerate(arr1):
    temp = value[index]
    temp2= value[len(value)-(index+1)]
    list_a.append(temp)
    list_b.append(temp2)
    print(value)

temp = 0
for ele in list_a:
    temp = temp+ele

temp2 = 0
for ele in list_b:
    temp2 = temp2+ele
 
res = 0

res = abs(temp)-abs(temp2)

print(temp)
print(temp2)

print(abs(res))

