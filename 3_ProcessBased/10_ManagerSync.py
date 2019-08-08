# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 12:02:03 2019

@author: Tanvir.Duggal
"""

import multiprocessing

def worker(dicto, key, item):
    dicto[key] = item

if __name__ == '__main__':
    mgr   = multiprocessing.Manager()
    dicto = mgr.dict()
    
    jobs  = [multiprocessing.Process(target=worker, args=(dicto, i, i*2)) for i in range(20)]
    
    for j in jobs:
        j.start()
        
    for j in jobs:
        j.join()
        
    print("-> ", dicto)