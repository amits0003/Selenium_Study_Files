

name = "amit 1umar sumit kumar"
Capital_name = []
list_name = name.split(" ")
# print(list_name[0][0].upper()+list_name[0][1:], list_name[1][0].upper()+list_name[1][1:])
first_name, last_name = [], []
mod_f_name, mod_l_name = [], []
for index, ele in enumerate(list_name):
    for idx, char in enumerate(ele):
        if idx == 0 and char :
            Capital_name.append((ele[0].upper()+ele[1:]))

res = ''

for ele in Capital_name:
    res = res+" "+ele

print(res.strip())
print(name[:].split())
for element in name[:].split():
    name = name.replace(element, element.capitalize())

print(name)

