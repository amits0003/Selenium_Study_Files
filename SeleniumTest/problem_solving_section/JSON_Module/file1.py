dict_a = {
    "GE Healthcare": [
        {
            "firstName": "John",
            "lastName": "Doe",
            "age": 23,
            "department": "accounting"
        },
        {
            "firstName": "Sally",
            "lastName": "Green",
            "age": 27,
            "department": "sales"
        }
    ],
    "GE Aviation": [
        {
            "firstName": "Mary",
            "lastName": "Smith",
            "age": 32,
            "department": "accounting"
        },
        {
            "firstName": "Jim",
            "lastName": "Galley",
            "age": 41,
            "department": "sales"
        }
    ]
}

class my_dict(dict):
    def __init__(self):
        self = dict()

    def add(self,key,value):
        self[key] = value

listA = []
listB = []
temp_idx = 0
new_dict = {}

dict_obj = my_dict()

for index, elements in dict_a.items():
    for index1, values1 in enumerate(elements):
        print(index, values1)







