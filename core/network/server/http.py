# -*- coding: utf-8 -*-
__package__ = "cloud-chain.core.network.server.http"
__version__ = "0.1.3"

import os
from wsgiref.simple_server import make_server

# Windows http server instance with debug command prompt window
def HOST_LOCAL_HTTP_SERVER_WIN():
    # Assumes the machine is windows and spawns a seperate command prompt window
    os.system("start py -m http.server --bind 127.0.0.1")

def APPLICATION(environ, start_response):
    response_body = [
        '{key}: {value}'.format(key=key, value=value) for key, value in sorted(environ.items())
    ]
    response_body = '\n'.join(response_body)
    status = '200 ok'
    response_headers = [
        {'Content-type', 'text/plain'},
    ]
    start_response(status, response_headers)
    return [response_body.encode('utf-8')]

def START_APP():
    server = make_server("localhost", 8000, app=APPLICATION)
    server.serve_forever()