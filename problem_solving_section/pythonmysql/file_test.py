import os

files_list = os.listdir("C:\\CCM\\NewWebTestingProject\\problem_solving_section\\pythonmysql")
print(files_list)

for file in files_list:
    if not file.endswith("."):
        with open(file, 'r') as fopen:
            fread = fopen.readlines()
            for line in fread:
                #pass
                print(line)