from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
# starting an animation
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

# listening screen events
screen.listen()

screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.right, key="Right")
screen.onkey(fun=snake.left, key="Left")

# updating animation
screen.update()

# moving the snake
is_game_on = True

while is_game_on:
    screen.update()

    # slowing down the snake
    time.sleep(0.1)
    snake.move()
    # detecting collision with food
    if snake.head.distance(food) < 15:
        snake.extend()
        food.refresh()
        scoreboard.increase_score()
    # detecting collision with wall
    if snake.head.xcor() < -290 or snake.head.xcor() > 290 or snake.head.ycor() < -290 or snake.head.ycor() > 290:
        # 2.
        scoreboard.reset()
        snake.reset()

    # detecting collision with a tail
    # excluding snake.head from the checking.
    for s in snake.snake_body[1:]:
        if snake.head.distance(s) < 10:
            # 2.
            scoreboard.reset()
            snake.reset()


screen.exitonclick()
