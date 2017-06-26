#!/usr/bin/env python3

import os

def conv(color):
    if color == 'R':
        return 'red'
    if color == 'G':
        return 'green'
    if color == 'B':
        return 'black'
    if color == 'W':
        return 'white'
    if color == 'U':
        return 'blue'

COLORS = ['R', 'G', 'B', 'W', 'U']
for col in COLORS:
    for i in range(34):
        os.rename(col + str(i) + '.csv', conv(col) + '/' + col + str(i) + '.csv')
