# NODE $ERVER$Y$TEM ## CLIENT #
'''
Node-Server top level client interface: Back-end CLI

Interacting with the client is easy once you learn how to use it. start by typing help then
hitting enter. this will launch the help menu. from here its pretty self explanitory. 
read the source code for more in depth instructs and to figure out the other commands and
functions. this is the higest level client interface meaning that there may be more features 
buried deeper in the repository. each lower level may have a pipe to the top level client
module. this is not always the case. 

good luck
~jpd
'''
# ------ IMPORTS ------ #
# Local imports
from library import menu 
from library import ipfs
from library import tpls_server

from library.ntwrk import pyscanner3 as ps3
from library.network import NetworkClient
from library.classes import Admin, DateTime
from node import *
from setup import UserBuild

# python builtin imports
import datetime
import platform
from time import sleep
import os
import shutil
# ---------------------- #

# CLIENT VARIABLES 
__login = True
__run = True
__title_stat = [0]
__mm = 0
__mm_nm = 0
__help =  """
        (command): (description) 
        0: logout
        1: main menu
        2: networking menu 
        3: python shell
        tpls: transport level security server
        ipfs: ipfs menu
        help: help menu (you are here)

        have you even read the source code? 
        did you actually read it though?
        seriously though read the source for documentation.
        the best help is the help you give yourself.
        when all else fails,
        google it.

        """

# Horizontal Title Bar
def title_bar():
    print("=" * shutil.get_terminal_size().columns)

# Title Bar Information
def title():
    title_bar()
    print('__ORION_NET_____\t\t____', dt1.dt())
    if __title_stat[0] == 0:
        print('\t\t|__LOGIN')
        title_bar()
    
    elif __title_stat[0] == 1:
        print('\t\t|__LOGIN_FAILED__')
        title_bar()
    
    elif __title_stat[0] == 2:
        print('\t\t|__NODE_ADMIN___|')
        print("\t\t\t\t|__", platform.platform())
        print("\t\t\t\t|__", "Python Version:",platform.python_version())
        print("\t\t\t\t|__", platform.machine())
        title_bar()

# Determine the system and clear the terminal screen
def clear():
    ops = platform.system()
    if ops == 'Darwin':
        os.system('clear')
    else:
        os.system('cls')

# Clears the screen then displays the title bar
def refresh_screen():
    clear()
    title()

# Clear and Append the __title_stat variable
def ts_c_a(ts_id):
    __title_stat.clear()
    __title_stat.append(ts_id)

# Displays directory information
# TODO: clean up naming and function 
def rfsm():
    path = input('path>')
    p = rfs(path)
    print(p)

# Dispays directory information 
# TODO: clean up naming and function 
def rfs(pathname):
    index = 0
    tsizevar = 0
    print('\n\nINDEX\t\tSIZE\t\tDIRECTORY')
    title_bar()
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
                    print('Permission Error')
            except (FileNotFoundError, OSError):
                print('file not found error')

    returndata = {'indexed files': index,'totalsize': tsizevar}
    print(returndata)
    input('enter>')
    return returndata
 

# Execute user build sequence
def __user_build():
    ub = UserBuild()
    input('enter>')

# Display help information
def __help_menu():
    print(__help)
    nodehelp()
    input('enter>')

# Display TPLS types; user choice; launch tpls type
def __tpls_server():
    try:
        print('[0] single instance of tpls')
        print('[1] infinite loop of tpls')
        print('[2] oop instance of tpls')
        _id = int(input("tpls type = "))
        NodeServer()._tpls_server(_id)
    except ValueError:
        print("bruh thats not an option")
        input('enter>')


# node launch 
def node_launch():
    __node = NodeServer()

# user input wrapper function to read and write files to ipfs manually
def __ipfs_io():
    choice = str(input('[r/w] read or write> ').lower())
    if choice == "r":
        filehash = input("filehash> ")
        __ipfs_read(filehash)
    elif choice == "w":
        infile = input("filename> ")
        __ipfs_write(infile)
    else:
        pass

# IPFS Reader function 
def __ipfs_read(filehash):
    # ipfsnode.reader(filehash)
    pass

#IPFS Writer function
def __ipfs_write(io_file):
    # ipfsnode.writer(io_file)
    pass

