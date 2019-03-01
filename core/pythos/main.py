# -*- coding: utf-8 -*-
__package__ = 'cloud-chain.core.pythos.main'
__version__ = "0.1.3"

# DEBUG OPTION
_debug = True

# IMPORTS #
# python library imports 
import os

class CORE_PYTHOS:
    def __init__(self):
        self.DirectoryObjectsList = self.returnDirList
    
    def returnDirList(self):
        self.listofdirobjs = rfs('.')
        return self.listofdirobjs

class dir_obj:
    def __init__(self, index, size, pathname):
        self._index = index
        self._size = size
        self._pathname = pathname

def rfsm():
    path = input('path>')
    p = rfs(path)
    print(p)

def rfs(pathname):
    index = 0
    tsizevar = 0
    returndata = []
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
                    _dir_obj = dir_obj(index, size, pathname)
                    returndata.append(_dir_obj)
                    index += 1
                except PermissionError:
                    print('perm error')
            except (FileNotFoundError, OSError):
                print('file not found error')
    return returndata

def rootfile_list_2():
    spath = '/'
    rootfilelist = os.listdir(spath)
    root_dict = rootfilelist
    
    for i in range(0, len(rootfilelist)):
        print(i, spath + rootfilelist[i])

    input('rootfile_list>\t')
    return rootfilelist
  