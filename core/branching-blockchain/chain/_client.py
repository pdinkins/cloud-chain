# client.py 
# environment for interacting with the network

import chain.menu
import test


def help_menu():
    '''
    TODO: Internal documentation for interacting with the client interface
    '''
    print('This is the help page\n')
    print('Read the documentation on the github page')
    print('aswell as whats written alongside the source code.')
    print('\nVim is highly recomended to make quick changes to source\naswell as read the documentation.')



# MAIN MENU DICT 
# menu.py for more documentation
main_menu = {
    'HELP MENU': help_menu,
    'Quit': chain.menu.quit_menu
}

def mm():
    # Launch the terminal menu interface 
    chain.menu.initialize_menu(main_menu, 'BB Main Menu') 

