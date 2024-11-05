from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

right_paddle = Paddle(350, 0)
left_paddle = Paddle(-350,0)

game_is_on = True
screen.listen()
while game_is_on:
    screen.onkey(right_paddle.move_up, "w")
    screen.onkey(right_paddle.move_down, "s")

    screen.onkey(left_paddle.move_up, "Up")
    screen.onkey(left_paddle.move_down, "Down")

    screen.update()


screen.exitonclick()