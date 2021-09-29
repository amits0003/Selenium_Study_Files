
line = 'This is a string'
str_a = ""
splitter = line.split(" ")

print(type(splitter))

joiner = "-".join(splitter)

print(joiner.rstrip("\n"))