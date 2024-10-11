import serial
import time
import pyglet

window = pyglet.window.Window(800, 800, "Nova Rover")

#---------------------------------------------------------------------------------#

OFFSET = 100

# The four wheels of the rover
wheel = pyglet.graphics.Batch()
wheel_img = pyglet.image.load("wheel.png") # 170 x 360
w, h = 170, 360
wheel_BL = pyglet.sprite.Sprite(img=wheel_img, x = 200 + ((w*0.3)/2) + OFFSET, y = 200 - ((h*0.3)/2), batch=wheel)
wheel_BR = pyglet.sprite.Sprite(img=wheel_img, x = 500 + ((w*0.3)/2) + OFFSET, y = 200 - ((h*0.3)/2), batch=wheel)
wheel_TL = pyglet.sprite.Sprite(img=wheel_img, x = 200 + ((w*0.3)/2) + OFFSET, y = 600 - ((h*0.3)/2), batch=wheel)
wheel_TR = pyglet.sprite.Sprite(img=wheel_img, x = 500 + ((w*0.3)/2) + OFFSET, y = 600 - ((h*0.3)/2), batch=wheel)
wheel_BL.scale = 0.3
wheel_BR.scale = 0.3
wheel_TL.scale = 0.3
wheel_TR.scale = 0.3

# The squares of the keys (wasd)
BLACK = (0, 0, 0)
WHITE= (255, 255, 255)
keys = pyglet.graphics.Batch()
square_width = 50
squareW = pyglet.shapes.Rectangle(x=97, y=97, width=60, height=60, color=BLACK, batch=keys)
squareW.anchor_position = square_width/2, square_width/2
squareA = pyglet.shapes.Rectangle(x=35, y=35, width=60, height=60, color=BLACK, batch=keys)
squareA.anchor_position = square_width/2, square_width/2
squareS = pyglet.shapes.Rectangle(x=97, y=35, width=60, height=60, color=BLACK, batch=keys)
squareS.anchor_position = square_width/2, square_width/2
squareD = pyglet.shapes.Rectangle(x=159, y=35, width=60, height=60, color=BLACK, batch=keys)
squareD.anchor_position = square_width/2, square_width/2

# Chassis
GREY = (82, 82, 82)
chassis = pyglet.graphics.Batch()
verc = pyglet.shapes.Rectangle(x=400 + OFFSET, y=400, width=200, height=400, color=GREY, batch=chassis)
verc.anchor_position = 200/2, 400/2
horz = pyglet.shapes.Rectangle(x=400 + OFFSET, y=400, width=300, height=250, color=GREY, batch=chassis)
horz.anchor_position =300/2, 250/2

# Labels for the keys (wasd)
CYAN = (40, 168, 168)
letterW = pyglet.text.Label("W", x=102, y=102, anchor_x="center", anchor_y="center", color=CYAN, batch=keys)
letterA = pyglet.text.Label("A", x=40, y=40, anchor_x="center", anchor_y="center", color=CYAN, batch=keys)
letterS = pyglet.text.Label("S", x=102, y=40, anchor_x="center", anchor_y="center", color=CYAN, batch=keys)
letterD = pyglet.text.Label("D", x=164, y=40, anchor_x="center", anchor_y="center", color=CYAN, batch=keys)

# NOVA ROVER title
RED = (255, 0, 0)
title = pyglet.graphics.Batch()
nL = pyglet.text.Label("N", x=70, y=575, anchor_x="center", anchor_y="center", font_name="Copperplate Gothic", font_size=50, bold=True, color=RED, batch=title)
oL = pyglet.text.Label("O", x=70, y=475, anchor_x="center", anchor_y="center", font_name="Copperplate Gothic", font_size=50, bold=True, color=WHITE, batch=title)
vL = pyglet.text.Label("V", x=70, y=375, anchor_x="center", anchor_y="center", font_name="Copperplate Gothic", font_size=50, bold=True, color=WHITE, batch=title)
aL = pyglet.text.Label("A", x=70, y=275, anchor_x="center", anchor_y="center", font_name="Copperplate Gothic", font_size=50, bold=True, color=WHITE, batch=title)

rR1 = pyglet.text.Label("R", x=145, y=675, anchor_x="center", anchor_y="center", font_name="Copperplate Gothic", font_size=50, bold=True, color=WHITE, batch=title)
oR = pyglet.text.Label("O", x=145, y=575, anchor_x="center", anchor_y="center", font_name="Copperplate Gothic", font_size=50, bold=True, color=WHITE, batch=title)
vR = pyglet.text.Label("V", x=145, y=475, anchor_x="center", anchor_y="center", font_name="Copperplate Gothic", font_size=50, bold=True, color=WHITE, batch=title)
eR = pyglet.text.Label("E", x=145, y=375, anchor_x="center", anchor_y="center", font_name="Copperplate Gothic", font_size=50, bold=True, color=WHITE, batch=title)
rR2 = pyglet.text.Label("R", x=145, y=275, anchor_x="center", anchor_y="center", font_name="Copperplate Gothic", font_size=50, bold=True, color=RED, batch=title)

icon = pyglet.image.load("badge.png") # 525 x 475
rover = pyglet.sprite.Sprite(img=icon, x = 70 - ((525*0.4)/2), y = 670 - ((475*0.4)/2), batch=title)
rover.scale = 0.4
#---------------------------------------------------------------------------------#

@window.event
def on_key_press(symbol, modifiers):
    global squareW, squareA, squareS, squareD, BLACK, WHITE
    if symbol == pyglet.window.key.W:
        squareW.color = WHITE
    elif symbol == pyglet.window.key.A:
        squareA.color = WHITE
    elif symbol == pyglet.window.key.S:
        squareS.color = WHITE
    elif symbol == pyglet.window.key.D:
        squareD.color = WHITE

@window.event
def on_key_release(symbol, modifiers):
    global squareW, squareA, squareS, squareD, BLACK, WHITE
    if symbol == pyglet.window.key.W:
        squareW.color = BLACK
    elif symbol == pyglet.window.key.A:
        squareA.color = BLACK
    elif symbol == pyglet.window.key.S:
        squareS.color = BLACK
    elif symbol == pyglet.window.key.D:
        squareD.color = BLACK

#---------------------------------------------------------------------------------#

"""
baud = 9600
arduino = serial.Serial(port="COM4", baudrate=9600, timeout=1)


def write_read(x):
    arduino.write(bytes(x,  'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return  data


while True:
    num = input("Enter a number: ")
    value  = write_read(num)
    print(value)
"""

#---------------------------------------------------------------------------------#

@window.event
def on_draw():
    window.clear()
    wheel.draw()
    keys.draw()
    chassis.draw()
    title.draw()

#---------------------------------------------------------------------------------#

pyglet.app.run()