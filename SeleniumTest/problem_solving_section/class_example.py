# Python program to show that the variables with a value
# assigned in class declaration, are class variables

# Class for Computer Science Student
class CSStudent:
    stream = 'cse'  # Class Variable
    count = 0

    def __init__(self, name, roll):
        self.name = name  # Instance Variable
        self.roll = roll
        CSStudent.count += 1


# object creation
a = CSStudent('Amit', 1)
b = CSStudent('Sumit', 2)
c = CSStudent('a0', 3)

print(a.stream)
print(b.stream)
print(CSStudent.count)
