
from sys import *

try:
    a = 1/0
except Exception as e:
    _,_,exc_tb = exc_info()
    fileName = exc_tb.tb_frame.f_code.co_filename
    print(exc_tb.tb_lineno)
    print(fileName)

    