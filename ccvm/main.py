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
from process.main import OxPR

# TRANSACTION
from transaction.main import TRANSACTION
from transaction.main import OxTX


class VM:
    def __init__(self):
        self.ca = self._CA_
        self.cn = self._CN_
        self.co = self._CO_
        self.cr = self._CR_
        self.er = self._ER_
        self.ex = self._EX_
        self.fx = self._FX_
        self.px = self._PX_
        self.tx = self._TX_
    
    def _CA_(self):
        self._ca = CALL
        self.__ca = OxCA

    def _CN_(self):
        self._cn = CHAIN
        self.__cn = OxCN
    
    def _CO_(self):
        self._co = CLOUD
        self.__co = OxCO
    
    def _CR_(self):
        self._cr = CREATE
        self.__cr = OxCR

    def _ER_(self):
        self._er = ERRROR
        self.__er = OxER

    def _EX_(self):
        self._ex = EXECUTE
        self.__ex = OxEX

    def _FX_(self):
        self._fx = FUNCTION
        self.__fx = OxFX

    def _PX_(self):
        self._px = PROCESS
        self.__px = OxPX

    def _TX_(self):
        self._tx = TRANSACTION
        self.__tx = OxTX


    def __test(self):
        return __test