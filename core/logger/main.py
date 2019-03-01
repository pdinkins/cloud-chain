# -*- coding: utf-8 -*-
__package__ = "cloud-chain.core.logger.main"
__version__ = "0.1.3"

# IMPORTS #
# python library imports
import logging
import inspect
import datetime

class CORE_LOGGER:
    def __init__(self):
        self.log = self.__log
        
    
    def __log(self, message):
        self.__current_function = inspect.currentframe().f_back.f_code
        logging.basicConfig(level=logging.DEBUG, format='%(name)s: %(messsage)s',)
        return logging.debug("{}\t{}\t{}\t{}".format(
            datetime.datetime.now(),
            self.__current_function.co_filename,
            self.__current_function.co_name,
            message))