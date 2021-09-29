def approach1():

    N = int(input("Enter Number"))

    listA = (input("Enter names").split() for _ in range(N))

    unique_list = []

    for ele in listA :
        if ele not in unique_list:
            unique_list.append(ele)

    print(len(unique_list))

#----------------------------#

def approach2():
    print(len(set([str(input("Enter Name")) for x in range(int(input("Enter Number")))])))


approach2()


def getMultiplicationResult(a, b):
    result = 0
    for _ in range(b):
        result = result + a

    return result

#
# print(getMultiplicationResult(2, 3))
# print(getMultiplicationResult(-2, 3))
# print(getMultiplicationResult(2, -3))
# print(getMultiplicationResult(2, 0))
# print(getMultiplicationResult(0, -3))
# print(getMultiplicationResult(1, -3))
# print(getMultiplicationResult(-1, -3))
# print(getMultiplicationResult(0, 0))
# print(getMultiplicationResult(199, 566))
# print(getMultiplicationResult(19988, 566777))
# print(getMultiplicationResult(199, -5543435435366))
# print(getMultiplicationResult(5, 5345455355353535566))
# print(getMultiplicationResult(19535353535359, 66))
