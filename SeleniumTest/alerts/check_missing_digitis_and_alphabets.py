def isDigit(ch):
    ch = ord(ch)
    if ord('0') <= ch <= ord('9'):
        return True
    return False


def missingCharacters(string_given):
    # present = [False for i in range(MAX)]

    # Write your code here
    list_from_string = []
    stringone_nine = '0123456789'
    list_one_nine = []
    extract_digit_list = []
    extract_aplhabets_list = []

    string_abc = "abcdefghijklmnopqrstuvwxyz"
    list_abc= []

    final_temp_list_digit = []
    final_temp_list_alpha = []

    for digit in stringone_nine:
        list_one_nine.append(digit)
    for char in string_abc:
        list_abc.append(char)


    for element in string_given :
        list_from_string.append(element)


    for index, value in enumerate(list_from_string):
        if isDigit(value):
            extract_digit_list.append(value)
        else:
            extract_aplhabets_list.append(value)

    for i in list_one_nine:
        if i not in extract_digit_list:
            final_temp_list_digit.append(i)

    for i1 in list_abc:
        if i1 not in extract_aplhabets_list:
            final_temp_list_alpha.append(i1)


    temp_list = final_temp_list_digit+final_temp_list_alpha

    stringA = ""
    for ele in temp_list:
        stringA = stringA+ str(ele)

    print(stringA)


    #print(extract_digit_list)
    #print(extract_aplhabets_list)


if __name__ == "__main__":
    s = '7985interdisciplinary12'
    missingCharacters(s)
