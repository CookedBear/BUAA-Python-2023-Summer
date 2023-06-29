# 10, 2 , 3 , 34,89,9,98
from functools import cmp_to_key


def cmp(a, b):
    if (a + b) > (b + a):
        return -1
    else:
        return 1


user_input = input()
list = list((user_input.split(',')))
list = [x.strip() for x in list]

list.sort(key=cmp_to_key(cmp))

for x in list:
    print(x, end="")
