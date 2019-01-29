'''
# WALLET 

'''

class NewWallet:
    def __init__(self):
        self.timestamp = self.time_stamp()
        self.usr_nym = self.user_nym()
        self.node_build = self.user_build()
        self.id = self.generate_user_id()

    def time_stamp(self):
        import datetime 
        return datetime.datetime.now()

    def user_nym(self):
        usernym = input('This info will be used to name the local wallet file.\nuser_nym> ')
        return usernym
    
    def user_build(self):
        # for testing the current local build
        # initial import
        try:
            import os, sys
            import platform
            import datetime
            import subprocess
            import requests
            import time

        except:
            print('FATAL__BUILD__ERROR')
            error = sys.exc_info()
            print(error)
            print(sys.exc_info()[0])
            raise
    
        try:
            # current cpu system configuration 
            log('0_SYSTEM_CONFIG')
            
            self._0_node_ip = requests.get('http://ip.42.pl/raw').text
            log(self._0_node_ip) 
            
            DEBUG_headers = False
            if DEBUG_headers == True:
                self._0_node_config = requests.get('http://ip.42.pl/headers').text
                log(self._0_node_config)
            else:
                log('DEBUG_headers = ' + DEBUG_headers)

            self._system_architecture = platform.uname()
            log(self._system_architecture)
            
            self.node = platform.platform()
            log(self.node)
            
            self._python_build = platform.python_build()
            log(self._python_build)
            
            self._system = platform.system()
            log(self._system)
            
            self._python_compiler = platform.python_compiler()
            log(self._python_compiler)

            log('0_SYSTEM_CONFIGFILE')

        except:
            print(datetime.datetime.now(), 'SYSTEM LOG')
            error = sys.exc_info()
            print(error)
            print(sys.exc_info()[0])
            raise


    def generate_user_id(self):
        import hashlib
        wid = hashlib.sha256()
        wid.update(str(self.timestamp).encode('utf=8') +
                    str(self.usr_nym).encode('utf-8') + 
                    str(self.node_build).encode('utf-8'))
        return wid.hexdigest()

def generate_new_wallet():
    wallet = NewWallet()
    sys_arc = wallet.user_build()
    builder(wallet.id, wallet.usr_nym, sys_arc)
    wd = [wallet.id, wallet.usr_nym, sys_arc]
    for i in range(0, len(wd)):
        log(wd[i])
    set_current_wallet(wd)


def builder(id, nym, arc):
    try:
        import pynetwork.ipfs as ipfs
        ipfs.initialize_ipfsapi()

        
        config_file = open('config_0_node.txt', 'w')
        for i in range(0, len(arc)):
            config_file.writelines(arc[i]) 
        config_file.close()
        ipfs.add_file('config_0_node.txt')
    
    except:
        print('__BUILD__FILE__IPFS__ERROR')
        import sys
        error = sys.exc_info()
        print(error)
        print(sys.exc_info()[0])
        raise



def set_current_wallet(rgw):
    try:
        d = str(input('Use recently generated wallet as current usable hash wallet [y/n]? >')).lower()
        
        #fill dynamic storage list
        if d == 'y':
            for i in range(0, len(rgw)):
                current_wallet.append(rgw[i])
            log('Succesfully set the current usable wallet')
            # pipe back to client interface
        elif d == 'n':
            aus = str(input('are you sure [y/n]? > ')).lower()
            if aus == 'y':
                # pipe to client interface 
                print('Did not set current usable wallet')
            elif aus == 'n':
                for i in range(0, len(rgw)):
                    current_wallet.append(rgw[i])
            else: 
                raise TypeError
        else:
            raise TypeError

    except TypeError:
        print("ERROR: Not a valid input")
        return


def print_cw():
    for i in range(0, len(current_wallet)):
        print(current_wallet[i])

class WalletFile:
    def __init__(self):
        self.wfn = self.gwfn()
        self.walletfile = self.generate_nwf()

    def gwfn(self):
        # relay function for future security checks on wallet
        file_nym = self.cwe()
        return file_nym

    # checks if current wallet exists and generates if not
    def cwe(self):
        if not current_wallet:
            print('No current usable wallet')
            try:
                gen = str(input('Generate new wallet [y/n]? >')).lower()
                if gen == 'y':
                    generate_new_wallet()
                    print('Test statement for flow..........')
                elif gen == 'n':
                    # pipe to function to set wallet from file
                    pass
                else:
                    raise TypeError
            except TypeError:
                print('ERROR: Invalid input')
        elif current_wallet:
            w_nym = current_wallet[0]
            wfn = w_nym + '.csv'
            return wfn


    def generate_nwf(self):
        import csv
        open(self.wfn, mode='w')


def write_wallet():
    wallet_f = WalletFile()
    name = wallet_f.wfn
    import csv
    with open(name, 'a', newline='') as wallet:
        writer = csv.writer(wallet)
        writer.writerow([current_wallet[0],
                        current_wallet[1],
                        current_wallet[2]])

def write_cwf():
    import csv
    try:
        with open ('main.csv', 'w', newline='') as cwallet:
            writer = csv.writer(cwallet)
            writer.writerow([current_wallet[0],
                            current_wallet[1],
                            current_wallet[2]])
    except FileNotFoundError:
        open('main.csv', 'w')
        return



def parse_wallet():
    try:
        wallet_data.clear()
        import csv
        walletfile = str(input('walletfile> '))
        with open(walletfile) as wallet:
            reader = csv.reader(wallet)
            for row in reader:
                wallet_data.append(row[0])
                wallet_data.append(row[1])
                wallet_data.append(row[2])
    except FileNotFoundError:
        print('ERROR: WALLET__NOT__FOUND')

def log(msg):
    wallet_auto_log(msg)

def wallet_auto_log(message):
    import inspect, logging
    import datetime as dt
    # Get the previous frame in the stack, otherwise it would
    # be this function!!!
    func = inspect.currentframe().f_back.f_code
    # Dump the message + the name of this function to the log.
    logging.debug("{}\t{}\t{}\t{}".format(
        dt.datetime.now(),
        func.co_filename,
        func.co_name,
        message
    ))


debug_menu = False
'''
import app.menu as m

md = {'new wallet': generate_new_wallet,
    'print current wallet info': print_cw,
    'write wallet': write_wallet,
    'quit': m.quit_menu}

while debug_menu:
    m.initialize_menu(md, 'title')
'''