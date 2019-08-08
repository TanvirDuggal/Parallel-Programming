# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 11:48:50 2019

@author: Tanvir.Duggal
"""

import multiprocessing
import time
import datetime

def testBarrier(synchronizer, serializer):
    name = multiprocessing.current_process().name
    synchronizer.wait()
    now = time.time()
    with serializer:
        print("Process : " + str(name) + " -> " + str(datetime.datetime.fromtimestamp(now)))

def testNoBarrier():
    name = multiprocessing.current_process().name
    now = time.time()
    print("Process : " + str(name) + " -> " + str(datetime.datetime.fromtimestamp(now)))


if __name__ == '__main__':
    synchronizer = multiprocessing.Barrier(2)
    serializer   = multiprocessing.Lock()
    
    multiprocessing.Process(name = "P1", target=testBarrier, args=(synchronizer, serializer)).start()
    multiprocessing.Process(name = "P2", target=testBarrier, args=(synchronizer, serializer)).start()
    
    multiprocessing.Process(name = "P11", target=testNoBarrier).start()
    multiprocessing.Process(name = "P22", target=testNoBarrier).start()
    
    