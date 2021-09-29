"""
find all the followings  in a unstrcutured content of file
a. all the emails
b. all the phone numbers
c. all the ip address
"""

import re

with open('file1.txt', 'r' ) as fptr:
    contents = fptr.readlines()

for ele in contents:
    number_list = re.findall('[0-9]+', ele)

    email_list = re.findall('\S+@\S+', ele)

    ip_address = re.findall('[0-1]+.+[2-5]+.+[2-5]+.+[2-5]+', ele)      #10.255.255.254

    print(number_list)
    print(email_list)
    print(ip_address)
#count the number of folder, number of files, number of different extesions in the directory
"""
    *
    * *
    * * *
    * *
    *
    
    rows = 5, cols = 3 
    
"""

def star_patter(col_len):
    for index in range(1,col_len+1):
        print("*"*index,end=" ")
        print()
    while col_len:
        print("*"*(col_len-1))
        col_len = col_len-1

star_patter(10)

"""
list number  =  [1,3,4,6,7,8,10,11,12,13,15,16,18,19,20,21,22]
print the continuous sequence of maximum length
n = [1,2,3,4,5,7,8]
"""

def find_continous_sequence_length():
    list_number = [1, 3, 4, 6, 7, 8, 10, 11, 12, 13, 15, 16, 18, 19, 20, 21, 22]
    temp_list = []
    sub_list= []
    len_temp_list = 0

    for index, value in enumerate(list_number):
        if index not in list_number:
            if index not in temp_list:
                pass
            temp_list.append(sub_list)

    print(temp_list)

find_continous_sequence_length()





