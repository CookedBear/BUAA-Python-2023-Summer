string = input()
lister = list(string)
tails = [0 for i in lister]
length = 0

for alpha in lister:
    i = 0
    j = length
    while i < j:
        m = int((i + j) / 2)
        if tails[m] <= alpha:
            i = m + 1
        else:
            j = m
    tails[i] = alpha
    if j == length:
        length += 1
print(length)
