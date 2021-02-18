#!/usr/bin/env python3
import os.path  

TARGET = '/home/dmitry/projects/games-saves'


# блок проверок
isdir = os.path.isdir(TARGET)  
print(isdir)
