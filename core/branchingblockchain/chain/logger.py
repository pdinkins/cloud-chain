'''
# Logging Module:

USE:
    1. from modules._log import log
    2. log('log message')

TODO:
    add functionality so logging can be dynamically turned on and off. 
'''

def log(message):
    import inspect
    import logging
    import datetime as dt
    logging.basicConfig(level=logging.DEBUG, format='%(message)s')
    func = inspect.currentframe().f_back.f_code
    logging.debug("{}\t{}\t{}\t{}".format(
        dt.datetime.now(),
        func.co_filename,
        func.co_name,
        message))
