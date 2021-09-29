num = int(input('Enter the Number\t'))
if num > 1:
    for i in range(2,num):
        if num % i == 0:
            print('Not prime')
            break
        else:
            print('prime')
            break
elif num == 1:
    print('1 is prime')
else:
    print(' 0 or negative number')