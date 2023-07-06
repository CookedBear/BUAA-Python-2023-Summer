str1 = input()
str2 = input()

if len(str1) == 0:
    print(len(str2))
    exit()
elif len(str2) == 0:
    print(len(str1))
    exit()

m, n = len(str1), len(str2)
matrix = [[0] * (n + 1) for i in range(m + 1)]

for i in range(1, m + 1):
    matrix[i][0] = i
for j in range(1, n + 1):
    matrix[0][j] = j

for i in range(0, m):
    for j in range(0, n):
        add = 0
        if str1[i] == str2[j]:
            add = 0
        else:
            add = 1
        matrix[i + 1][j + 1] = min(matrix[i][j] + add, min(matrix[i][j + 1] + 1, matrix[i + 1][j] + 1))

print(matrix[m][n])
