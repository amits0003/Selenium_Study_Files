from collections import namedtuple

mappedArr = namedtuple('mappedArr','x,y' )

pt1 = mappedArr(1,2)
pt2 = mappedArr(3,4)

res = (pt1.x * pt2.x) + (pt2.y * pt1.y)

print(res)

print(mappedArr)

print(type(mappedArr))