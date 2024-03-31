from random import randint
from time import perf_counter


def game():
	answer = []
	start = perf_counter()
	while 1:
		num = randint(0, 16)
		print(bin(num))
		guess = int(input(' enter guess : '))
		if guess == num:
			answer.append('True')
		else:
			answer.append('False')
		end = perf_counter()
		if end - start >= 20:
			break
	return answer


print(game())
