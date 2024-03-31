import string
pro = ',.?!'


def func3(word):
	for h in word:
		if h in pro:
			return True
	return False


def func2(word):
	d = False
	d1 = False
	for k in word:
		if k in string.ascii_lowercase:
			d = True
		if k in string.ascii_uppercase:
			d1 = True
		if d1 and d:
			return True
	return False


def func(password):
	if len(password) >= 8 and func2(password) and func3(password):
		return True
	else:
		return False


def win():
	li = []
	x = tuple(input('split usernames by space : ').split(' '))
	for i in range(1, len(x), 2):
		if func(x[i]):
			li.append(x[i - 1])
	return li


print(win())
