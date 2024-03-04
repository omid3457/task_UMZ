import turtle

length = int(input())
color = input()
shape = input()
s = turtle.Screen()
t = turtle.Turtle()
t.shape(shape)
t.color(color)
for i in range(4):
	t.fd(length)
	t.lt(90)
s.mainloop()
