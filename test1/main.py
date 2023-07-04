integer = input()

try:
    integer = int(integer)
except Exception:
    print(-1)
    exit()
if integer > 999 or integer < 100:
    print(-1)
    exit()
else:
    list1 = list(str(integer))
    list1.reverse()
    print(int("".join(list1)))
