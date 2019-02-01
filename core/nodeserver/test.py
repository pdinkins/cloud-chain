'''
# TEST 
# for testing the current build and the chain module

'''

# initial import
try:
    import os, sys
    import platform
    import subprocess
    import requests
    import ipfsapi

except ModuleNotFoundError:
    print('FATALBUILDERROR')
    print(sys.exc_info())

