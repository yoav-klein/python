
#####################################################
#
#       Demonstrates how to set the logging level
#       from the command line
#
#
##################################################

import argparse
import logging

def configure_logger(loglevel):
    
    log_level_numeric_value = getattr(logging, loglevel.upper(), None)
    if not isinstance(log_level_numeric_value, int):
        print("Invalid log level: %s" % loglevel)
        raise ValueError('Invalid log level: %s' % loglevel)
    
    logging.basicConfig(level=log_level_numeric_value)

def main():
    parser = argparse.ArgumentParser(description='My application')
    parser.add_argument('--loglevel', help="Set the loglevel: debug, info, warning, error",
                        default="warning")
    
    args = parser.parse_args()
    configure_logger(args.loglevel)

    logging.debug('Debugging info')


if __name__ == "__main__":
    main()