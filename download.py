#!/usr/bin/env python3

import urllib.request as dl
import sys

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

# http://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=<>&type=card\
COLORS = ['R', 'G', 'B', 'W', 'U']
ALL_ID = []
for col in COLORS:
    for i in range(34):
        filename = conv(col) + '/' + col + str(i) + '.csv'

        string = open(filename, 'r').read()
        for ID in string.split(','):
            if len(ID) != 0:
                ALL_ID.append(ID)

for u_ID in set(ALL_ID):
    url = 'http://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=' + u_ID + '&type=card'
    dl.urlretrieve(url, 'images/'+u_ID+'.jpg')
