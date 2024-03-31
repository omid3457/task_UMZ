def rand(d, start=0, end=10):
	guess = d*(end - start) * start
	return guess


x, y, z = map(int, input('x : start, y : end, z : number : ').split(' '))
f = 0.1
for i in range(z):
	print(rand(f, x, y))
	f += 0.07
