import random


def random_colour():
	r = random.randint(0, 255)
	g = random.randint(0, 255)
	b = random.randint(0, 255)
	rgb_colour = (r, g, b)
	return rgb_colour


def shape_drawing_right(turtle, num_sides):
	"""Make the turtle draw different shapes based on the number of sides cw"""
	angle = 360 / num_sides
	for _ in range(num_sides):
		turtle.forward(100)
		turtle.right(angle)


def shape_drawing_left(turtle, num_sides):
	"""Makes the turtle draw different shapes based on the number of sides ccw"""
	angle = 360 / num_sides
	for _ in range(num_sides):
		turtle.right(-angle)
		turtle.backward(100)


def shape_drawing_turnaround(turtle, n1, n2):
	turtle.penup()
	turtle.setposition(-50, 300)
	turtle.pendown()
	for shape_sides in range (n1, n2):
		turtle.pencolor(random_colour())
		if shape_sides % 2 == 0:
			shape_drawing_right(turtle, shape_sides)
		else:
			shape_drawing_left(turtle, shape_sides)


def dashed_line(turtle, total_length, jump_length):
	"""Make the turtle draw a dashed line"""
	turtle.penup()
	turtle.goto(-300, 0)
	turtle.pendown()
	turtle.pencolor("CornflowerBlue")
	turtle.speed(1.5)
	for _ in range(int(total_length / 2)):
		turtle.forward(jump_length)
		turtle.pendown()
		turtle.forward(jump_length)
		turtle.penup()
	turtle.pendown()


def random_walk(turtle, total_moves):
	"""Makes the turtle walk on a random path"""
	turtle.penup()
	turtle.home()
	turtle.pendown()
	turtle.speed(1.5)
	for _ in range(total_moves):
		direction = random.choice([0, 90, 180, 270])
		turtle.pencolor(random_colour())
		turtle.forward(20)
		turtle.setheading(direction)


def spirograph(turtle, gap_size):
	"""Makes the turtle draw a multitude of overlapping circles to create a spirograph"""
	turtle.penup()
	turtle.home()
	turtle.pendown()
	turtle.pensize(2)
	turtle.speed(0)
	angle = 0
	for _ in range(int(360 / gap_size)):
		turtle.pencolor(random_colour())
		turtle.right(angle)
		angle += gap_size
		turtle.circle(100, 380)
		turtle.home()

