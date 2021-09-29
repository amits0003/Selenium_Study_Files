def diagonalDifference(arr):
    # Write your code here
    list_a = []
    list_b = []
    abc, bcd = 0, 0
    for idx in range(len(arr)):
        abc += arr[idx][idx]
        bcd += arr[idx][-idx - 1]

    return abs(abc - bcd)


if __name__ == "__main__":
    n = int(input("Enter the number of rows").strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input("Enter the numbers separated by space ").rstrip().split())))

    print("diagonal difference is : ", diagonalDifference(arr))
