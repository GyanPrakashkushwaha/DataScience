import logging

"""If we don't define levels this from warning so to print from start I have to define level"""

# filemode in 'logging.basicConfig' is by default a (means append)

""" To save all information we need to set filename ....."""
logging.basicConfig(filename='learn.log',level=logging.DEBUG,filemode='w' # this filemode will reload complete data 
            
            
            ) # to see level concept do comment down this and see

logging.debug(' debug message') # 10
logging.info('info message') # 20
logging.warning('warning message') # 30
logging.error('error message') # 40
logging.critical('critical message') # 50