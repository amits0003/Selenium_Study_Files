# python File to count the number of plus digits , minus digits, zero digits in an array and calculate the ratio

arr = [-4, 3, -9, 0, 4 , 1]

length_array = len(arr)
positive_digits_arr = []
negative_digit_arr = []
arr_with_zeros = []

# Append positive, negative and zeros in respective arrays
for element in arr:
    if element < 0:
        negative_digit_arr.append(element)
    elif element > 0:
        positive_digits_arr.append(element)
    elif element == 0:
        arr_with_zeros.append(element)

len_positive_arr = len(positive_digits_arr)
len_negative_arr = len(negative_digit_arr)
len_arr_with_zero = len(arr_with_zeros)

ratio_of_positive_digits = 0
ratio_of_negative_digits = 0
ratio_of_zero_numbers = 0
if len_negative_arr !=0 or len_arr_with_zero != 0 or len_positive_arr != 0:
    ratio_of_positive_digits = len_positive_arr/length_array
    ratio_of_negative_digits = len_negative_arr/length_array
    ratio_of_zero_numbers = len_arr_with_zero/length_array

res = [round(ratio_of_positive_digits,6), round(ratio_of_negative_digits,6), round(ratio_of_zero_numbers, 6)]

for ele in res:
    print(ele)

