message = input()
atAll = list()
atPerson = list()
while message != "no new messages":
    if message.find("@all") != -1:
        atAll.append(message)
    elif message.find("@nyima") != -1:
        atPerson.append(message)
    message = input()

atAll.sort()
for message in atAll:
    print(message)

atPerson.sort(reverse=True)
for message in atPerson:
    print(message)
