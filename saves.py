#!/usr/bin/env python3
import os  

TARGET = '/home/dmitry/projects/games-saves'


# блок проверок
if not os.path.exists(TARGET):
    os.makedirs(TARGET)
sys.exit()
