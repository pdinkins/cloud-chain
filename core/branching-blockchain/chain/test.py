'''
# TEST 
# for testing the current build and the chain module

'''

# initial import
try:
    import os, sys
    import platform
    import subprocess
    import blocks
    import chain
    import classes
    import ipfs
    #import ipfsdaemon
    import ledger
    import menu

except:
    print('FATALBUILDERROR')
    error = sys.exc_info()
    print(error)
    print(sys.exc_info()[0])
    raise

# os definitions
os_name = os.name
os_platform = platform.system() + platform.release()
os_id = os_name + os_platform
print(os_id)

def start():
    if platform.system() == 'Windows':
        os.system("python -i test.py")
    elif platform.system() == 'Darwin':
        os.system("py -i test.py")
    elif platform.system() == "Linux":
        os.system("py -i test.py")


modules = [blocks, chain, classes, ipfs, ledger, menu]

for i in range(0, len(modules)):
    print(modules[i])
    print(dir(modules[i]), '\n\n')
