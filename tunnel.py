from random import randint
import unicornhathd as unicorn
import math
from time import sleep

unicorn.brightness(1)
unicorn.rotation(0)

height = 16
width = 16

half_height = 8 
half_width = 8

palette = [
    (0x1a, 0x1c, 0x2c),
    (0x5d, 0x27, 0x5d),
    (0xb1, 0x3e, 0x53),
    (0xef, 0x7d, 0x57),
    (0xff, 0xcd, 0x75),
    (0xa7, 0xf0, 0x70),
    (0x38, 0xb7, 0x64),
    (0x25, 0x71, 0x79),
    (0x29, 0x36, 0x6f),
    (0x3b, 0x5d, 0xc9),
    (0x41, 0xa6, 0xf6),
    (0x73, 0xef, 0xf7),
    (0xf4, 0xf4, 0xf4),
    (0x94, 0xb0, 0xc2),
    (0x56, 0x6c, 0x86),
    (0x33, 0x3c, 0x57)
];


t = 0

try:
    while True:
        t += 0.25

        for y in range(-half_height - 1, half_height - 1):
            for x in range(-half_width, 0):
                z = 20/math.sqrt(x*x + y*y) + t
                q = z - (z%21) + 15 if (z%21) < 15 else z
                w = 9/y + t if y != 0 else t 

                if y > 0 and w < q:
                    c = (14 if pow(x*(q - t), 2) < 39 else 6) + w%2
                else:
                    if -y*(q - t) < 99/(pow(x*(q - t)/50, 2) + 1):
                        c = z%2 if q == z else 3
                    else:
                        c = 9 - y/3 - ((0x2 >> (-y%3)) & 1)

                unicorn.set_pixel(x, y, *palette[int(c)])

        unicorn.show()
        sleep(0.025)


except KeyboardInterrupt:
    unicorn.off()
