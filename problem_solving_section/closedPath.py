
def closedPath(number):
    count = 0
    for ele in str(number):
        num = int(ele)
        if num in [0,4,6,9]:
            count = count+1
        elif num in [8]:
            count = count +2
        else:
            pass
    return count



print(closedPath(63081))
