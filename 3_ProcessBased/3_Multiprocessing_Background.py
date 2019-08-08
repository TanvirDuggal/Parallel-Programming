# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 10:56:37 2019

@author: Tanvir.Duggal
"""

import multiprocessing
import time

def foo():
    name = multiprocessing.current_process().name
    print("Starting : " + name)
    time.sleep(3)
    print("Exiting  : " + name)
    
    
if __name__ == '__main__':
    background_process = multiprocessing.Process(name='background_process', target=foo)
    background_process.daemon = True
    
    no_background_process = multiprocessing.Process(name ='no_background_process', target = foo)
    no_background_process.daemon = False
    
    background_process.start()
    no_background_process.start()
    
    background_process.join()
    no_background_process.join()