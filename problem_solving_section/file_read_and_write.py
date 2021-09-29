
with open("file1.txt", 'r') as reader:
    content = reader.readlines()
    reversed(content)

    with open("file1.txt", 'w') as writer:
        for line in reversed(content):
            writer.write(line)
