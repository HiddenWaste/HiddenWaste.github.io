import turtle
import random

#Array for colors
colors = ["red", "green", "blue", "black", "purple"]

#Array for shapes
shapes = ['triangle','square', 'pentagon', 'hexagon', 'spiral']

#initializing the turtle and setting speed
sue = turtle.Turtle()
sue.speed(100)

#Actual Shape Functions
def triangle(d):
  c = random.choice(colors)
  sue.color(c)
  for s in range(3):
    sue.forward(d)
    sue.right(120)

def square(d):
  c = random.choice(colors)
  sue.color(c)
  for s in range(4):
    sue.forward(d)
    sue.right(90)

def pentagon(d):
  c = random.choice(colors)
  sue.color(c)
  for s in range(5):
    sue.forward(d)
    sue.right(72)
  
def hexagon(d):
  c = random.choice(colors)
  sue.color(c)
  for s in range(6):
    sue.forward(d)
    sue.right(60)

def spiral(d):
  i = 0
  c = random.choice(colors)
  sue.color(c)
  for s in range(d):
    sue.forward(d + i)
    sue.right(90)
    i = i + 5
    
#Start of loop to actually make shapes
for s in range(200):
  #function for random size of each shape made for easy substition
  f = (random.randint(10,100))

  #Going to a random spot
  sue.penup()
  sue.goto(random.randint(-300,300), random.randint(-300,300))
  sue.pendown()

  #Drawing the shape
  if (random.choice(shapes)) == 'triangle':
    triangle(f)
  elif (random.choice(shapes)) == 'square':
    square(f)
  elif (random.choice(shapes)) == 'pentagon':
    pentagon(f)
  elif (random.choice(shapes)) == 'hexagon':
    hexagon(f)
  elif (random.choice(shapes)) == 'spiral':
    spiral(random.randint(1,30))


print('Finished!')
