#   a123_apple_1.py
import turtle as trtl
import random as rand

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape
pear_image = "pear.gif"

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file
wn.addshape(pear_image)
wn.bgpic("background.gif")

apple = trtl.Turtle()
pear = trtl.Turtle()

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  wn.update()

def draw_pear(active_pear):
  active_pear.shape(pear_image)
  wn.update()

def drop_apple():
  apple.penup()
  apple.goto(0,-200)
  apple.pendown()
  apple.clear()
  apple.hideturtle()

def drop_pear(active_pear):
  pear.penup()
  pear.goto(0,-200)
  pear.pendown()

# This function takes care of font and color.
def draw_an_A():
  apple.color("White")
  apple.write('A', font=("Arial", 65, "bold")) 

def reset():
  apple.clear()
  apple.hideturtle()

#-----function calls-----
draw_an_A()

draw_apple(apple)

wn.onkeypress(drop_apple, "a")


"""draw_pear(pear)

drop_pear(pear)"""

wn.listen()

wn.mainloop()
