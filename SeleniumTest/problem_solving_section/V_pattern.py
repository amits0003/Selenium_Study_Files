

n = 5
space = 8

# for i in range(n+1):
#     k = i+1
#     if(k!=n+1):
#         print(" "*(n-k)+'*'*k)

for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end='')

    for k in range(1, space+1):
        print(end=' ')
    space = space-2

    for j in range(i,0,-1): # 5,4,3,2,1,0
        print(j, end='')
    print()
