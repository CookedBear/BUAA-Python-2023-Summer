
def encode(alpha, key):
    if alpha.islower():
        return chr(ord("a") + (ord(alpha) - ord("a") + key) % 26)
    elif alpha.isupper():
        return chr(ord("A") + (ord(alpha) - ord("A") + key) % 26)
    else:
        return alpha


try:
    key = int(input())
except ValueError:
    print("Error input!")
    exit()

with open("./in.txt", "r") as f1:
    with open("./out.txt", "w") as f2:
        str = f1.read()
        for i in str:
            print(i, end="")
            f2.write(encode(i, key))

