'''Count the number of objects created
Consider a class having multiple methods.
# filename: moduleA
class A():
def abc():
def pqr():
def printNoObj():

Implement a method that prints the number of objects created as part of execution.

for example:

# in moduleB.py
obj = A()
obj.abc()

# in moduleC.py
obj = A()
obj.abc()

# in moduleD.py
# Call to printNoObj()
Output:
No. of A objects created = 2

'''

class a:
    count = 0
    def __init__(self):
        a.count +=1


    def abc(self):
        print("hello")
    def bcd(self):
        print('hello')

obj1 = a()
obj2 = a()
obj3 = a()

print(a.count)


