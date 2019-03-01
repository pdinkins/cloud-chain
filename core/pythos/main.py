# -*- coding: utf-8 -*-
__package__ = 'cloud-chain.core.pythos.main'
__version__ = "0.1.3"

# DEBUG OPTION
_debug = True

# IMPORTS #
# python library imports 
import os



def rfsm():
    path = input('path>')
    p = rfs(path)
    print(p)

def rfs(pathname):
    index = 0
    tsizevar = 0
    print('\n\nINDEX\t\tSIZE\t\tDIRECTORY')
    print('=' * 80)
    for root, dirs, files in os.walk(pathname):
        for file in files:
            try:
                try:
                    pathname = os.path.join(root, file)
                    size = os.path.getsize(pathname)
                    tsizevar += size
                    print(index, '\t\t', size, '\t\t', pathname)
                    index += 1
                except PermissionError:
                    print('perm error')

            except (FileNotFoundError, OSError):
                print('file not found error')

    returndata = {'indexed files': index,'totalsize': tsizevar}
    print(returndata)
    input('>')
    return returndata

def rootfile_list_2():
    spath = '/'
    rootfilelist = os.listdir(spath)
    root_dict = rootfilelist
    
    for i in range(0, len(rootfilelist)):
        print(i, spath + rootfilelist[i])

    input('rootfile_list>\t')
    return rootfilelist
  