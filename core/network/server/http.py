# -*- coding: utf-8 -*-
__package__ = "cloud-chain.core.network.server.http"
__version__ = "0.1.3"

import os

# Windows http server instance with debug command prompt window
def HOST_LOCAL_HTTP_SERVER_WIN():
    # Assumes the machine is windows and spawns a seperate command prompt window
    os.system("start py -m http.server --bind 127.0.0.1")