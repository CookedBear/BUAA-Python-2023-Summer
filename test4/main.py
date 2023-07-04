def sorter(a, b):
    if a > b:
        return b, a
    else:
        return a, b


ax1, ay1, ax2, ay2 = map(int, input().split())
bx1, by1, bx2, by2 = map(int, input().split())

ax1, ax2 = sorter(ax1, ax2)
ay1, ay2 = sorter(ay1, ay2)
bx1, bx2 = sorter(bx1, bx2)
by1, by2 = sorter(by1, by2)

if min(ax2, bx2) > max(ax1, bx1) and min(ay2, by2) > max(ay1, by1):
    print((min(ax2, bx2) - max(ax1, bx1)) * (min(ay2, by2) - max(ay1, by1)))
else:
    print(0)
