# NODE $ERVER$Y$TEM ## CLASSES #
'''
Classes are used to create consistent data structures and namespaces 
within other modules in the repository. 
'''

# -- Imports -- # 
import datetime
from requests import get


class User:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.reputation = 0.0
        self.fullname = self.fullname_construction()

    def fullname_construction(self):
        return '{}{}'.format(self.first, self.last)
        
    # method for storing user reputation status
    def reputation_calc(self):
        category_rep = self.reputation

class Idea:
    def __init__(self, title, category, value, creator):
        self.title = title
        self.category = category
        self.value = value
        self.creator = creator  

class Admin:
    # TODO: make the admin class an inherited class under the user
    def __init__(self, username, password):
        self.username = username
        self.password = password
        
class DateTime():
    def dt(self):
        return datetime.datetime.now()

class Command:
    def __init__(self, cmd, func):
        self._command = cmd
        self._function = func
    
class ipAddress:
    def __init__(self, octet1, octet2, octet3, octet4):
        self.octet1 = octet1
        self.octet2 = octet2
        self.octet3 = octet3
        self.octet4 = octet4
        self.ip = self.__ip_str()
    
    def __ip_str(self):
        #self.__ip_string = str(self.octet1) + "." + str(self.octet2) + "." + str(self.octet3) + "." + str(self.octet4)
        self.__ip_string = str("{}.{}.{}.{}").format(self.octet1, self.octet2, self.octet3, self.octet4)
        return self.__ip_string 

class Location:
    """
    virtual and physical location class
    """
    def __init__(self):
        self.location = self.__location()
        self.ip = self.__get_ip()


    def __location(self):
        self._location = []
        return self._location

    def __get_ip(self):
        try:
            self._0_node_ip = get('http://ip.42.pl/raw').text
        except:
            self._0_node_ip = 'No network connection'
        return self._0_node_ip  
