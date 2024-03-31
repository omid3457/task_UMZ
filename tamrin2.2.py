li = ['ali', 1233, 0, "", [], {}, 'False', '0', 'None', None, -1, [1, 2, 3], {'key': 'value'}, True, ' ', '[]',
'[1, 2, 3]', '{}', '{"a": 1}', 'True', 'ali', '1234', 1, 0.1, -0.1, True, ' ', '[]', '[1, 2, 3]', '{}', '{"a": 1}',
'True', 'ali', '1234', 1, 0.1, -0.1, True, ' ', '[]', '[1, 2, 3]', '{}', '{"a": 1}', 'True', 'ali', '1234', 1, 0.1, -0.1]


def solve_puzzle(puzzles):
	answer = []
	for i in puzzles:
		if isinstance(i, int) or isinstance(i, float):
			if i == 0:
				answer.append("False")
			else:
				answer.append('True')
		elif i is True or i is None:
			if i:
				answer.append('True')
			elif i is None:
				answer.append("None")
		else:
			if len(i) == 0:
				answer.append("False")
			else:
				answer.append('True')
	return answer


print(solve_puzzle(li))
