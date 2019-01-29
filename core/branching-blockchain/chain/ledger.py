'''
# LEDGER 
# ledger related classes and functions
# 
'''

class FileObject:
    '''
    This class only creates a file object for refrencing by other 
    classes and functions. Do not use this function for anything else
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


# MAIN-LEDGER (genesis chain ledger)
class PublicLedger:
    '''
    Genesis chain are created by initiating a PublicLedger.
    This class adopts the FileObject class 
    ''' 
    def __init__(self):
        self.ledgerfileobject = FileObject('genesis', 'csv')
    
    # creates a ledger file
    def __write_file(self):
        self.ledgerfile = self.ledgerfileobject.file

    # writes initial data to file
    def main_ledger_construct(self):
        pass

    # read data from the ledger
    def main_ledger_parse(self):
        pass

    def main_ledger_update(self):
        pass

# SUB-LEDGER (branched chain ledger)
class PrivateLedger:
    '''
    Branched chains are created by initiating a PrivateLedger
    '''
    def __init__(self):
        pass

    def sub_ledger_construct(self):
        pass

    def sub_ledger_parse(self):
        pass

    def sub_ledger_update(self):
        pass