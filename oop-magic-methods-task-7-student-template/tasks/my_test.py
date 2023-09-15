from task import LogFile
import time


@LogFile('my_trace.log')
def my_func():
    print('hellow')
    time.sleep(0.001)
    raise ValueError('ruytyet')


my_func()
