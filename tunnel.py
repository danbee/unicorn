# Original Lua/TIC-80 source was live-coded in
# 25 minutes by exoticorn during a 256-byte battle
# at outlinedemoparty.nl 2021-05-15
# 
# function TIC()t=time()/1e3
# for i=0,32639 do
# x=i%240-120
# y=i//240-68
# z=20/(x*x+y*y)^.5+t
# q=z%9<6 and z-z%9+6 or z
# w=9/y+t
# c=y>0 and w<q and
# (((x*(w-t))^2<99 and 14 or 6)+w%2)or
# (-y*(q-t)<99/((x*(q-t)/50)^2+1)and(q==z and z%2 or 3)or 12-y/20)
# poke4(i,c)
# end
# end

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
                    c = (14 if pow(x*(w - t), 2) < 39 else 6) + w%2
                else:
                    if -y*(q - t) < 99/(pow(x*(q - t)/50, 2) + 1):
                        c = z%2 if q == z else 3
                    else:
                        c = 9 - y/3 - ((0x2 >> (-y%3)) & 1)


                unicorn.set_pixel(8 + x, 15 - (y + 9), *palette[int(c)])
                unicorn.set_pixel(15 - (8 + x), 15 - (y + 9), *palette[int(c)])

        unicorn.show()
        sleep(0.025)


except KeyboardInterrupt:
    unicorn.off()
