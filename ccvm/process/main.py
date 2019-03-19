# -*- coding: utf-8 -*-
__package__ = "cloud-chain.ccvm.process.main"
__version__ = "0.1.37"
__debug = True
__test = True

import inspect

class PROCESS:
    def __init__(self):
        if __debug:
            if __test:
                self.__test()

    def __test(self):
        return __test

def OxPX():
    return inspect.currentframe()