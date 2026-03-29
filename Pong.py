import turtle

# Window setup
wn = turtle.Screen()
wn.title("Pong Game")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Scores
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.35
ball.dy = 0.35

# Score display
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# Paddle movement flags
paddle_a_up_flag = False
paddle_a_down_flag = False
paddle_b_up_flag = False
paddle_b_down_flag = False

# Paddle movement speed
paddle_speed = 1  # super slow

# Paddle movement functions
def paddle_a_up_press():
    global paddle_a_up_flag
    paddle_a_up_flag = True
def paddle_a_up_release():
    global paddle_a_up_flag
    paddle_a_up_flag = False
def paddle_a_down_press():
    global paddle_a_down_flag
    paddle_a_down_flag = True
def paddle_a_down_release():
    global paddle_a_down_flag
    paddle_a_down_flag = False
def paddle_b_up_press():
    global paddle_b_up_flag
    paddle_b_up_flag = True
def paddle_b_up_release():
    global paddle_b_up_flag
    paddle_b_up_flag = False
def paddle_b_down_press():
    global paddle_b_down_flag
    paddle_b_down_flag = True
def paddle_b_down_release():
    global paddle_b_down_flag
    paddle_b_down_flag = False

# Keyboard bindings
wn.listen()
wn.onkeypress(paddle_a_up_press, "w")
wn.onkeyrelease(paddle_a_up_release, "w")
wn.onkeypress(paddle_a_down_press, "s")
wn.onkeyrelease(paddle_a_down_release, "s")
wn.onkeypress(paddle_b_up_press, "Up")
wn.onkeyrelease(paddle_b_up_release, "Up")
wn.onkeypress(paddle_b_down_press, "Down")
wn.onkeyrelease(paddle_b_down_release, "Down")

# Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Move paddles
    if paddle_a_up_flag and paddle_a.ycor() < 250:
        paddle_a.sety(paddle_a.ycor() + paddle_speed)
    if paddle_a_down_flag and paddle_a.ycor() > -240:
        paddle_a.sety(paddle_a.ycor() - paddle_speed)
    if paddle_b_up_flag and paddle_b.ycor() < 250:
        paddle_b.sety(paddle_b.ycor() + paddle_speed)
    if paddle_b_down_flag and paddle_b.ycor() > -240:
        paddle_b.sety(paddle_b.ycor() - paddle_speed)

    # Border checking (top/bottom wall)
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.dy *= -1

    # Ball goes past paddles → update score
    if ball.xcor() > 390:
        score_a += 1
        pen.clear()
        pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    if ball.xcor() < -390:
        score_b += 1
        pen.clear()
        pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    # Paddle collisions
    if (340 < ball.xcor() < 350) and (paddle_b.ycor() + 50 > ball.ycor() > paddle_b.ycor() - 50):
        ball.dx *= -1

    if (-350 < ball.xcor() < -340) and (paddle_a.ycor() + 50 > ball.ycor() > paddle_a.ycor() - 50):
        ball.dx *= -1
