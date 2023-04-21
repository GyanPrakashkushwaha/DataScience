import logging

"""If we don't define levels this print from warning so to print from start I have to define level # to see level concept do comment down this and see """

# filemode in 'logging.basicConfig' is by default a (means append)

""" To save all information we need to set filename ....."""
logging.basicConfig(filename='learnLogAddtimeDate.log',level=logging.DEBUG,filemode='w' # this filemode will reload complete data 
            ,format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s", # I am changing the format
            datefmt='%d/%b/%Y %I:%M:%S %p'
            ) # to see level concept do comment down this and see

logging.debug(' debug message') # 10
logging.info('info message') # 20
logging.warning('warning message') # 30
logging.error('error message') # 40
logging.critical('critical message') # 50