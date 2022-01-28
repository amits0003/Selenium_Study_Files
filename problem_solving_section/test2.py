# stringa = 'aaaaavvvvccceeeddd'
#
# lista = []
#
# for ele in stringa:
#     if ele not in lista:
#         lista.append(ele)
#         #print(ele, stringa.count(ele))
# print(lista)
#
# for i in range(0, len(stringa)):
#     count = 1
#     for j in range(i+1, len(stringa)):
#         if stringa[i] == stringa[j] and stringa[i] != "":
#             count = count+1
#             stringa = stringa[:j] + '0' + stringa[j+1:]
#
#     if count>1 and stringa[i] != '0':
#         print(count, stringa[i])
lista = [1,2,3,4,-6,-24,3,-3,1,3]
listb = []
listc, listd = [], []
temp = [ele for ele in lista if ele< 0 ]+ [ele for ele in lista if ele >0]

print(temp)


def display(func):

    def hello():
        print("Hello, you name is ", end='')
        func()
    return hello


@display
def print_name():
    print("Amit")

print_name()