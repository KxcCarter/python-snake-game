from turtle import Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snek Game")
screen.tracer(0)

snake = Snake()


def end_game():
    global game_is_on
    game_is_on = False


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(end_game, "space")


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.2)
    snake.move()











screen.exitonclick()