# Launch vim window with user inputted file name
# TODO: directory selection tool/menu
def __vim_file_input():
    vimfile = str(input("file name> "))
    __vim(vimfile)

# Launch Vim windows of the client and node top level modules
def _vim_top_level():
    __vim("client.py")
    __vim("node.py")

# Launch Vim window with given file object
def __vim(file_obj):
    launch_cmd = str("start vim ") + str(file_obj)
    os.system(launch_cmd)

# Launch Interactive Python Shell
def __start_file_io():
    io_file = str(input("file> "))
    __start(io_file)

# function wrapper to start interactive python shell with given python filename
# TODO: Add multiplatform support
def __start(io_f):
    start_cmd = str("start py -i ") + str(io_f)
    os.system(start_cmd)

# Local Network Scan 192.168.1.x:xxxxx
def __pyscanner3():
    return ps3.main()

# MAIN MENU FUNCTIONS # 
# Display Setup Main Menu
def __setup_menu():
    menu.initialize_menu(setup_md, "SETUP MAIN MENU")

# Networking Main Menu
def __ntwrk_menu():
    refresh_screen()
    menu.initialize_menu(networking_menu_dict, "NETWORKING MAIN MENU")


# instantiaite the NetworkClient class
nc = NetworkClient()

# Main Menu Dictionary
mm = {
    'Directory Info': rfsm,
    'Setup Menu': __setup_menu,
    'Networking Menu': __ntwrk_menu,
    'Vim-Top-Level': _vim_top_level}

# Networking Menu Dictionary
networking_menu_dict = {
    'TPLS_$ERVER': __tpls_server,
    '$C4N L4N': __pyscanner3,
    "$C4N L4N (NC)": nc._network_scan,
    "Py$canner": nc._pyscanner,
    "Py$canner2": nc._pyscanner2,
    "Rever$e_$he11": nc._reverse_shell,
    'node launch': node_launch}

# IPFS Menu Dictionary
ipfs_md = {
    'IPFS: Reader': __ipfs_read,
    'IPFS: Writer': __ipfs_write}

# Setup Menu Dictionary
setup_md = {
    'User Build': __user_build,
    'Help': __help_menu}



# ================ LOGIN SEQUENCE ================ #
def login():
    if __login == False:
        ts_c_a(2)

    while __login:
        title()
        usn = input('username: ')
        if usn != admin1.username:
            ts_c_a(1)
            refresh_screen()
                    
        elif usn == admin1.username:
            ts_c_a(0)
            refresh_screen()
            pasw = input('password: ')

            if pasw == admin1.password:
                ts_c_a(2)
                refresh_screen()
                print('You are logging in as ', usn)
                refresh_screen()

# ==========#################### APP INTERFACE #####################============ #
# TODO: add auto login functionality
# TODO: function class; client code reduction and optimization; 
                while __run:
                    refresh_screen()
                    command = input('>')
                    
                    # Commands

                    # tpls : Launches a tpls server
                    if command == 'tpls':
                        __tpls_server()

                    # ipfs : launch ipfs main menu
                    elif command == "ipfs":
                        menu.initialize_menu(ipfs_md, "IPFS MAIN MENU")

                    # vim : Vim Vindow
                    elif command == "vim":
                        refresh_screen()
                        __vim_file_input()
                    
                    # help : Help Window 
                    elif command == "help":
                        refresh_screen()
                        __help_menu()

                    # 1 : Main Menu
                    elif command == '1':
                        refresh_screen()              
                        menu.initialize_menu(mm, 'PYTHOS MAIN MENU')
                    
                    # 2 : Networking Main Menu 
                    elif command == '2':
                        refresh_screen()
                        __ntwrk_menu()

                    # 3 : Interactive Python Shell
                    elif command == "3":
                        refresh_screen()
                        __start_file_io()
                        
                    # 0 : Quits the program
                    elif command == '0':
                        refresh_screen()
                        print('LOGING OUT OF THE MATRIX')
                        clear()
                        break

        


if __name__ == "__main__":
    # create admin user
    admin1 = Admin('admin', 'password')
    # create datetime object
    dt1 = DateTime()
    # launch the client
    login()
