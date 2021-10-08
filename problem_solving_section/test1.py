arr = [10,-44,-13,23,2,3]

# To find the res = max multliplication of any three number. multiplication of three largest numbers

temp1,temp2,temp3 = 0,0,0

temp1= max(arr)

arr.remove(temp1)

temp2 = max(arr)

arr.remove(temp2)

temp3 = max(arr)

res = temp1*temp2*temp3

print(temp1, temp2, temp3)
print(res)
