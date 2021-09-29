if __name__ == '__main__':
    s = 'qA2'

    res = False
    for ele in s:
        if ele.isalnum():
            res = True
            break
    print(res)

    res1 = False
    for ele in s:
        if ele.isalpha():
            res1 = True
            break
    print(res1)

    res2 = False
    for ele in s:
        if ele.isnumeric():
            res2 = True
            break
    print(res2)

    res3 = False
    for ele in s:
        if ele.islower():
            res3 = True
            break
    print(res3)

    res4 = False
    for ele in s:
        if ele.isupper():
            res4 = True
            break
    print(res4)



























    # for ele in s:
    #     if ele.isalnum():
    #         print(True)
    #     else:
    #         print(False)
    #
    #     if ele.isalpha():
    #         print(True)
    #     else:
    #         print(False)
    #
    #     if ele.isnumeric():
    #         print(True)
    #     else:
    #         print(False)
    #
    #     if ele.islower():
    #         print(True)
    #     else:
    #         print(False)
    #
    #     if ele.isupper():
    #         print(True)
    #     else:
    #         print(False)
