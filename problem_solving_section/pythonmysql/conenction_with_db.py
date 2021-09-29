"""
Write a function that takes an array of integers and returns th
"""


def average(arr1):
    len_arr = len(arr1)
    res, avg = 0, 0

    for ele in arr1:
        res = res + ele

    avg = res / len_arr

    return avg


if __name__ == "__main__":
    user_input = list(map(int, input("Enter the number speerated by space").split()))

    print("Average result = \t ", average(user_input))
