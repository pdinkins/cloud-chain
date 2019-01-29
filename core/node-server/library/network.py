# NODE $ERVER$Y$TEM ## NETWORK #

class NetworkClient:
    '''
    NetworkClient class requires the NodeBuild class containing import config data
    Controls networking module import and namespace elevation
    '''
    def __init__(self, **NodeBuild):
        #self._nodebuild = NodeBuild
        #self.ip = self._nodebuild._ip
        #self.port = self._nodebuild._port
        self._network_scan = self.__network_scan
        self._pyscanner2 = self.__pyscanner2
        self._pyscanner = self.__pyscanner
        self._reverse_shell = self.__reverse_shell
        self._axis_cam = self.__axis_cam

    def __network_scan(self):
        print('__NetworkClient.__network_scan()')
        from library.ntwrk import pyscanner3
        return pyscanner3
    
    def __pyscanner2(self):
        print('__NetworkClient.__pyscanner2()')
        from library.ntwrk import pyscanner2
        return pyscanner2

    def __pyscanner(self):
        print('__NetworkClient.__pyscannern()')
        from library.ntwrk import pyscanner
        return pyscanner
    
    def __reverse_shell(self):
        print('__NetworkClient.__reverse_shell()')
        from library.ntwrk import reverseshell
        return reverseshell
    
    def __axis_cam(self):
        print('__NetworkClient.__axis_cam()')
        from library.ntwrk import axis

class node:
    def __init__(self, ip, peers):
        self.ip = ip
        self.peers = peers
    
    def connect_to_peer(self):
        pass

    def connect(self):
        pass