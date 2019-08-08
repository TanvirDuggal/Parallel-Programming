# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 14:20:24 2019

@author: Tanvir.Duggal
"""

import multiprocessing

def myFun(i):
    print("Called function in process " + str(i))
    return
    
if __name__ == '__main__':
    process_jobs = []
    for i in range(5):
        p = multiprocessing.Process(target=myFun, args=(i,))
        process_jobs.append(p)
        p.start()
        p.join()