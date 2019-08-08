# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 12:16:25 2019

@author: Tanvir.Duggal
"""

import threading

def fun(i):
    print("Function called by thread : " + str(i))
    
thread = []

for i in range(5):
    t = threading.Thread(target=fun, args=(i,))
    thread.append(t)
    print(str(t.name))
    t.start()
    t.join()
    