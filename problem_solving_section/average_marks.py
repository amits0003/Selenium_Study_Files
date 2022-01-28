if __name__ == '__main__':
    n = int(input("Enter Numebr of Students"))
    student_marks = {}
    marks_list = []
    average_marks = 0.0
    total_marks = 0.0
    for _ in range(n):
        name, *line = input("Enter student Name and marks seperated by white space").split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input("Enter the Student name to know the his average Marks : \t")

    for name, marks in student_marks.items():
        if query_name.strip() in name:
            print(name, marks)
            print(name, type(marks))
            for ele in marks:
                marks_list.append(ele)
                total_marks = total_marks + ele

            average_marks = total_marks / len(marks)

    print("Average Marks for ",query_name, 'is '.format(average_marks))