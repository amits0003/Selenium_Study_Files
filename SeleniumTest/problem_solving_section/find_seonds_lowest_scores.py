if __name__ == '__main__':
    list_name_score = {}
    list_name = []
    list_score = []
    try:
        for _ in range(int(input("Enter the number of input"))):
            name = input("Enter the name")
            score = float(input("Enter the Score"))
            list_name_score[name] = score
    except ValueError as e:
        print(e)

    print(list_name_score)

    for index, values in list_name_score.items():
        list_score.append(values)
list_score_ = []
for ele in list_score:
    if ele != max(list_score):
        list_score_.append(ele)


print(list_score)
print(list_score_)