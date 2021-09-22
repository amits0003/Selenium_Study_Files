def wrapper(f):

    def fun(l):
            f('+91 ' + ele[-10:-5] + " " + ele[-5:] for ele in l if (len(ele) > 10))
    return fun


@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')


if __name__ == '__main__':
    try:
        l = [input("Enter Mob no") for _ in range(int(input('no of inputs')))]
        sort_phone(l)
    except (ValueError,TypeError) as e:
        print('Exception: ', e)



