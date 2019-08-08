# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 11:54:59 2019

@author: Tanvir.Duggal
"""

import threading
import logging

logging.basicConfig(level  = logging.DEBUG,
                    format = '(%(threadName)-10s) %(message)s',)

def threading_with(statement):
    with statement:
        logging.debug("Acquired via with statememt " + str(statement))
        
def threading_without(statement):
    statement.acquire()
    try:
        logging.debug("Acquired directly " + str(statement))
    finally:
        statement.release()
        
        
if __name__ == '__main__':
    lock  = threading.Lock()
    rLock = threading.RLock()
    condition = threading.Condition()
    mutex     = threading.Semaphore(1)
    
    threadList = [lock, rLock, condition, mutex]
    
    for i in threadList:
        print("--------- " + str(i) + " ------------")
        t1 = threading.Thread(target=threading_with, args=(i,))
        t2 = threading.Thread(target=threading_without, args=(i,))
        
        t1.start()
        t2.start()
        
        t1.join()
        t2.join()