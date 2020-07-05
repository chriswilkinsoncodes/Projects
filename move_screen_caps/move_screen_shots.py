#!/usr/bin/env python3

import os
import pathlib
import shutil
import time

dirs = set()
basepath = '/Users/username/Desktop/'
destpath = '/Users/username/Documents/ScrShots_Desktop/'

def folder_date(basepath, entry):
    created = os.stat(basepath + entry).st_mtime
    return time.strftime('%Y%m%d', time.localtime(created))

# get file list and extract dates to check for directories
for entry in os.listdir(basepath):
    if entry.startswith('Screen Shot'):
        folder = folder_date(basepath, entry)
        dirs.add(folder)
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
    if entry.startswith('Screen Shot'):
        folder = folder_date(basepath, entry)
        try:
            source = basepath + entry
            destination = destpath + folder + '/'
            shutil.move(source, destination)
        except:
            print('File not moved: ' + entry)
        else:
            print(entry, 'moved.')