#!/usr/bin/env python3

import os
import pathlib
import shutil
import time


def get_files(basepath):
    # get file list and extract dates to check for directories
    dirs = set()
    for entry in os.listdir(basepath):
        if entry.startswith('Screen Shot'):
            folder = folder_date(basepath, entry)
            dirs.add(folder)
            print(entry)
    return dirs

def folder_date(basepath, entry):
    created = os.stat(basepath + entry).st_mtime
    return time.strftime('%Y%m%d', time.localtime(created))

def make_folders(dirs):
    # check if directories exist and mkdir if not
    for dir in dirs:
        dir = destpath + dir
        file = pathlib.Path(dir)
        if file.exists():
            print(dir, 'exists.')
        else:
            os.mkdir(dir)
            print(dir, 'created.')

def move_files(basepath, destpath):
    # move files to directories
    for entry in os.listdir(basepath):
        if entry.startswith('Screen Shot'):
            folder = folder_date(basepath, entry)
            try:
                source = basepath + entry
                destination = destpath + folder + '/'
                shutil.move(source, destination)
            except Exception as e:
                print(f'File not moved: {entry}. {e}')
            else:
                print(entry, 'moved.')


if __name__ == '__main__':
    basepath = '/Users/username/Desktop/'
    destpath = '/Users/username/Documents/ScrShots_Desktop/'
    dirs = get_files(basepath)
    make_folders(dirs)
    move_files(basepath, destpath)