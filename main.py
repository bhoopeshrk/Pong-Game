# Import required library
import turtle
import ctypes

Screen = ctypes.windll.user32

Screen_Width = int(Screen.GetSystemMetrics(0))
Screen_Height = int(Screen.GetSystemMetrics(1))

# Create game_screenreen
game_screen = turtle.Screen()
game_screen.title("PONG GAME")
game_screen.bgcolor("black")
game_screen.setup(width=Screen_Width, height=Screen_Height)

# Left paddle
pad_A = turtle.Turtle()
pad_A.speed(0)
pad_A.shape("square")
pad_A.color("blue")
pad_A.shapesize(stretch_wid=8, stretch_len=1)
pad_A.penup()
pad_A.goto(-(Screen_Width/2)+200, 0)

# Right paddle
pad_B = turtle.Turtle()
pad_B.speed(0)
pad_B.shape("square")
pad_B.color("green")
pad_B.shapesize(stretch_wid=8, stretch_len=1)
pad_B.penup()
pad_B.goto((Screen_Width/2)-200, 0)

# Ball of circle shape
Ball = turtle.Turtle()
Ball.speed(10)
Ball.shape("circle")
Ball.color("red")
Ball.penup()
Ball.goto(0, 0)
Ball.dx = 5
Ball.dy = -10

# Initialize the score
Player_A = 0
Player_B = 0

# Displays the score
Score_board = turtle.Turtle()
Score_board.speed(0)
Score_board.color("yellow")
Score_board.penup()
Score_board.hideturtle()
Score_board.goto(0, (Screen_Height/2)-100)
Score_board.write("Player A : 0  |  Player B : 0", align="center", font=("Courier", 24, "normal"))

# Functions to move paddle vertically
def paddle_Aup():
	y = pad_A.ycor()
	y += 20
	pad_A.sety(y)

def paddle_Adown():
	y = pad_A.ycor()
	y -= 20
	pad_A.sety(y)

def paddle_Bup():
	y = pad_B.ycor()
	y += 20
	pad_B.sety(y)

def paddle_Bdown():
	y = pad_B.ycor()
	y -= 20
	pad_B.sety(y)

# Keyboard bindings
game_screen.listen()
game_screen.onkeypress(paddle_Aup, "e")
game_screen.onkeypress(paddle_Adown, "d")
game_screen.onkeypress(paddle_Bup, "Up")
game_screen.onkeypress(paddle_Bdown, "Down")

while True:
    game_screen.update()
    
    Ball.setx(Ball.xcor()+Ball.dx)
    Ball.sety(Ball.ycor()+Ball.dy)

	# Checking borders
    if Ball.ycor() > (Screen_Height/2)-150:
        Ball.sety((Screen_Height/2)-150)
        Ball.dy *= -1

    if Ball.ycor() < -(Screen_Height/2)+150:
        Ball.sety(-(Screen_Height/2)+150)
        Ball.dy *= -1

    if Ball.xcor() > (Screen_Width/2)-200:
        Ball.goto(0, 0)
        Ball.dy *= -1
        Player_B += 1
        Score_board.clear()
        Score_board.write("Player A : {}  |  Player B : {}".format(Player_B, Player_A), align="center", font=("Courier", 24, "normal"))

    if Ball.xcor() < -(Screen_Width/2)+200:
        Ball.goto(0, 0)
        Ball.dy *= -1
        Player_A += 1
        Score_board.clear()
        Score_board.write("Player A : {}  |  Player B : {}".format(Player_B, Player_A), align="center", font=("Courier", 24, "normal"))

	# Ball collision on paddle B
    if (Ball.xcor() > (Screen_Width/2)-220 and Ball.xcor() < (Screen_Width/2)-210) and (Ball.ycor() < pad_B.ycor()+70 and Ball.ycor() > pad_B.ycor()-70):
        Ball.setx((Screen_Width/2)-220)
        Ball.dx*=-1
        Player_A += 1
        Score_board.clear()
        Score_board.write("Player A : {}  |  Player B : {}".format(Player_B, Player_A), align="center", font=("Courier", 24, "normal"))
		
    # Ball collision on paddle A
    if (Ball.xcor() > -(Screen_Width/2)+210 and Ball.xcor() < -(Screen_Width/2)+220) and (Ball.ycor() < pad_A.ycor()+70 and Ball.ycor() > pad_A.ycor()-70):
        Ball.setx(-(Screen_Width/2)+220)
        Ball.dx*=-1
        Player_B += 1
        Score_board.clear()
        Score_board.write("Player A : {}  |  Player B : {}".format(Player_B, Player_A), align="center", font=("Courier", 24, "normal"))
