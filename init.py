#!/usr/bin/env python3

import os

dirs = ['black', 'blue', 'white', 'red', 'green', 'images']
for directory in dirs:
    if not os.path.exists(directory):
        os.makedirs(directory)
