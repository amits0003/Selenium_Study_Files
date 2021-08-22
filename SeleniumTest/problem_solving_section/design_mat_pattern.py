
n = int(input('Enter the number of rows'))
m = 3*int(n)
res = []
dot = '.'
dot_stand = '.|.'
letter = 'WELCOME'
mid = n//2
counter = 1
dec_counter = 1
counter_iter2 = int((m-6)/3)



for i in range(1,n+1):
    print(str((counter*int((mid-7)/2))) + letter + str((counter*int((mid-7)/2))))
#for i in range(1,n+1)


#---------------------------------------------------
# print(5/2)
# print(5//2)
# print(5%2)
#
# for i in range(1,n+1):
#     raw =[]
#     for j in range(m):
#         raw.append([i+j])
#     res.append(raw)
#     res.append('\n')
#
# print(res)



