# -*- coding: utf-8 -*-
__package__ = "cloud-chain.core.logger.main"
__version__ = "0.1.4"

# IMPORTS #
# python library imports
import logging
import inspect
import datetime

# pass a message and log to your hearts desire
def CORE_LOGGER(msg):
    logging.basicConfig(level=logging.DEBUG,)
    current_function = inspect.currentframe().f_back.f_code
    return logging.debug("{}\t{}\t{}\t{}".format(
            datetime.datetime.now(),
            current_function.co_filename,
            current_function.co_name,
            msg))

# this does not work. get rid of classes. functional module
class cCORE_LOGGER:
    def __init__(self, msg):
        logging.basicConfig(level=logging.DEBUG, format='%(name)s: %(messsage)s',)
        self.msg = msg
        self._log(self.msg)
    
    def _log(self, message):
        self.__current_function = inspect.currentframe().f_back.f_code
        #logging.basicConfig(level=logging.DEBUG, format='%(name)s: %(messsage)s',)
        return logging.debug("{}\t{}\t{}\t{}".format(
            datetime.datetime.now(),
            self.__current_function.co_filename,
            self.__current_function.co_name,
            message))

