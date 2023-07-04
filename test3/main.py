str1 = input()
str2 = input()
if len(str1) < len(str2):
    str1, str2 = str2, str1

maximum = 0
cut = ""
for i in range(len(str2)):
    for j in range(i, len(str2) + 1):
        cuter = str2[i: j]
        if cuter in str1 and maximum < len(cuter):
            maximum = len(cuter)
            cut = cuter

if cut == "":
    cut = "No Answer"
print(cut)
