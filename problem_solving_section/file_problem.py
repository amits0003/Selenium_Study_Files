import glob
import os

current_path = os.getcwd()
files_list = os.listdir("C:\\CCM\\NewWebTestingProject\\problem_solving_section\\pythonmysql")

print(current_path)
for file_name in files_list:
    #if not (file_name.startswith(".") or file_name.startswith("_")):
    if not (file_name.__contains__(".")):
        with open(file_name,'r') as fopen:
            fread = fopen.readlines()

        for line in fread:
            print(line)
