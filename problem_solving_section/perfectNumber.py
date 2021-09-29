import time
def func1():
    N = int(input("Enter N"))

    # setA = list(map(str, input("Enter the words").split()))

    count = 0
    while N > 0:
        t, c = map(int, input("Enter Number").split())
        if c - t >= 2:
            count = count + 1
        N = N - 1
    print(count)


def perfectNumberUsingComprehension(number):
    start_time = time.time()
    divisorList = []
    list(divisorList.append(idx) for idx in range(1, number) if number % idx == 0)
    print(number, 'is a perfect number') if sum(divisorList) == number else print(number, 'is a perfect number')
    end_time = time.time()
    print('Total time taken : ', end_time-start_time)


def perfectNumber(number):
    start_time = time.time()
    number = int(number)
    divisorList = []
    sum_ele = 0
    for idx in range(1, number):
        if number % idx == 0:
            divisorList.append(idx)

    for ele in divisorList:
        sum_ele = sum_ele + ele
    #print(sum_ele)

    if sum_ele == number:
        print(number, 'is a perfect number')
    else:
        print(number, 'is not a perfect number')

    end_time = time.time()
    print('Total time taken : ', end_time - start_time)


for _ in range(int(input('Enter the number of values you want to check\t'))):
    perfectNumber(int(input("Enter the Number\t")))
