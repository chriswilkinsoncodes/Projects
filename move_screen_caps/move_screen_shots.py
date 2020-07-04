#!/usr/bin/env python3

import os
import pathlib
import shutil

dirs = set()
basepath = '/Users/username/Desktop/'
destpath = '/Users/username/Documents/ScrShots_Desktop/'

# get file list and extract dates to check for directories
for entry in os.listdir(basepath):
    if entry.startswith('Screen Shot'):
        dirs.add(entry[12:22].replace('-', ''))
        print(entry)

# check if directories exist and mkdir if not
for dir in dirs:
    dir = destpath + dir
    file = pathlib.Path(dir)
    if file.exists():
        print(dir, 'exists.')
    else:
        os.mkdir(dir)
        print(dir, 'created.')

# move files to directories
for entry in os.listdir(basepath):
    movedate = entry[12:22].replace('-', '')
    if entry.startswith('Screen Shot'):
    # if entry.startswith('Screen Shot') and movedate != basepath[-9:-1]:
        try:
            source = basepath + entry
            destination = destpath + movedate + '/'
            shutil.move(source, destination)
        except:
            print('File not moved: ' + entry)
        else:
            print(entry, 'moved.')