# -*- coding: utf-8 -*-
__package__ = "cloud-chain.core.network.main"
__version__ = "0.1.3"

import socket
from server.main import SERVER
from client.main import CLIENT
from config.main import *

class CORE_NETWORK:
    def __init__(self):
        self.ip = HOST._get_host_ip()


if __name__ == "__main__":
    c = CORE_NETWORK()


