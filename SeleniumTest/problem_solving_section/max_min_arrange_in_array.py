array = [6, 7, 78, 3, 4, 5, 6, 2]


def arrange_arr(arr):
    n = len(arr)
    temp = n * [None]

    small, large = 0, n - 1

    flag = True

    for i in range(n):
        if flag is True:
            temp[i] = arr[large]
            large -= 1
        else:
            temp[i] = arr[small]
            small += 1

        flag = bool(1 - flag)

    for i in range(n):
        arr[i] = temp[i]

    return arr

print('m')