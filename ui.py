import serial
import time
import pyglet

window = pyglet.window.Window(800, 800, "Nova Rover")

#---------------------------------------------------------------------------------#

OFFSET = 100

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

BLACK = (0, 0, 0)
WHITE= (255, 255, 255)
keys = pyglet.graphics.Batch()
square_width = 50
squareW = pyglet.shapes.Rectangle(x=97 + OFFSET, y=97, width=60, height=60, color=BLACK, batch=keys)
squareW.anchor_position = square_width/2, square_width/2
squareA = pyglet.shapes.Rectangle(x=35 + OFFSET, y=35, width=60, height=60, color=BLACK, batch=keys)
squareA.anchor_position = square_width/2, square_width/2
squareS = pyglet.shapes.Rectangle(x=97 + OFFSET, y=35, width=60, height=60, color=BLACK, batch=keys)
squareS.anchor_position = square_width/2, square_width/2
squareD = pyglet.shapes.Rectangle(x=159 + OFFSET, y=35, width=60, height=60, color=BLACK, batch=keys)
squareD.anchor_position = square_width/2, square_width/2

CYAN = (40, 168, 168)
letterW = pyglet.text.Label("W", x=102, y=102, anchor_x="center", anchor_y="center", color=CYAN, batch=keys)
letterA = pyglet.text.Label("A", x=40, y=40, anchor_x="center", anchor_y="center", color=CYAN, batch=keys)
letterS = pyglet.text.Label("S", x=102, y=40, anchor_x="center", anchor_y="center", color=CYAN, batch=keys)
letterD = pyglet.text.Label("D", x=164, y=40, anchor_x="center", anchor_y="center", color=CYAN, batch=keys)

GREY = (82, 82, 82)
chassis = pyglet.graphics.Batch()
verc = pyglet.shapes.Rectangle(x=400 + OFFSET, y=400, width=200, height=400, color=GREY, batch=chassis)
verc.anchor_position = 200/2, 400/2
horz = pyglet.shapes.Rectangle(x=400 + OFFSET, y=400, width=300, height=250, color=GREY, batch=chassis)
horz.anchor_position =300/2, 250/2

title = pyglet.graphics.Batch()
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

#---------------------------------------------------------------------------------#

pyglet.app.run()