
##################################################
#
#       Demonstrations of simple usage of logging
#
#####################################################

import logging

def simple_example():
    """
    by default, the severity level is set to WARNING, so you won't see the info message
    """
    logging.warning('Watch out!')
    logging.info('Told you so')

def write_to_file():    
    logging.basicConfig(filename='example.log',level=logging.DEBUG)
    logging.debug('This message should go to the log file')
    logging.info('So should this')
    logging.warning('And this, too')

def log_variables():
    obj = "Apple"
    color = "Red"
    logging.warning("my %s is %s", obj, color)


def setting_format():
    logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
    logging.debug('This message should appear on the console')
    logging.info('So should this')
    logging.warning('And this, too')

setting_format()
#log_variables()
#write_to_file()
#simple_example()


