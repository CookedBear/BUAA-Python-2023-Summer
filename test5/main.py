import re


def remove_const(line):
    new_line = ""
    in_const = False
    for i in range(len(line)):
        if not in_const:
            if not (line[i] in "\'\""):
                new_line += line[i]
            else:
                in_const = True
        elif line[i] in "\'\"":
            in_const = False

    return new_line


def remove_single_comment(line):
    new_line = ""
    pos = line.find("//")
    if pos == -1:
        new_line = line
    else:
        new_line = line[0: pos]
        new_line += "\n"
    return new_line


def contain_multi_comment(line, state):
    if (not state and "/*" in line) or (state and "*/" in line):
        return True

    return False


def proceed_multi_comment(line, state):
    new_line = ""
    stop = 0
    for i in range(len(line) - 1):
        if line[i] == '/' and line[i + 1] == '*':
            new_line += line[stop: i]
            state = True
        if line[i] == '*' and line[i + 1] == '/':
            stop = i + 2
            state = False
    if not state:
        new_line += line[stop: len(line)]
    return new_line + '\n', state


def generate_text(new_lines):
    with open("./in.c", "r") as f1:
        # with open("./out.txt", "w") as f2:
        lines = f1.readlines()
        state = False
        for line in lines:
            if state and not contain_multi_comment(line, state):
                continue
            # print(line, end="")
            line = remove_const(line)
            # print(line, end="")
            line = remove_single_comment(line)
            # print(line)
            if contain_multi_comment(line, state):
                line, state = proceed_multi_comment(line, state)
            # print(line, end="")
            new_lines.append(line)


keywords = ["if", "else", "for", "while", "switch", "case"]
is_comment = False
new_lines = []
result = []

pattern = re.compile('|'.join(keywords))

generate_text(new_lines)
for line in new_lines:
    result.extend(pattern.findall(line))

with open("./out.txt", "w") as f2:
    for words in result:
        f2.write(words)
