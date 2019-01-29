'''
#==============================================================================================#
# Pyhtos top level client interface:
##  Back-end, CLI interface


This is the higest level client interface meaning that there may be more features 
buried deeper in the repository. Each level may have a client module. This is 
not always the case. good luck ~jpd
#==============================================================================================#
'''

from modules.menu import *
#from modules.ntwrk import *
from time import sleep
import os


login = False
run = True
titlestat = [0]

#==============================================================================================#
#### Classes
class Admin:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class DateTime():
    def dt(self):
        import datetime
        return datetime.datetime.now()

#define the class instances
admin1 = Admin('admin', 'password')
# hint: this line 
dt1 = DateTime()
#==============================================================================================#

def help_menu():
    '''
    TODO: Add more sarcastic comments for laughs.
    '''
    print(
        """
        _______HELP_PAGE_______
        =======================
        
        have you even read the source code? 
        
        did you actually read it though?

        seriously read the source for documentation though
        
        the best help is the help you give yourself.
        

        for root, dirs, files in os.walk(".", topdown=True):
            for file in files:
                print(os.path.join(root, file))

            for name in dirs:
                print(os.path.join(root, name))

        for dir in dirs:
            dirpath = os.path.join(root, dir)
            dirsize = os.path.getsize(dirpath)
            print(index, '\t\t', dirsize, '\t\t', dirpath)
            index += 1
        """
    )
    input('> ')

#==============================================================================================#
def title():
    # running titlebar
    print('=' * 80)
    print('PYTHOS\t\t\t\t\t', dt1.dt())
    #print('=' * 80)
    
    # subtitle
    if titlestat[0] == 0:
        print('\n\t\tLOGIN')
        print('=' * 80)
    
    elif titlestat[0] == 1:
        print('\n\t\tLOGIN FAILED')
        print('=' * 80)
    
    elif titlestat[0] == 2:
        print('\n\t\tNODE_ADMIN')
        print('=' * 80)

def clear():
    import platform
    ops = platform.system()
    if ops == 'Darwin':
        os.system('clear')
    else:
        os.system('cls')

def refresh_screen():
    clear()
    title()
    input('.')


#==============================================================================================#
####### LOGIN SEQUENCE #######

if login == False:
    titlestat.clear()
    titlestat.append(2)

while login:
    #title()
    usn = input('username: ')
    if usn != admin1.username:
        titlestat.clear()
        titlestat.append(1)
        refresh_screen()
                
    elif usn == admin1.username:
        titlestat.clear()
        titlestat.append(0)
        refresh_screen()
        pasw = input('password: ')

        if pasw == admin1.password:
            titlestat.clear()
            titlestat.append(2)
            refresh_screen()
            print('You are logging in as ', usn)
            refresh_screen()
            break

#==============================================================================================#
# MATRIX MENU
#==============================================================================================#
'''
def genmatrix():
    el1 = int(input('el1> '))
    el2 = int(input('el2> '))
    main.matrix(el1, el2)
    input('>')
'''

infinity_menu = {
#    "matrix": genmatrix,
    'HELP MENU': help_menu,
    'Quit': mm.quit_menu,
#    'tpls start handshake': ntwrk.tpls_server.start_handshake
}

def matrixm():
    # Launch the terminal menu interface 
    mm.initialize_menu(infinity_menu, 'BB Main Menu') 
#==============================================================================================#


#==============================================================================================#
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
        
# Main menu dictionary
mam = {
    'root file system list 2': rootfile_list_2,
    'directory info': rfsm,
    'matrix': matrixm
}
#==============================================================================================#
######## APP INTERFACE ########
while run:
    refresh_screen()
    command = input('>')
    if command == '0':
        refresh_screen()
        print('LOGING OUT OF THE MATRIX')
        clear()
        break
    
    elif command == "help":
        refresh_screen()
        help_menu()

    elif command == '1':
        refresh_screen()              
        mm.initialize_menu(mam, 'ROOT FILE SYSTEM MAIN MENU')

    elif command == '2':
        path = input('path >\t')
        rfs(path)
        command = input('>')
    
    elif command == '':
        refresh_screen()
    
    else:
        try:
            print(eval(command))
            input('>')
        except (NameError, SyntaxError):
            print('ERROR')
            input('>')
#==============================================================================================#
