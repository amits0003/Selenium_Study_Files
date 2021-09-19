
def v_patter(n):
    space = (n*2)-2

    for i in range(1,n+1):
        for j in range(1, i+1):
            print(j, end='')

        for k in range(1, space+1):
            print(end=' ')
        space = space-2

        for j in range(i,0,-1): # 5,4,3,2,1,0
            print(j, end='')
        print()


if __name__ == "__main__":
    n = int(input("Enter the value"))
    v_patter(n)
