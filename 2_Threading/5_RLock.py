# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 11:10:11 2019

@author: Tanvir.Duggal
"""

import threading
import time

class Box(object):
    lock = threading.RLock()
    
    def __init__(self):
        self.total_time = 0
        
    def execute(self, n):
        Box.lock.acquire()
        self.total_time += n
        Box.lock.release()
        
    def add(self):
        Box.lock.acquire()
        self.execute(1)
        Box.lock.release()
        
    def remove(self):
        Box.lock.acquire()
        self.execute(-1)
        Box.lock.release()
        

def adder(box, items):
    while items > 0:
        print("Add 1 item to box")
        box.add()
        time.sleep(5)
        items -= 1

def remover(box, items):
    while items > 0:
        print("Removing 1 item from box")
        box.remove()
        time.sleep(5)
        items -= 1
        
if __name__ == '__main__':
    items = 5
    print("putting items in box : " + str(items))
    box = Box()
    
    t1 = threading.Thread(target = adder,   args=(box, items))
    t2 = threading.Thread(target = remover, args=(box, items))
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    
    print("Items in box : " + str(box.total_time))