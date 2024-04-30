data_list = []
countA, countB = 0, 0
statement = ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3', 'd1', 'd2', 'd3']
for i in range(12):
	data_list.append(None)
data_list[2] = True
print(
"""a1 = "C and I meet today"
a2 = "B is thief"
a3 = "thief did not know who car was for"
b1 = "D is not thief"
b2 = "d3 is lying"
b3 = "i am not thief"
c1 = "i have not met A yet"
c2 = "B is not thief"
c3 = "D knows how to drive"
d1 = "b1 is lying"
d2 = "I don't know how to drive"
d3 = "A is thief""")
print("-" * 30)
if input('is a1 statement is right? (yes or no): ').lower() == 'yes':
	data_list[0], data_list[6] = True, False
else:
	data_list[6], data_list[0] = True, False
if input('is b1 statement is right? (yes or no): ').lower() == 'yes':
	data_list[3], data_list[9] = True, False
else:
	data_list[9], data_list[3] = True, False
if input('is b2 statement is right? (yes or no): ').lower() == 'yes':
	data_list[4], data_list[11] = True, False
else:
	data_list[11], data_list[4] = True, False
if input('is c3 statement is right? (yes or no): ').lower() == 'yes':
	data_list[8], data_list[10] = True, False
else:
	data_list[10], data_list[8] = True, False
print(data_list)
for i in data_list:
	if i:
		countA += 1
	elif i == False:
		countB += 1
print(f"truth={countA},lie={countB}")
print("you most choose c2,a2,b3 statements in a way that lies = 6 and truths = 6")
if input("is b3 statement correct?(yes/no): ").lower() == "no":
	data_list[5], data_list[1], data_list[7] = False, True, False
else:
	data_list[5], data_list[1], data_list[7] = True, False, True
countB, countA = 0, 0
for item in data_list:
	if item:
		countA += 1
	elif not item:
		countB += 1
if countB == countA:
	for i in range(12):
		print(f'{statement[i]} is {data_list[i]}', end=',')
	print('the number of lies and truths ar equal')
	print('b is thief!!! nice job')
else:
	print('sorry the thief ran away!!!!')
