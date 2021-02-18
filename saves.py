#!/usr/bin/env python3
import os  
import sys

TARGET = '/home/dmitry/projects/games-saves'


# блок проверок
if not os.path.exists(TARGET):
    print('This directory does not exists')
    sys.exit()
 
print(TARGET)
