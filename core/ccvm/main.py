# -*- coding: utf-8 -*-
__package__ = "cloud-chain.ccvm.main"
__version__ = "0.1.37"
__debug = True
__test = True


# CALL
from call.main import CALL
from call.main import OxCA

# CHAIN 
from chain.main import CHAIN
from chain.main import OxCN

# CLOUD 
from cloud.main import CLOUD
from cloud.main import OxCO
# CREATE
from create.main import CREATE
from create.main import OxCR

# ERROR
from error.main import ERRROR
from error.main import OxER

# EXECUTE
from execute.main import EXECUTE
from execute.main import OxEX

# FUNCTION
from function.main import FUNCTION
from function.main import OxFX

# PROCESS
from process.main import PROCESS
from process.main import OxPX

# TRANSACTION
from transaction.main import TRANSACTION
from transaction.main import OxTX


class VM:
    def __init__(self):
        self.ca = CALL
        self.__ca = OxCA
        self.cn = CHAIN
        self.__cn = OxCN
        self.co = CLOUD
        self.__co = OxCO
        self.cr = CREATE
        self.__cr = OxCR
        self.er = ERRROR
        self.__er = OxER
        self.ex = EXECUTE
        self.__ex = OxEX
        self.fx = FUNCTION
        self.__fx = OxFX
        self.px = PROCESS
        self.__px = OxPX
        self.tx = TRANSACTION
        self.__tx = OxTX

    def __test(self):
        if __debug:
            if __test:
                return __test



if __name__ == "__main__":
    vm = VM()
    dl = [ca,cn,co,cr,er,ex,fx,px,tx]
    if __debug:
        for i in range(0, len(dl)):
            vm.dl[i]()

