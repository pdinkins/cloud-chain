# -*- coding: utf-8 -*-
__package__ = "cloud-chain.ccvm.chain.main"
__version__ = "0.1.3"
__debug = True
__test = True

class CHAIN:
    def __init__(self):
        if __debug:
            if __test:
                self.__test()

    def __test(self):
        return __test