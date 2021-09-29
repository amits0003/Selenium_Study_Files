# if __name__ == '__main__':
#     n = int(input("Enter Number of Students"))
#     list_s = []
#     second_lowest = 0
#     for _ in range(n):
#         temp = []
#
#         student = input("Enter the name")
#         marks = float(input("enter the marks"))
#
#         list_s.append([student, marks])
#
#     order_student_list = sorted(list_s, key=lambda x: float(x[1]))
#
#     print(order_student_list)
#
#     for i in range(n):
#         if order_student_list[i][1] != order_student_list[0][1]:
#             second_lowest = order_student_list[i][1]
#             break
#
#     student_with_second_lowest_grade = [x[0] for x in order_student_list if x[1] == second_lowest]
#
#     student_with_second_lowest_grade.sort()
#
#     for name in student_with_second_lowest_grade:
#         print(name)


def s2():
    #N = int(input())
    list1 = []
    list1.insert(0, 5)
    list1.insert(1, 10)
    list1.insert(0, 6)
    print(list1)
    list1.remove(6)
    list1.append(9)
    list1.append(1)
    list1.sort()
    print(list1)
    list1.pop()
    list1.reverse()
    print(list1)

def s3():
    x = ()
    n = (x for x in range(int(input("Enter range"))))
    integer_list = tuple(map(int, input("Enter number").split()))
    #print(n)
    print(hash(integer_list))



def er23():
    T = int(input('enter input'))

    for _ in range(T):
        a, b = input("enter").split()
        # a,b= int(a), int(b)
        try:
            print(int(a) / int(b))
        except ZeroDivisionError as e:
            print("Error Code:", e)

er23()