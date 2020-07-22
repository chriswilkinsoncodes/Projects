#!/usr/bin/env python3

import os
import pathlib
import shutil
import time


def get_files_dirs(basepath: str):
    '''
    Get contents of desktop (basepath).
    Return:
        screen_shots: List of Screen Shots to be moved to directories
                      based on capture date.
        dirs: Set of required directories based on screen shot dates.
    '''
    path_contents = os.listdir(basepath)
    desktop_contents = [os.path.join(basepath, file) for file in path_contents]
    screen_shots = [file for file in desktop_contents if os.path.isfile(file)
                    and 'Screen Shot' in file]
    dirs = {folder_date(file) for file in screen_shots}
    return screen_shots, dirs


def folder_date(file: list):
    '''
    Get folder dates based on file created dates.
    Return:
        date in YYYYMMDD format
    '''
    created = os.stat(file).st_mtime
    return time.strftime('%Y%m%d', time.localtime(created))


def make_folders(dirs: set):
    '''
    Check if directories exist and mkdir if not.
    '''
    for dir in dirs:
        dir = destpath + dir
        file = pathlib.Path(dir)
        if file.exists():
            print(dir, 'exists.')
        else:
            os.mkdir(dir)
            print(dir, 'created.')


def move_files(screen_shots: list, destpath: str):
    '''
    Move files to directories based on file created date.
    '''
    for file in screen_shots:
        folder = folder_date(file)
        try:
            destination = destpath + folder + '/'
            shutil.move(file, destination)
        except Exception as e:
            print(f'File not moved: {file}.\n{e}')
        else:
            print(file, 'moved.')


if __name__ == '__main__':
    basepath = '/Users/username/Desktop/'
    destpath = '/Users/username/Documents/ScrShots_Desktop/'
    screen_shots, dirs = get_files_dirs(basepath)
    make_folders(dirs)
    move_files(screen_shots, destpath)
