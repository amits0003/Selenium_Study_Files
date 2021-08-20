

n = 1012

list_n = []
# Write your code here
for ele in str(n):
    ele = int(ele)
    if ele != 0:
        if n % ele == 0:
            list_n.append(ele)

print(len(list_n))