from turtle import *
from random import randrange

# Set up the screen
setup(420, 420)
title("Snake Game")
bgcolor("black")
tracer(0)

# Create the snake head
head = Turtle()
head.shape("square")
head.color("white")
head.penup()

# Create the food
food = Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.goto(randrange(-190, 190, 10), randrange(-190, 190, 10))

# Set the initial direction of the snake
direction = "stop"

# Set up game state
game_over = False

# Set up score and length variables
score = 0
snake_length = 1

# Create a list to hold the snake segments
segments = []

# Function to move the snake
def move():
    global game_over

    if game_over:
        return

    if direction == "up":
        y = head.ycor()
        head.sety(y + 10)
    elif direction == "down":
        y = head.ycor()
        head.sety(y - 10)
    elif direction == "left":
        x = head.xcor()
        head.setx(x - 10)
    elif direction == "right":
        x = head.xcor()
        head.setx(x + 10)

    # Call move function again after a delay
    ontimer(move, 100)  # Adjust the delay value to change the speed

    # Check for collision with the food
    if head.distance(food) < 10:
        # Increase score and length
        global score, snake_length
        score += 10
        snake_length += 1

        # Update score display
        score_display.clear()
        score_display.write(f"Score: {score}", align="center", font=("Arial", 16, "bold"))

        # Move the food to a new location
        food.goto(randrange(-190, 190, 10), randrange(-190, 190, 10))

        # Add a new segment to the snake's body
        segment = Turtle()
        segment.shape("square")
        segment.color("white")
        segment.penup()
        segments.append(segment)

    # Move the segments of the snake's body
    for i in range(len(segments) - 1, 0, -1):
        x = segments[i - 1].xcor()
        y = segments[i - 1].ycor()
        segments[i].goto(x, y)

    # Move the first segment to where the head is
    if len(segments) > 0:
        segments[0].goto(head.xcor(), head.ycor())

    # Check for collision with the body
    for segment in segments[1:]:
        if segment.distance(head) < 10:
            game_over = True
            break

# Function to change the direction of the snake
def go_up():
    global direction
    if direction != "down":
        direction = "up"

def go_down():
    global direction
    if direction != "up":
        direction = "down"

def go_left():
    global direction
    if direction != "right":
        direction = "left"

def go_right():
    global direction
    if direction != "left":
        direction = "right"

# Set up keyboard bindings
listen()
onkeypress(go_up, "Up")
onkeypress(go_down, "Down")
onkeypress(go_left, "Left")
onkeypress(go_right, "Right")
onkeypress(lambda: None, "space")  # Ignore space key to prevent immediate game over

# Start the game
move()

# Set up score display
score_display = Turtle()
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 190)
score_display.write("Score: 0", align="center", font=("Arial", 16, "bold"))

# Main game loop
while not game_over:
    update()

    # Check for collision with the border
    if (head.xcor() > 200 or head.xcor() < -200 or
        head.ycor() > 200 or head.ycor() < -200):
        game_over = True

# Game over message
game_over_text = Turtle()
game_over_text.color("white")
game_over_text.penup()
game_over_text.hideturtle()
game_over_text.write("Game Over", align="center", font=("Arial", 24, "italic"))

# Keep the turtle window open
mainloop()
