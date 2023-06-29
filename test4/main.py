n, m, q = map(int, input().split())

list = [(i + 1) for i in range(n)]

left = n
cnt = 0
for i in range(q-1):
    p = list.pop(0)
    list.append(p)

while left > 1:
    popper = list.pop(0)
    cnt += 1
    if cnt == m:
        cnt = 0
        left -= 1
        # print(list)
        continue
    else:
        list.append(popper)
print(list[0])
