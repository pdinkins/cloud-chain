# -*- coding: utf-8 -*-
__package__ = "cloud-chain.core.network.main"
__version__ = "0.1.3"

class CORE_NETWORK:
    def __init__(self):
        self.network = self.__returnnetwork

    def __returnnetwork(self):
        self.__network = "CORE_NETWORK.network"
        return self.__network