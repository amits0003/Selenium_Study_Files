"""
i = 1, j = 1   | > control moves to new line
i = 2 , j = 1,2
i = 3 , j = 1,2,3
i = 4 , j = 1,2,3,4
i = n , j = 1,2,3,4, .., n
w
"""


def one_patter(n):
    for idx in range(1,n+1):
        for j in range(1,idx+1):
            print(j, end=" ")
        print("")


if __name__ == "__main__":
    try:
        n = int(input("Enter the value of n to print the matrix"))
        one_patter(n)
    except:
        print("invalid value")
