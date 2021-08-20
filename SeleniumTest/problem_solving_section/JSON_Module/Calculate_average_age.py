import  json

f_ptr = open('file.json')

data_ = json.load(f_ptr)
list_bu = []
dit_age  = {}
for index, value in data_.items():
    if index not in list_bu:
        list_bu.append(index)
    for indexN, valueN in enumerate(list_bu):
        print(indexN, valueN)


print(list_bu)