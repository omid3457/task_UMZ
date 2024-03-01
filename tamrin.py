money = float(0)
while 1:
	command = input('enter your action : ').lower()
	if command == 'exit':
		print('***goodbye!!!***')
		break
	elif command == 'add':
		command2 = input("choose from my or others : ").lower()
		if command2 == 'my':
			money = money + float(input("enter number : "))
		elif command2 == 'others':
			x = float(input('please enter how much : '))
			if x > money:
				print('the input number is higher than your money(', money, ')')
			else:
				account = input('please enter account :')
				if len(account) != 16:
					print('wrong account')
				else:
					print('your sending money to : default name')
					a = input('are you sure? : ').lower()
					if a == 'yes':
						money = money - x
						print('completed')
					elif a == 'no':
						print('action terminated')
					else:
						print('wrong input')
		else:
			print('wrong input')
	elif command == 'withdraw':
		if money <= 0:
			print('you are low on money')
		else:
			d = float(input('enter number : '))
			if d > money:
				print('the input number is higher than your money(', money, ')')
			else:
				money = money - d
	elif command == 'account':
		print('account : ', money)
	else:
		print('wrong input')
	print('enter "exit" when your are finished')
	print('-'*50)
