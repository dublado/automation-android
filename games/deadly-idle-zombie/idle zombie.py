#!/usr/bin/env python3

from ppadb.client import Client
from PIL import Image
import numpy
import time

adb = Client(host='127.0.0.1', port=5037)
devices = adb.devices()

if len(devices) == 0:
    print('no device attached')
    quit()

device = devices[0]

while True:
    #image = device.screencap()

    # with open('screen.png', 'wb') as f:
    #    f.write(image)

    #start, target1, target2 = transitions
    #gap = target1 - start
    #target = target2 - target1
    #distance = (gap + target / 2) * .98

    #print(f'transition points: {transitions}, distance: {distance}')
    print('clicou')
    # close top
    #device.shell(f'input touchscreen swipe 80 80 80 80')
    # close tap
    #device.shell(f'input touchscreen swipe 551 1657 551 1657')
    # close claim
    #device.shell(f'input touchscreen swipe 988 366 988 366')
    device.shell(f'input touchscreen swipe 988 366 988 366')
    device.shell(f'input touchscreen swipe 988 366 988 366')
    device.shell(f'input touchscreen swipe 988 366 988 366')
    time.sleep(0.2)
    device.shell(f'input touchscreen swipe 600 600 600 600')
    device.shell(f'input touchscreen swipe 600 600 600 600')
    device.shell(f'input touchscreen swipe 600 600 600 600')

    #device.shell(f'input touchscreen swipe 500 500 500 500 {int(distance)}')

    # time.sleep(0.5)
