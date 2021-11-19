#   a123_apple_1.py
import turtle as trtl
import random as rand

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file
wn.bgpic("background.gif")

drawer = trtl.Turtle()
apple = trtl.Turtle()
apple_2 = trtl.Turtle()
apple_3 = trtl.Turtle()
apple_4 = trtl.Turtle()
apple_5 = trtl.Turtle()

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file

letters = ['a,s,d,f,g']

random_letter = rand.choice(letters)

def draw_an_A():
  drawer.penup()
  drawer.goto(-129, -45)
  drawer.pendown()
  drawer.color("White")
  drawer.write((random_letter), font=("Arial", 50, "bold")) 

def draw_apple(active_apple):
  active_apple.penup()
  active_apple.goto(0,0)
  active_apple.pendown()
  active_apple.shape(apple_image)
  wn.update()

def draw_apple2(active_apple_2):
  active_apple_2.penup()
  active_apple_2.goto(-60,-0)
  active_apple_2.pendown()
  active_apple_2.shape(apple_image)
  wn.update()
  
def draw_apple3(active_apple_3):
  active_apple_3.penup()
  active_apple_3.goto(-110,-0)
  active_apple_3.pendown()
  active_apple_3.shape(apple_image)
  wn.update()

def draw_apple4(active_apple_4):
  active_apple_4.penup()
  active_apple_4.goto(60,0)
  active_apple_4.pendown()
  active_apple_4.shape(apple_image)
  wn.update()

def draw_apple5(active_apple_5):
  active_apple_5.penup()
  active_apple_5.goto(110,-0)
  active_apple_5.pendown()
  active_apple_5.shape(apple_image)
  wn.update()

def drop_apple():
  apple.penup()
  apple.goto(0,-150)
  apple.pendown()
  apple.clear()
  apple.hideturtle()
  draw_an_A()

def drop_apple_2():
  apple_2.penup()
  apple_2.goto(-60,-150)
  apple_2.pendown()
  apple_2.clear()
  apple_2.hideturtle()
  draw_an_A()

def drop_apple_3():
  apple_3.penup()
  apple_3.goto(-110,-150)
  apple_3.pendown()
  apple_3.clear()
  apple_3.hideturtle()
  draw_an_A()

def drop_apple_4():
  apple_4.penup()
  apple_4.goto(60,-150)
  apple_4.pendown()
  apple_4.clear()
  apple_4.hideturtle()
  draw_an_A()

def drop_apple_5():
  apple_5.penup()
  apple_5.goto(110,-150)
  apple_5.pendown()
  apple_5.clear()
  apple_5.hideturtle()
  draw_an_A()

# This function takes care of font and color.

#-----function calls-----
draw_apple(apple)
draw_apple2(apple_2)
draw_apple3(apple_3)
draw_apple4(apple_4)
draw_apple5(apple_5)

draw_an_A()
wn.onkeypress(drop_apple, "d")
wn.onkeypress(drop_apple_2, "s")
wn.onkeypress(drop_apple_3, "a")
wn.onkeypress(drop_apple_4, "f")
wn.onkeypress(drop_apple_5, "g")

wn.listen()

wn.mainloop()
