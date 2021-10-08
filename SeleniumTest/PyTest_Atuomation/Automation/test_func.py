

def test_one():
    arr1 = [7, 6, 5, 4, 3, 2, 1]
    arr2 = []

    len_arr = len(arr1)

    while len_arr != 0:
        arr2.append(arr1[len_arr - 1])
        len_arr = len_arr - 1

    print(arr2)

    number = 7654321

    temp = str(number)
    str2 = ''
    le_temp = len(temp)
    while le_temp != 0:
        str2 = str2 + temp[le_temp - 1]
        le_temp = le_temp - 1

    print(int(str2))


"""
0,1,1,2,3,5,8
"""

limit = 10


def fibo_s(limit):
    idx = 0
    arrX = []
    while idx != limit:
        sum = (idx + 1) + idx
        arrX.append(sum)
        idx = idx + 1

    print(arrX)

    assert limit not in arrX


fibo_s(10)

arr4 = [1000, 200, 43242, 52525, 25235]

max_num = max(arr4)
arr5, arr6 = [], []
for ele in arr4:
    if ele != max_num:
        arr5.append(ele)

sec_max = max(arr5)
for ele in arr5:
    if ele != sec_max:
        arr6.append(ele)

print(max(arr6))

lis_month = ['jan', 'feb', 'mar', 'apr', 'may', 'june', 'july', 'aug', 'sept', 'nov', 'dec']

for ele in lis_month:
    # if ele.startswith('m') or ele.startswith("M") :
    #     print(ele)

    if ele[0] == 'm' or ele[0] == 'M':
        print(ele)


def fibo_s(limit):
    a, b, res, count = 0, 1, 0, 1
    if limit < 0:
        print('invalid')
    while count <= limit:
        print(res, end=" ")
        count = count + 1
        a = b
        b = res
        res = a + b

    assert limit not in res


def test_infinite_fibo():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b


obj = test_infinite_fibo()
print(obj)


def test_reverse_string():
    lista = [2, 3, 5, 7, 11]
    listb = []

    # temp = list(print(x*x, end=' ') for x in lista)

    res = lambda x, y: x * y

    print(res(5, 6))
    count = 0
    with open("file.txt", 'r') as fopen:
        obj = fopen.readlines()

    for idx in obj:
        count = count + 1

    print(count)
    stringa = 'My name is Amit'
    strb = ''

    strb = ' '.join(ele[::-1] for ele in stringa.split(" "))

    print(strb)

    assert strb != "Test Failed"
    assert strb != "Test Failed"
