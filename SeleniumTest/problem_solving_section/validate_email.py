import re
import pytest

email_pattern = r"\b[A-Za-z0-9._%+-]+@['A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"


def validate_email(email_id):
    if re.fullmatch(email_pattern, email_id):
        print(email_id, " is Valid")

    else:
        print(email_id + " is invalid")


validate_email("amit@gmail.com")


def file_open():
    with open("file1.txt", "r") as fp:
        total_lines = fp.readlines()

    count = 0

    for ele in total_lines:
        count = count + 1

    print("Total number of lines", count)
