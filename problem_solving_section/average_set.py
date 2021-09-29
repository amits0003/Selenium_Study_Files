def average(array):
    # your code goes here
    #set_score = set(array)

    length_set = len(array)

    result = sum(array)/length_set

    return result



if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

