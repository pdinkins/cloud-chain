# NODE $ERVER$Y$TEM ## MENU # 
'''
# Menu Module:
# displays a menu, user choice, choice function execution.


USE:
    1. import menu
    2. define menu choice functions
    3. define menu dictionary
        {'menu choice label': corresponding function}
    4. menu.initialize_menu(**menu_dictionary, **menutitle)
'''

fsocietylogo = '''
        d88888b .d8888.  .d88b.   .o88b. d888888b d88888b d888888b db    db
        88'     88'  YP .8P  Y8. d8P  Y8   `88'   88         88    `8b  d8'
        88ooo   `8bo.   88    88 8P         88    88ooooo    88     `8bd8'
        88        `Y8b. 88    88 8b         88    88         88       88
        88      db   8D `8b  d8' Y8b  d8   .88.   88.        88       88
        YP      `8888Y'  `Y88P'   `Y88P' Y888888P Y88888P    YP       YP
        '''

class newMenu:
    def __init__(self, menu_dict, menu_title):
        self.dictionary = menu_dict
        self.title = menu_title
        self.__init_menu(self.dictionary, self.title)
    
    def __init_menu(self, _menu_dict, _menu_title):
        self.__menu_list = list(_menu_dict.keys())
        print(fsocietylogo)
        for i in range(len(self.__menu_list)):
            print(int(i +1), "-", self.__menu_list[i])


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
        


def quit_menu():
    quit()

def os_walk():
    pass
    

def dir_iter(module_list):
    for i in range(0, len(module_list)):
        print(dir(module_list[i]))


class _Menu:
    def __init__(self, title, choice_matrix):
        self.title = title
        self.choice_matrix = choice_matrix
