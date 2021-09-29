
class Sample:
    def __init__(self):
        pass

    def display(self, lista):
        dict_a  = {}
        lista = list((int(val) for val in lista))
        count = 0
        temp = []
        for index, element in enumerate(lista):
            if element not in dict_a.keys():
                #dict_a[element] = element
                if element not in temp:
                    temp.append(element)
                dict_a[element] = len(temp)



        print(dict_a)


        #print(lista)

obj1 = Sample()

input_list = input("Enter the numbers").split(" ")

obj1.display(input_list)



a = int(input("enter the number you want"))
b = 4 #int(input("enter the number of item you want to see int the list"))

# divide in to b parts such that the sum of element = a

sum_num = 0

list_num = []
index = 0
sum_res = 0
temp3 = 0
ele_to_add = 0
if a > b:
    while b != 0:
        val = a
        temp = val % b
        if temp != 0:
            list_num.append(temp)
        else:
            temp = val % (b + 1)
            list_num.append(temp)
        val = a - temp

        b = b - 1
        b = str(b).upper()
    for ele in list_num:
        sum_res = sum_res + ele

    if sum_res == a:
        print(list_num)
    else:
        if sum_res > a:
            temp3 = sum_res - a
        else:
            temp3 = a - sum_res

        for index, ele in enumerate(list_num):
            if index == len(list_num) - 1:
                ele_to_add = temp3 + ele
                list_num.pop()
                list_num.append(ele_to_add)
        print(list_num)
else:
    print("Number to be divided is less or equal the number of item in which it is divided")