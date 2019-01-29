'''
## a_w.orld
'''

sphere_matrix = [ [], [], [], [], [], [], [], [] ]

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
        from requests import get
        try:
            self._0_node_ip = get('http://ip.42.pl/raw').text
        except:
            self._0_node_ip = 'No network connection'
        return self._0_node_ip