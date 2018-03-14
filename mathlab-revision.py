def braccontroller(open, close):
    open = list(reversed(open))
    for i in open:
        cmd = chars[int(open[i]) + 1:int(close[i])]
        ans = conclude(''.join(cmd))
        chars[int(open[i]):int(close[i]) + 1] = str(ans)


def divcontroller(divindex):
    for i in divindex:
        ans = int(chars[int(i) - 1]) / int(chars[int(1) + 1])
        del chars[int(i) - 1:int(i) + 1]
        chars.insert(int(i) - 1, ans)


def mulcontroller(mulindex):
    for i in mulindex:
        ans = int(chars[int(i) - 1]) * int(chars[int(1) + 1])
        del chars[int(i) - 1:int(i) + 1]
        chars.insert(int(i) - 1, ans)


def addcontroller(addindex):
    for i in addindex:
        ans = int(chars[int(i) - 1]) + int(chars[int(i) + 1])
        del chars[int(i) - 1:int(i) + 1]
        chars.insert(int(i) - 1, ans)


def subcontroller(subindex):
    for i in subindex:
        ans = int(chars[int(i) - 1]) - int(chars[int(1) + 1])
        del chars[int(i) - 1:int(i) + 1]
        chars.insert(int(i) - 1, ans)


print("Type your problem in this format :: 2+5-6+2")
query = input("Calculator :: ")
query.replace(" ", "")
query = str(query)
chars = []


def conclude(q):
    addopindex = []
    subopindex = []
    mulopindex = []
    divopindex = []
    bracopenindex = []
    braccloseindex = []

    for x in q:
        chars.append(x)

    for i in chars:
        addopindex = [i for i, x in enumerate(chars) if x == "+"]
        subopindex = [i for i, x in enumerate(chars) if x == "-"]
        mulopindex = [i for i, x in enumerate(chars) if x == "*"]
        divopindex = [i for i, x in enumerate(chars) if x == "/"]
        bracopenindex = [i for i, x in enumerate(chars) if x == "("]
        braccloseindex = [i for i, x in enumerate(chars) if x == ")"]

    braccontroller(bracopenindex, braccloseindex)
    divcontroller(divopindex)
    mulcontroller(mulopindex)
    addcontroller(addopindex)
    subcontroller(subopindex)
    return chars


print(conclude(query))
