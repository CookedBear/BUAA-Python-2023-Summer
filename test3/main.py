target = float(input())

length = 2
total = 0
step = 0

while total < target:
    step += 1
    total += length
    length *= 0.98

print(step)
