m = input()
n = input()
sum = 0

try:
    int(m)
    int(n)
except ValueError:
    print("illegal input")
    exit()

list = [int(m), int(n)]
for i in range(18):
    list.append(list[len(list) - 2] + list[len(list) - 1])

for i in list:
    sum += i
print(sum)
