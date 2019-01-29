# NODE # 
# $ERVER$Y$TEM # 

#==============================================================================================#
#==============================================================================================#
#Pythos Database
#events|contacts|
#csv read/write/parse/view/print/
# this is a fragile module thats been scraped together from legacy code 
# it needs to be updated and moved from a functional model to
#==============================================================================================#
#==============================================================================================#

import csv


#==============================================================================================#
## DYNAMIC STORAGE ## 
'''
dynamically stored data
'''
                            ## Contact Storage
names = []
email = []
phone = []
                            ## Event Storage
events = []
dates = []
starttime = []
endtime = []

# clears the lists so they can be re-parsed in the csvread function

def listclear():
    names.clear()
    email.clear()
    phone.clear()

def eventlistclear():
    events.clear()
    dates.clear()
    starttime.clear()
    endtime.clear()

def dyndump():
    listclear()
    eventlistclear()

#==============================================================================================#


#==============================================================================================#
## CVS READ ##
'''
reads data from the csv to the lists above
'''

                            # contacts csv read
def csvread():
    try:
        with open('contacts.csv') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                names.append(row[0])
                email.append(row[1])
                phone.append(row[2])
    except FileNotFoundError:
        print('Could not find contacts file.\nA new was file created.\n')
        open('contacts.csv', 'w')
        csvread()


                            # events csv read 
def eventcsvread():
    try:
        with open('events.csv') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                events.append(row[0])
                dates.append(row[1])
                starttime.append(row[2])
                endtime.append(row[3])

    except FileNotFoundError:
        open('events.csv', 'w')
        eventcsvread()

def main_csv_read():
    csvread()
    eventcsvread()

#==============================================================================================#



#==============================================================================================#
## CSV WRITE ##
'''
# writes a new contact to the csv file
'''

                                # contacts csv writer
def csvwrite():
    with open('contacts.csv', 'a', newline='') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        name = input('name: ')
        email = input('email: ')
        phone = input('phone: ')
        filewriter.writerow([name, email, phone])

                                # eventas csv writer
def eventcsvwrite():
    with open('events.csv', 'a', newline='') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        event_name = input('Event name: ')
        event_date = input('Event date: ')
        start_time = input('Start time: ')
        end_time = input('Endtime: ')
        filewriter.writerow([event_name, event_date, start_time, end_time])


#==============================================================================================#



###### Contacts ########## Events #########
#==============================================================================================#

#==============================================================================================#
## VIEW ##
'''
# allows the user to view a single contact from the csv file
# display the information in a readble fashion
'''
# contacts
def view():
    try:
        if len(names) == 0:
            print('*** The contacts file is empyty ***')
        else:    
            v1 = int(input('\nContact number: '))
            v = v1 - 1
            print('\nName: ', names[v])
            print('Email: ', email[v])
            print('Phone #: ', phone[v])
    except ValueError:
        print('*** Invalid Integer ***')
    except IndexError:
        print('*** Invalid Contact Number ***')

# events
def eventview():
    v = int(input('\nEvent number: '))
    v -= 1
    print('\nEvent: ', events[v])
    print('Date: ', dates[v])
    print('Time: ', starttime[v], 'till', endtime[v])

#==============================================================================================#
## LIST ##
'''
# Lists all of the names from the contacts file and gives them index values
# those index values are used for the rest of the functions 
'''
# contacts
def llist():
    listclear()
    csvread()
    if len(names) == 0:
        print('*** The contacts file is empty ***')
    else:
        namelen = len(names)
        listnum = 1
        for i in range(0, namelen):
            print(listnum, '. ', names[i])
            listnum += 1

# events
def eventllist():
    namelen = len(events)
    listnum = 1
    for i in range(0, namelen):
        print(listnum, '. ', events[i])
        listnum += 1

#==============================================================================================#
## ADD ##
'''
# adds contact to the file, clears the storage lists and re-parses the csv file
'''

# contacts
def add():
    csvwrite()
    listclear()
    csvread()

# events
def eventadd():
    eventcsvwrite()
    eventlistclear()
    eventcsvread()
    
#==============================================================================================#
## DELETE ##
'''
# deletes a contact be index number defined in the llist function
'''
# contacts
def delete():
    try:
        if len(names) == 0:
            print('*** The contacts file is empty ***')
        else:
            file = open('contacts.csv', 'r')
            lines = file.readlines()
            file.close()
            delnum = int(input('Contact number to delete: '))
            delnum -= 1
            del lines[delnum]
            open('contacts.csv', 'w').writelines(lines)
            listclear()
            csvread()
    except IndexError:
        print('*** Invalid Contact Number ***')
    except ValueError:
        print('*** Invalid Integer ***')

# events
def eventdelete():
    file = open('events.csv', 'r')
    lines = file.readlines()
    file.close()
    delnum = int(input('Events number to delete: '))
    delnum -= 1
    del lines[delnum]
    open('Events.csv', 'w').writelines(lines)
    eventlistclear()
    eventcsvread()

#==============================================================================================#

# database help menu
def command_menu():
    print('COMMAND MENU')
    menuchoices = [
        'list - Display all contacts',
        'view - View a contact',
        'add - Add a contact',
        'del - Delete a contact',
        'exit - Exit program']
    size = len(menuchoices)
    for i in range(0, size):
        print(menuchoices[i])


# dictionary with the available commands
# contacts
command_dict = {
    'list': llist,
    'view': view,
    'add': add,
    'del': delete
    }
# events
events_command_dict = {
    'list': eventllist,
    'view': eventview,
    'add': eventadd,
    'del': eventdelete
    }


#==============================================================================================#



######### MENU ###########
#==============================================================================================#

### menu init ##### 
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


def main_menu():
    initialize_menu(planner_dict, 'Main Menu')

def events_menu():
    initialize_menu(events_command_dict, 'Events Menu')

def contacts_menu():
    initialize_menu(command_dict, "Contacts Menu")


planner_dict = {
    'e': events_menu,
    'c': contacts_menu,
    'quit': quit_menu
}


#==============================================================================================#
#==============================================================================================#

run = True

main_csv_read()

while run:
    print('debug top of while loop')
    main_menu()

#==============================================================================================#
#==============================================================================================#
#==============================================================================================#