#      2+4+7-5+3

# Basic Calculator to run on Ubuntu Linux CORE


def bracController(open, close):
	# The Controller method to do math of stuff inside the braces [ALSO CALLED THEORY OF BRACES]
	open = list(reversed(open)) #Reverse the arrangements of the list
	for i in open:
		# Conclude(''.join(chars[int(open[i] + 1):int(close[i])]))
		cmd = chars[int(open[i])+1:int(close[i])]
		ans = Conclude(''.join(cmd))
		chars[int(open[i]):int(close[i])+1] = str(ans)


def divController(divIndex):
	# The Division Handler
	for i in divIndex:
		ans = int(chars[int(i)-1]) / int(chars[int(1)+1])
		chars[int(i)-1:int(i)+1] = ans


def mulController(mulIndex):
	#The Multiplication Handler
	for i in mulIndex:
		ans = int(chars[int(i)-1]) * int(chars[int(1)+1])
		chars[int(i)-1:int(i)+1] = ans


def addController(addIndex):
	#The Addition Handler
	for i in addIndex:
		ans = int(chars[int(i)-1]) + int(chars[int(i)+1]) #Add two freaking numbers >:-(
		chars[int(i)-1:int(i)+1] = ans #Replace the goddamn numbers and the operators


def subController(subIndex):
	#The Substraction Handler
	for i in subIndex:
		ans = int(chars[int(i)-1]) - int(chars[int(1)+1])
		chars[int(i)-1:int(i)+1] = ans


#Taking Input from the User
print("Type your problem in this format :: 2+5-6+2")
query = input("Calculator :: ")
query.replace(" ", "")
query = str(query)
chars = []

#Referencing Further

def Conclude(q):
	addOpIndex = []
	subOpIndex = []
	mulOpIndex = []
	divOpIndex = []
	bracOpenIndex = []
	bracCloseIndex = []
	for x in q:
        chars.append(x)

    for i in chars:
		addOpIndex = [i for i, x in enumerate(chars) if x == "+"]
		subOpIndex = [i for i, x in enumerate(chars) if x == "-"]
		mulOpIndex = [i for i, x in enumerate(chars) if x == "*"]
		divOpIndex = [i for i, x in enumerate(chars) if x == "/"]
		bracOpenIndex = [i for i, x in enumerate(chars) if x == "("]
		bracCloseIndex = [i for i, x in enumerate(chars) if x == ")"]

    bracController(bracOpenIndex, bracCloseIndex)
    divController(divOpIndex)
    mulController(mulOpIndex)
    addController(addOpIndex)
    subController(subOpIndex)
    return ''.join(chars)


print(Conclude(query)) # Taking Function
