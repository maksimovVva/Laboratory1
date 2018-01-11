OPERAND_TO_PRIORITY = {
    '(': 0,
    ')': 0,
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2
}


def checkCorrect(line):
    err = None
    if len(line) == 0:
        err = "empty string!"
        return err
    i = 0
    d = 0
    while i < len(line):
        if line[i] == "(":
            d += 1
        elif line[i] == ")":
            d -= 1
            if d < 0:
                err = "incorrect bracket alignment!"
                break
        elif line[i] == '*' or line[i] == '/' or line[i] == '+' or line[i] == '-':
            if i == 0:
                err = "incorrect beginning of string - \"" + line[i] + "\""
                break
            elif (not line[i - 1].isdigit()) and line[i - 1] != '.' and line[i - 1] != ')':
                err = "incorrect combination - \"" + line[i - 1] + line[i] + "\""
                break
            if i == len(line) - 1:
                err = "incorrect end of string - \"" + line[i] + "\""
                break
            elif (not line[i + 1].isdigit()) and line[i + 1] != '.' and line[i + 1] != '(':
                err = "incorrect combination - \"" + line[i] + line[i + 1] + "\""
                break
        elif (not line[i].isdigit()) and line[i] != ".":
            err = "incorrect token - \"" + line[i] + "\""
            break
        i += 1
    if d > 0 and err is None:
        err = "incorrect bracket alignment!"
    return err


def parse(line):
    line = line.replace(" ", "")
    err = checkCorrect(line)
    if err is not None:
        print("ERROR: ", err)
        return None
    res = ""
    stack = []
    i = 0
    while i < len(line):
        if line[i].isdigit() or line[i] == ".":
            if line[i] == ".":
                res += '0'
            while i < len(line) and (line[i].isdigit() or line[i] == "."):
                res += line[i]
                i += 1
            i -= 1
            if line[i] == ".":
                res += '0'
            res += " "
        elif line[i] == "(":
            stack.append(line[i])
        elif line[i] == ")":
            while stack[-1] != "(":
                res += stack[-1] + " "
                stack.pop()
            stack.pop()
        elif line[i] == '*' or line[i] == '/' or line[i] == '+' or line[i] == '-':
            priority = OPERAND_TO_PRIORITY[line[i]]
            while len(stack) != 0 and priority <= OPERAND_TO_PRIORITY[stack[-1]]:
                res += stack[-1] + " "
                stack.pop()
            stack.append(line[i])
        i += 1
    while len(stack) != 0:
        res += stack[-1] + " "
        stack.pop()
    return res[:-1]
