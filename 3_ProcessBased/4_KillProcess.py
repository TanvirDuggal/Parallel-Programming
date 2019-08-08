# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 11:20:12 2019

@author: Tanvir.Duggal
"""

import multiprocessing
import time

def foo():
    print("Start Process")
    time.sleep(0.1)
    print("End Process")
    
if __name__ == '__main__':
    p = multiprocessing.Process(target = foo)
    print("Process before execution : ", p, p.is_alive())
    
    p.start()
    print("Process running : ", p, p.is_alive())
    
    p.terminate()
    print("Process terminated : ", p, p.is_alive())
    
    p.join()
    print("Process join : ", p, p.is_alive())

    print("Exit Code    : ", p.exitcode)