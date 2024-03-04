while 1:
	command = input("enter command : ").lower()
	if command == "exit":
		print("****goodbye!!***")
		break
	elif command == "sum":
		a, b = map(float, input("please enter your command : ").split("+"))
		print("answer : ", a + b)
	elif command == "difference":
		a, b = map(float, input("please enter your command : ").split("-"))
		print("answer : ", a - b)
	elif command == "multiple":
		a, b = map(float, input('please enter your command : ').split("*"))
		print('answer : ', a * b)
	elif command == "divide":
		a, b = map(float, input('please enter your command : ').split('/'))
		print("answer : ", a / b)
	else:
		print('wrong input')
	print("-" * 30)
