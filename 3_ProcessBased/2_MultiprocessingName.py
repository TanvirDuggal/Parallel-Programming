# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 14:47:44 2019

@author: Tanvir.Duggal
"""

import multiprocessing

def foo():
    print("Process working " + multiprocessing.current_process().name)
    
    
if __name__  == '__main__':
    p1 = multiprocessing.Process(name = 'P1', target = foo)
    p2 = multiprocessing.Process(target = foo)
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()