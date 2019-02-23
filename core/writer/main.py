# -*- coding: utf-8 -*-

"""core.writer.main module"""

writer_help = '''
This module interacts with files and contians:
    Classes
        FileObject
        Write2file

USE:
    1. from core.writer.main import FileObject, Write2File
    2. file_obj = writer.FileObject('name', 'filetype')
    3. Write2file(file_obj.file, 'data 2 be written to the file')


Three lines of code is all it takes and is all it should take,
to make a file and write something to a it.
'''

class FileObject:
    '''
    file_obj = writer.FileObject('name', 'filetype')

    This class only creates a file object for refrencingby other 
    classes and functions. Do not use this function for anythong else
    '''
    def __init__(self, filename, filetype):
        self.filename = filename
        self.filetype = filetype
        self.file = self.fileconstructor()
        self.filecreator()

    def fileconstructor(self):
        return self.filename + '.' + self.filetype

    def filecreator(self):
        open(self.file, mode='w')


class Write2file:
    """
    Write2file(file_obj.file, 'data 2 be written to the file')
    """
    def __init__(self, filenameobject, data2write):
        with open(filenameobject, 'w') as fille:
            fille.write(data2write)
