
def count_substring(stringa, sub_stringa):
    temp = ''
    count = 0

    for index in range(len(stringa)):
        if stringa.startswith(sub_stringa,index):
            count = count+1

    return count


if __name__ == "__main__":
    stringA = 'ABCDCDC'
    sub_stringA = 'CDC'
    res = count_substring(stringA, sub_stringA)
    print(res)



#-------------------------------------------------------------------------------------------------------------
    #
    # while idx != len(stringa):
    #     # print(idx)
    #     temp = stringa[idx:len(stringa)]
    #     # print(temp)
    #     if sub_stringa in temp:
    #         print('amit')
    #
    #     idx = idx +1
