# from collections import defaultdict
#
# d = defaultdict(list)
#
# print(d)
# d['python'].append("awesome")
#
# d['something-else'].append("not relevant")
# print(d)
# # d['python'].append("language")
# # for i in d.items():
# #
# #     print(i)
n = 17
for i in range(1, n + 1):
    length = len('{0:b}'.format(n))
    length = int(length)
    print('{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}'.format(i, width=length))
