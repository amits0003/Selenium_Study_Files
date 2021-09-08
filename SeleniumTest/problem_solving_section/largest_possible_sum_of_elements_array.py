"""
You have been given an array of integers. Your Task is to find the maximum possible
sum of elements of the array such that it is divisible by three

Input                 output
5                      18
3 6 5 1 8

Sol  :
Make an array to store the cumulative with modulo 3

cumArr[0] = largest sum which is divisible by 3
cumArr[1] = largest sum when divided by 3 leaves rem  = 1
cumArr[2] = largest sum when divided by 3 leaves remo = 2

"""


def maxSumDivThree(Arr):
    cumm_Arr = [0, 0, 0]
    for ar in Arr:
        for i in cumm_Arr[:]:
            cumm_Arr[(i + ar) % 3] = max(cumm_Arr[(i + ar) % 3], i + ar)

    return cumm_Arr[0]

if __name__ == "__main__":
    in_arr = list(map(int, input("Enter the numbers").split()))

    print("Max Possible sum is : \t ", maxSumDivThree(in_arr))
