import turtle

drawing_board=turtle.Screen()
drawing_board.title("Python Turtle")
drawing_board.bgcolor("light blue")

turtle_instance=turtle.Turtle()

def turtle_forward():
    turtle_instance.forward(100)

def rotate_angle_right():
    turtle_instance.right(50)


def rotate_angle_left():
    turtle_instance.left(50)

def clear_screen():
    turtle_instance.clear()

def turtle_return_home():
    turtle_instance.penup()
    turtle_instance.home()
    turtle_instance.pendown()

def turtle_pen_up():
    turtle_instance.penup()

def turtle_pen_down():
    turtle_instance.pendown()


drawing_board.listen()
drawing_board.onkey(turtle_forward,"space")
drawing_board.onkey(rotate_angle_left,"Left")
drawing_board.onkey(rotate_angle_right,"Right")
drawing_board.onkey(clear_screen,"c")
drawing_board.onkey(turtle_return_home,"h")
drawing_board.onkey(turtle_pen_up,"u")
drawing_board.onkey(turtle_pen_down,"d")

turtle.mainloop()

