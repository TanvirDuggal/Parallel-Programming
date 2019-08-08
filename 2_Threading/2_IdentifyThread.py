# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 14:46:41 2019

@author: Tanvir.Duggal
"""

import threading
import time

def thread_1():
    print(threading.current_thread().getName() + " is running")
    time.sleep(2)
    print(threading.current_thread().getName() + " still exists")
    return

def thread_2():
    print(threading.current_thread().getName() + " is running")
    time.sleep(2)
    print(threading.current_thread().getName() + " still exists")
    return

def thread_3():
    print(threading.current_thread().getName() + " is running")
    time.sleep(2)
    print(threading.current_thread().getName() + " still exists")
    return


if __name__ == '__main__':
    t1 = threading.Thread(
                name   = 'first_function',
                target = thread_1
            )
    
    t2 = threading.Thread(
                name   = 'second_function',
                target = thread_2
            )
    
    t3 = threading.Thread(
                name   = 'third_function',
                target = thread_3
            )
    
    t1.start()
    t2.start()
    t3.start()
    
    t1.join()
    t2.join()
    t3.join()