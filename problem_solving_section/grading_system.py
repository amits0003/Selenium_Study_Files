# Approach 1 --------------------------------------------------

'''
arr_grades = [73,67,38,33]
res = []
multiple_of_5_above_40 = []

for ele in range(41,100):
    if ele%5 ==0 :
        multiple_of_5_above_40.append(ele)

print(multiple_of_5_above_40)

for index, value in enumerate(arr_grades):
    if value < 38:
        res.append(value)
    elif 38<=value<=40:
        res.append(40)
    elif 40<value<=45:
        if 45-value <3:
            res.append(45)
        else:
            res.append(value)
    elif 45<value<=50:
        if 50-value <3:
            res.append(50)
        else:
            res.append(value)
    elif 50<value<=55:
        if 55-value<3:
            res.append(55)
        else:
            res.append(value)
    elif 55<value<=60:
        if 60-value<3:
            res.append(60)
        else:
            res.append(value)
    elif 60<value<=65:
        if 65-value<3:
            res.append(65)
        else:
            res.append(value)
    elif 65<value<=70:
        if 70-value<3:
            res.append(70)
        else:
            res.append(value)
    elif 70<value<=75:
        if 75-value<3:
            res.append(75)
        else:
            res.append(value)
    elif 75<value<=80:
        if 80-value<3:
            res.append(80)
        else:
            res.append(value)
    elif 80<value<=85:
        if 85-value<3:
            res.append(85)
        else:
            res.append(value)
    elif 85<value<=90:
        if 90-value<3:
            res.append(90)
        else:
            res.append(value)
    elif 90<value<=95:
        if 95-value<3:
            res.append(95)
        else:
            res.append(value)
    elif 95<value<=100:
        if 100-value<3:
            res.append(100)
        else:
            res.append(value)

for ele in res:
    print(ele)
'''
# ---------------------------------------------------------------------------------------
# count = 0
# for index1 , value1 in enumerate(multiple_of_5_above_40):
#     if value1<arr_grades[count]<=multiple_of_5_above_40[index1+1]:
#         if multiple_of_5_above_40[index1+1]-arr_grades[index1]<3:
#             res.append(multiple_of_5_above_40[index1+1])
#         else:
#             res.append(arr_grades[index1])
#     else:
#         count = count+1


# =================================================================================

# if value>40:
#     for index1, value1 in enumerate(multiple_of_5_above_40):
#         if value < value1 and value1 - value <3:
#             res.append(value1)
#         elif value<value1 and value1-value>3:
#             res.append(value)


# =====================================================================================
from typing import List, Union, Any


def test_return_grades():
    arr_grades: List[Union[int, Any]] = [73, 67, 38, 33, 3, 45, 90, 91, 57, 58, 94]
    res = []
    for index, value in enumerate(arr_grades):
        if value < 38:
            res.append(value)
        if value >= 38:
            if value % 5 == 3:
                value += 2
                res.append(value)
            elif value % 5 == 4:
                value += 1
                res.append(value)
            else:
                res.append(value)

    print(res)


if __name__ == "__main__":
    test_return_grades()