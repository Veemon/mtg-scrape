#!/usr/bin/env python3

from __future__ import division
from multiprocessing import Pool, freeze_support
import urllib.request as dl
import sys
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

def dl_image(u_ID):
    url = 'http://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=' + u_ID + '&type=card'
    dl.urlretrieve(url, 'images/'+u_ID+'.jpg')

def main(page_amount):

    # http://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=<>&type=card\
    COLORS = ['R', 'G', 'B', 'W', 'U']
    ALL_ID = []
    for col in COLORS:
        for i in range(page_amount):
            filename = conv(col) + '/' + col + str(i) + '.csv'

            string = open(filename, 'r').read()
            for ID in string.split(','):
                if len(ID) != 0:
                    ALL_ID.append(ID)

    u_IDs = set(ALL_ID)
    pool = Pool(20)

    num_tasks = len(u_IDs)
    for i, _ in enumerate(pool.imap_unordered(dl_image, u_IDs), 1):
        sys.stderr.write('\rdownloading images... {0:%}'.format(i/num_tasks))

if __name__ == '__main__':
    freeze_support()
    main(34) # Currently 34 Pages of Cards
