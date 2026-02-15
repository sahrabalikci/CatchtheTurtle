import turtle
import random

game_board = turtle.Screen()
game_board.bgcolor("lightblue")
game_board.title("Catch the Turtle")

game_over = False
score = 0

#HIGH SCORE
try:
    with open("highscore.txt", "r") as file:
        high_score = int(file.read())
except:
    high_score = 0

#SCORE
score_turtle = turtle.Turtle()
score_turtle.color("darkblue")
score_turtle.hideturtle()
score_turtle.penup()

top_height = game_board.window_height() / 2
y = top_height * 0.8
score_turtle.setpos(0, y)
score_turtle.write("Score = 0", align="center", font=("Arial", 20, "bold"))

#HIGH SCORE TURTLE
highscore_turtle = turtle.Turtle()
highscore_turtle.color("purple")
highscore_turtle.hideturtle()
highscore_turtle.penup()
highscore_turtle.setpos(0, y - 30)
highscore_turtle.write("High Score = " + str(high_score), align="center", font=("Arial", 15, "bold"))

#TIMER
countdown_turtle = turtle.Turtle()
countdown_turtle.color("darkred")
countdown_turtle.hideturtle()
countdown_turtle.penup()

#TURTLE ICON
turtle_icon = turtle.Turtle()
turtle_icon.penup()
turtle_icon.shape("turtle")
turtle_icon.color("darkgreen")


#TURTLE MOVER
def turtle_mover():
    if not game_over:
        x = random.randint(-130, 130)
        y = random.randint(-130, 130)
        turtle_icon.setpos(x, y)
        game_board.ontimer(turtle_mover, 1000)


#CLICK
def clickturtle(a, b):
    global score, high_score

    if not game_over:
        score += 1

        score_turtle.clear()
        score_turtle.write("Score = " + str(score),align="center", font=("Arial", 20, "bold"))

        # HIGH SCORE KONTROL
        if score > high_score:
            high_score = score

            highscore_turtle.clear()
            highscore_turtle.write("High Score = " + str(high_score),align="center", font=("Arial", 15, "bold"))


            with open("highscore.txt", "w") as file:
                file.write(str(high_score))


turtle_icon.onclick(clickturtle)


#COUNT DOWN
def countdown(time):
    global game_over

    top_height = game_board.window_height() / 2
    y = top_height * 0.8
    countdown_turtle.setpos(0, y - 60)

    if time > 0:
        countdown_turtle.clear()
        countdown_turtle.write("Time: {}".format(time),align="center", font=("Arial", 15, "bold"))
        game_board.ontimer(lambda: countdown(time - 1), 1000)
    else:
        game_over = True
        countdown_turtle.clear()
        countdown_turtle.write("GAME OVER!", align="center", font=("Arial", 20, "bold"))
        turtle_icon.hideturtle()



turtle_mover()
countdown(20)



game_board.mainloop()

