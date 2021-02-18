#!/usr/bin/env python3
import os  
import sys

TARGET = '/home/dmitry/projects/games-saves'


# блок проверок
if not os.path.exists(TARGET):
    sys.exit()
