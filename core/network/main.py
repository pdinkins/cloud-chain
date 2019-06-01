# -*- coding: utf-8 -*-
__package__ = "cloud-chain.core.network.main"
__version__ = "0.1.3"

from core.network.server.main import SERVER
from core.network.client.main import CLIENT
from core.network.config.main import *
from core.network.utils import ingest

class CORE_NETWORK:
    def __init__(self):
        self.ip = HOST._get_host_ip()

def test_network():
    c = CORE_NETWORK()
    while True:
        pcks = ingest.INGEST(c.ip)._return_raw_packets()
        print(pcks)

if __name__ == "__main__":
    c = CORE_NETWORK()
    while True:
        pcks = ingest.INGEST(c.ip)._return_raw_packets()
        print(pcks)
