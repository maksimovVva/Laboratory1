OPERAND_TO_PRIORITY = {
    '(': 0,
    ')': 0,
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2
}


def parse(line):
    if len(line) == 0:
        print("ERROR: empty string!")
        return None
    res = ""
    stack = []
    i = 0
    d = 0
    lastDigFl = False
    lastDig = ""
    while i < len(line):
        if line[i].isdigit() or line[i] == ".":
            if lastDigFl or (i > 0 and line[i-1] == ')'):
                nextDig = ""
                while i < len(line) and (line[i].isdigit() or line[i] == "."):
                    nextDig += line[i]
                    i += 1
                if lastDigFl:
                    print("ERROR: incorrect combination - \"", lastDig, nextDig + "\"")
                else:
                    print("ERROR: incorrect combination - \" )", nextDig, "\"")
                return None
            if line[i] == ".":
                res += '0'
            lastDig = ""
            while i < len(line) and (line[i].isdigit() or line[i] == "."):
                res += line[i]
                lastDig += line[i]
                i += 1
            i -= 1
            if line[i] == ".":
                res += '0'
            res += " "
            lastDigFl = True
        elif line[i] == "(":
            if lastDigFl:
                print("ERROR: incorrect combination - \"", lastDig, "(\"")
                return None
            elif i > 0 and line[i-1] == ')':
                print("ERROR: incorrect combination - \" ) ( \"")
                return None
            d += 1
            stack.append(line[i])
            lastDigFl = False
        elif line[i] == ")":
            d -= 1
            if d < 0:
                print("ERROR: incorrect bracket alignment!")
                return None
            if i > 0 and (line[i-1] == '+' or line[i-1] == '-' or line[i-1] == '*' or line[i-1] == '/' or line[i-1] == '('):
                print("ERROR: incorrect combination - \"", line[i-1], line[i], "\"")
                return None
            while stack[-1] != "(":
                res += stack[-1] + " "
                stack.pop()
            stack.pop()
            lastDigFl = False
        elif line[i] == '*' or line[i] == '/' or line[i] == '+' or line[i] == '-':
            if i == 0:
                print("ERROR: incorrect beginning of string - \"" + line[i] + "\"")
                return None
            elif line[i-1] == '*' or line[i-1] == '/' or line[i-1] == '+' or line[i-1] == '-' or line[i-1] == '(':
                print("ERROR: incorrect combination - \"", line[i - 1], line[i],"\"")
                return None
            if i == len(line) - 1:
                print("ERROR: incorrect end of string - \"" + line[i] + "\"")
                return None
            priority = OPERAND_TO_PRIORITY[line[i]]
            while len(stack) != 0 and priority <= OPERAND_TO_PRIORITY[stack[-1]]:
                res += stack[-1] + " "
                stack.pop()
            stack.append(line[i])
            lastDigFl = False
        elif line[i] == " ":
            line = line[:i] + line [i+1:]
            i -= 1
        else:
            print("ERROR: incorrect token - \"" + line[i] + "\"")
            return None
        i += 1
    if d > 0:
        print("ERROR: incorrect bracket alignment!")
        return None
    while len(stack) != 0:
        res += stack[-1] + " "
        stack.pop()
    return res[:-1]
