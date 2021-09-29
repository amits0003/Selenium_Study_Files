from collections import Counter

List1 = [1, 2, 2, 3, 2, 3, 2, 3, 1, 3, 2, 4, 5, 4, 5, 5, 2, 5, 2, 45, 23, 2, 3, 2, 2, 1, 2, 3, 2]

# Count the frequency of the elements of array
l2 = Counter(List1)

# print(l2)

# Storing the Key Value pair in Tuple.

t1 = list(Counter(List1).items())
# print(t1)

# Printing the Keys from the Counter Keys

l3 = list(Counter(List1).keys())
# print(l3)
# Printing he Values against the Counter Keys

l4 = list(Counter(List1).values())
print(l4)

"""-------------------------------------------------------------------------------------------------------------------- """

X = input()
shoes_list = Counter(map(int, input().split()))
N = input()
for _ in range(N):
    size, prices = list(map(int, input().split()))

res = 0
for ele in prices:
    res = res + ele

print(res)
