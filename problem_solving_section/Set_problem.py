"""
M = input()
setA = set(M.split())


N = input()
listb = N.split()
setB= set(listb)

a = setA.difference(setB)
b = setB.difference(setA)

c = a.union(b)
print("\n".join(sorted(c, key=int)))
"""

"""
# Enter your code here. Read input from STDIN. Print output to STDOUT

M, m1 = (int(input()), input().split())
N, n1 = (int(input()), input().split())

x = set(m1)
y = set(n1)
a = x.difference(y)
b = y.difference(x)

c = a.union(b)
print("\n".join(sorted(c, key=int)))
"""

m, n = int(input().split()), int(input().split())
arr1 = input().split()
arr2 = input().split()


