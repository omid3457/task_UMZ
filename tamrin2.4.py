import turtle


def goto(x=0.0, y=0.0, b=True):
	if b:
		t.penup()
		t.goto(x, y)
	else:
		t.penup()
		t.goto(x, y)
		t.pendown()


def go_right(r, f, b=True):
	if b:
		t.right(r)
		t.forward(f)
	else:
		t.forward(f)
		t.right(r)


def go_left(le, f, b=True):
	if b:
		t.left(le)
		t.forward(f)
	else:
		t.forward(f)
		t.left(le)


s = turtle.Screen()
t = turtle.Turtle()
angle = 0
for i in range(3):
	go_right(90, 50)
t.penup()
for i in range(2):
	go_left(90, 20)
t.pendown()
go_right(90, 30, False)
go_left(90, 30, False)
for i in range(8):
	go_right(angle, 5, False)
	angle += 3
goto(-103.08, -20)
go_right(184, 50, False)
t.pendown()
for i in range(2):
	go_right(90, 30, False)
t.forward(50)
go_left(90, 30)
for i in range(2):
	go_right(90, 30)
goto(-141.75, -70.91, False)
t.circle(5)
goto(-75.0, -30.0, False)
t.circle(5)
goto(-85.0, -30.0, False)
t.circle(5)
goto()
s.mainloop()
