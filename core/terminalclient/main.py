# terminal-client

import platform
import os
import shutil
import datetime

class Interface:
    """
    Terminal Interface
    """
    def __init__(self, menudict, menutitle, lus=0):
        self.__menudict = menudict
        self.__menutitle = menutitle
        self.__operating_system = platform.system()
        self.__localuserstate = lus
        self.__userstate = self.checkuserstate()
        
    
    # Horizontal Title Bar
    def __title_bar(self):
        print("=" * shutil.get_terminal_size().columns)

    # Title Bar Information
    def __title(self):
        self.__title_bar()
        print('\t\t____________________', datetime.datetime.now())
        print('\t\t|_____ADMIN_____|')
        print("\t\t\t\t|__", platform.platform())
        print("\t\t\t\t|__","Python Version:",platform.python_version())
        self.__title_bar()

    # Determine the system and clear the terminal screen
    def __clear(self):
        if self.__operating_system == 'Darwin':
            os.system('clear')
        elif self.__operating_system == 'Windows':
            os.system('cls')

    def __menu(self):
        initialize_menu(self.__menudict, self.__menutitle)

    def checkuserstate(self):
        if self.__localuserstate == 0:
            return False
        elif self.__localuserstate == 1:
            return True
        else:
            return None

    # Clears the screen then displays the title bar
    def display(self):
        self.__clear()
        self.__title()
        self.__menu()


def initialize_menu(menu_dictionary, menutitle):
    menulist = list(menu_dictionary.keys())
    j = 1
    print('\n' + menutitle, '\n')
    for i in range(0,len(menulist)):
        print(j,'-', menulist[i])
        j += 1 
    choose_from_menu(menulist, menu_dictionary)

def choose_from_menu(menulist, menu_dictionary):
    try:
        try:
            menuchoice = int(input('\nMenu Choice:  '))
        except EOFError:
            return
        menuchoice -= 1
        print()
        menu_dictionary[menulist[menuchoice]]()
    except (IndexError, ValueError):
        print('***invalid choice***')
 

if __name__ == "__main__":
    testdict = {}
    ui = Interface(testdict, "test")
    #ui.display()

