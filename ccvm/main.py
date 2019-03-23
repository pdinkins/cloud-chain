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
        self.ca = self._CA_
        self._ca = CALL
        self.__ca = OxCA
        self.cn = self._CN_
        self._cn = CHAIN
        self.__cn = OxCN
        self.co = self._CO_
        self._co = CLOUD
        self.__co = OxCO
        self.cr = self._CR_
        self._cr = CREATE
        self.__cr = OxCR
        self.er = self._ER_
        self._er = ERRROR
        self.__er = OxER
        self.ex = self._EX_
        self._ex = EXECUTE
        self.__ex = OxEX
        self.fx = self._FX_
        self._fx = FUNCTION
        self.__fx = OxFX
        self.px = self._PX_
        self._px = PROCESS
        self.__px = OxPX
        self.tx = self._TX_
        self._tx = TRANSACTION
        self.__tx = OxTXs
    
    def _CA_(self):
        raise NotImplemented

    def _CN_(self):
        raise NotImplemented
    
    def _CO_(self):
        raise NotImplemented
    
    def _CR_(self):
        raise NotImplemented

    def _ER_(self):
        raise NotImplemented

    def _EX_(self):
        raise NotImplemented

    def _FX_(self):
        raise NotImplemented

    def _PX_(self):
        raise NotImplemented

    def _TX_(self):
        raise NotImplementeds

    def __test(self):
        if __debug:
            if __test:
                return __test


if __name__ == "__main__":
    vm = VM()