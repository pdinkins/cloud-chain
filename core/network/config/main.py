# -*- coding: utf-8 -*-
__package__ = "cloud-chain.core.network.config.main"
__version__ = "0.1.3"

debug = True

from socket import gethostname
from socket import gethostbyname

class HOST:
    
    @staticmethod
    def _get_host_ip():
        try:
            __host_name = gethostname()
            __host_ip = gethostbyname(__host_name)
            if debug:
                print(__host_ip)
            return __host_ip
        except Exception as error:
            print(error)