import math


def isprimebad(n):
    if n < 2:
        return False
    else:
        for i in range(2, int(math.sqrt(n))):
            if n % i == 0:
                return False
        return True


print(isprimebad(15))


def alldistinct(a, b, c):
    if a != b:
        if b != c:
            if a != c:
                result = True
            else:
                result = False
        else:
            result = False
    else:
        result = False

    return result

def evenpositions(l):
  if len(l) == 0:
    return([])
  else:
    return list(l[index] for index, value in enumerate(l) if index % 2 == 0)
       # Complete the recursive call below this line


def cubefree(n):
  if n == 1:
    return True
  for i in range(2, int(n ** (1 / 3) + 1)):
    if n % (i * i * i) == 0:
      return False

  return True


def listdiff(l1, l2):
  check1 = list(item for item in l2 if item not in l1)
  check2 = list(item for item in l1 if item not in l2)

  return (check2, check1)


l2 = []
count = 0
def deldup(l):
  for item in l:
    count = l.count(item)
    if count == 1:
      l2.append(item)

  return l2


