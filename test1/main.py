class Stu:
    def __init__(self, name, score, position):
        self.name = name
        self.score = score
        self.position = position

    def __lt__(self, b):
        if (self.score < b.score) or (self.score == b.score and self.position > b.position):
            return False
        else:
            return True


number = int(input())
box = []

for i in range(number):
    name, score = input().split()
    score = int(score)
    box.append(Stu(name, score, i))

box.sort()

for i in range(number):
    print("{: >15}{: >5}".format(box[i].name, box[i].score))
