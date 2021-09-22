
def reverse_the_number():
    try:
        number_input = int(input("Enter the Number"))
        rem = 0
        if number_input>0:
            while number_input > 0:
                rem = number_input % 10
                print(rem, end='')
                number_input = number_input // 10

            print('\nthe first number without conversion of the number is ', rem)
        elif number_input ==0:
            print("Number given is 0")
        else:
            temp = str(number_input)
            number_to_convert = int(temp[1:])
            print('-', end='')
            while number_to_convert > 0:
                rem = number_to_convert % 10
                print(rem, end='')
                number_to_convert = number_to_convert // 10

    except (ValueError, ArithmeticError, TypeError) as e:
        print("OOPS !! Error occurred - ", e)


def reverse_the_number_without_inbuilt_functions(number):
    res = 0
    while number:
        remainder  = number % 10
        number = number//10
        res = res + remainder

    return res


print(reverse_the_number_without_inbuilt_functions(100))
reverse_the_number()



