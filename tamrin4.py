while 1:
	command = input('choose from fahrenheit or celsius : ')
	if command == "exit":
		print('***goodbye!!!***')
		break
	elif command == 'fahrenheit':
		temp = float(input('enter temperature : '))
		print("answer : ", (temp - 32) * 5 / 9)
	elif command == 'celsius':
		temp = float(input('enter temperature : '))
		print('answer : ', temp * 9 / 5 + 32)
	else:
		print('wrong input')
	print('-' * 30)
