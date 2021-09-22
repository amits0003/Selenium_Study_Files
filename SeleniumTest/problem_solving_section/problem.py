#
# fopen = open('file1.txt', 'r+')
#
# arr1 = fopen.readlines()
# temp = ''
# for index, value in enumerate(arr1):
#     if "Capgemini" in value:
#         temp = 'Company'
#     elif "Company" in value:
#         temp = "Capgemini"
#
#
#
# arr2 = fopen.readlines()
# print(arr2)
#
# test = { 1 :
#              { 5 :
#                    {8:
#                         { 10: "final"}
#                     }
#                }
#          }
#
# for key, value in test.items():
#     for key1, value1 in value.items():
#         for key2, value2 in value1.items():
#             print(value1[key2][10])
#
#
# email_format = 'amit.kumar@gmail.com'
#
#
# regex = '$[a-z][A-Z]d[0-9]@[a-z][A-Z].[a-z][A-Z]^'
#
# import re
#
# #re.match()
# re.search(regex, email_format, True)

str1 = "12363416"
list = ['a','b''c','d','e','f']
temp = ''
res = ''


# for index, value in enumerate(str1):
#     ascii(1)

import requests
# latitude , logntitude,

url = 'www.google.com'

attr = requests.get(url)

print(attr)
# C:\logs\a1.log

import logging

