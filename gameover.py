from turtle import Turtle, Screen
import scores
import snake
import scores
import main


reason = None


def restart_game():
    snake.all_turtles = []
    snake.game_on = True
    scores.current_score = 0
    main.main()


def game_over():
    global reason
    screen1 = Screen()
    screen1.clear()
    screen1.bgcolor("Black")
    over = Turtle()
    over.hideturtle()
    over.color("white")
    s = f'''Game Over
({reason})
==========
Final Score : {scores.current_score}'''
    over.write(s, False, "center", ("Arial", 40, 'normal'))
    over.color("dark gray")
    s = "Press \"r\" to restart."
    over.penup()
    over.sety(-100)
    over.write(s, False, "center", ("Arial", 20, 'normal'))
    screen1.onkey(restart_game, "r")
