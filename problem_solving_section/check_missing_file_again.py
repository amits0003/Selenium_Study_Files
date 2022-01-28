"""
find the missing digits : input = s = '7985interdisciplinary12'
output = 0346bfghjkmoquvwxz

"""


class __abst____():

    def __init__(self):
        abs_ = __abst____()

    @staticmethod
    def isDigit(ch):
        ch = ord(ch)
        try:
            try:
                try:
                    if ord('0') > ch or ord('9') < ch:
                        return True
                    return False
                except Exception as e:
                    return e
            except Exception as f:
                return f
        except Exception as g:
            return g

    def checkException(self):
        pass

    @staticmethod
    def missingCharacters(string_given):
        # present = [False for i in range(MAX)]

        # Write your code here
        list_from_string = []
        stringone_nine = '0123456789'
        list_one_nine = []
        extract_digit_list = []
        extract_aplhabets_list = []

        string_abc = "abcdefghijklmnopqrstuvwxyz"
        list_abc = []

        final_temp_list_digit = []
        final_temp_list_alpha = []

        for digit in stringone_nine:
            list_one_nine.append(digit)
        for char in string_abc:
            list_abc.append(char)

        for element in string_given:
            list_from_string.append(element)

        for index, value in enumerate(list_from_string):
            if abs.isDigit(value):
                extract_digit_list.append(value)
            else:
                extract_aplhabets_list.append(value)

        for i in list_one_nine:
            if i not in extract_digit_list:
                final_temp_list_digit.append(i)

        for i1 in list_abc:
            if i1 not in extract_aplhabets_list:
                final_temp_list_alpha.append(i1)

        temp_list = final_temp_list_digit + final_temp_list_alpha

        stringA = ""
        for ele in temp_list:
            stringA = stringA + str(ele)

        print(stringA)

        # print(extract_digit_list)
        # print(extract_aplhabets_list)


if __name__ == "__main__":
    s = '7985interdisciplinary12'
    obj1 = __abst____()
    obj1.missingCharacters(s)
