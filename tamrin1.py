text = input()


def digit(temp):
	number = '0123456789'
	d = 0
	for j in temp:
		if j in number:
			d += 1
	return d


if digit(text) == len(text):
	text = int(text)
	print(type(text), text)
elif digit(text) == len(text) - 1:
	text = float(text)
	print(type(text), text)
elif not text.isdigit():
	if text[0] == '[' and text[-1] == ']':
		text = list(text)
		text.remove('[')
		text.remove(']')
		a = text.count(',')
		for i in range(a):
			text.remove(',')
	print(type(text), text)
else:
	print(type(text), text)

