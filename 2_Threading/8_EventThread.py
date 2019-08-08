# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 11:17:51 2019

@author: Tanvir.Duggal
"""

import threading
import time
import random

items = []
event = threading.Event()

class consumer(threading.Thread):
    def __init__(self, items, event):
        threading.Thread.__init__(self)
        self.items = items
        self.event = event
        
    def run(self):
        while True:
            time.sleep(2)
            self.event.wait()
            item = self.items.pop()
            print("Consumer consumed " + str(item) + " , popped from list " + self.name)
            
class producer(threading.Thread):
    def __init__(self, integers, event):
        threading.Thread.__init__(self)
        self.items = items
        self.event = event
        
    def run(self):
        global item
        for i in range(10):
            time.sleep(2)
            item = random.randint(0,256)
            self.items.append(item)
            print("Producer produced " + str(item) + " , appended into " + str(self.name))
            self.event.set()
            self.event.clear()
            
            
if __name__ == '__main__':
    t1 = consumer(items, event)
    t2 = producer(items, event)

    t1.start()
    t2.start()
    
    t1.join()
    t2.join()