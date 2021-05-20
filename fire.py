from random import randint
import unicornhathd as unicorn
from time import sleep

width = 16
height = 16
rows = []
row_pointer = 0

colours = []

unicorn.brightness(1)
unicorn.rotation(0)


def init():

    global rows

    # create a buffer of <height> blank rows
    for i in range(height):
        rows.append(get_blank_row())

    # add an initial source row
    rows.append(get_source_row())

    # generate an array of colours
    for i in range(64):
        r = i * 4
        g = 0 
        b = 0
        if i > 24:
            g = (i - 24) * 6
        if i > 48:
            g = (i - 48) * 8
        if i < 16:
            b = 4 - (i / 4)
        colours.append([r, g, b])


def get_blank_row():

    # generate a blank row
    return [0] * (width + 2)


def get_source_row():

    # generate a source row with random white
    new_row = []
    for i in range(width + 2):
        new_row.append(randint(0, 63))
    return new_row


def update_rows():

    # create fire
    for h in range(height):
        for w in range(width):
            rows[h][w + 1] = (rows[h + 1][w] + rows[h + 1][w + 1] + rows[h + 1][w + 2]) / 3.3


def update_display():

    # keep track of the row we are updating
    for h in range(height):
        for w in range(width):
            # val is between 50 and 255
            val = rows[h][w + 1]

            # fetch the colour
            colour = colours[int(round(val))]

            # invert coordinates
            unicorn.set_pixel((width - 1) - w, (height - 1) - h, colour[0], colour[1], colour[2])

    unicorn.show()


def step():
    global row_pointer

    # add new row at current row pointer
    # leave other rows the same, display will start from this one which overwrites the
    # oldest existing row from the last time we updated the display
    update_rows()
    update_display()

    if row_pointer % 2 == 0:
        rows[height] = get_source_row()

    # determine next row pointer, wrapping around if we went past zero
    row_pointer -= 1
    if row_pointer < 0:
        row_pointer = height - 1


init()
try:
    while True:
        step()
        sleep(0.025)

except KeyboardInterrupt:
    unicorn.off()
