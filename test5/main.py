def priority(op):
    if op in "*/":
        return 2
    elif op in "+-":
        return 1
    else:
        return 0


operation = input()
result = list()
stack = list()

for c in operation:
    if c.isdigit():
        result.append(c)
    else:
        if c == ')':
            while True:
                popper = stack.pop()
                if popper != '(':
                    result.append(popper)
                else:
                    break
        elif not stack or c == '(' or stack[-1] == '(' or \
                priority(c) > priority(stack[-1]):
            stack.append(c)
        else:
            while True:
                if stack and stack[-1] != '(' and \
                        priority(c) <= priority(stack[-1]):
                    result.append(stack.pop())
                else:
                    stack.append(c)
                    break

stack.reverse()
result.extend(stack)

print("".join(result))
