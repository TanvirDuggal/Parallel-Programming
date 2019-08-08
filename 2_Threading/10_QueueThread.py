# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 12:08:47 2019

@author: Tanvir.Duggal
"""

import threading
import queue
import time
import random

class producer(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue
        
    def run(self):
        for i in range(10):
            item = random.randint(0, 256)
            self.queue.put(item)
            print("Producer notify : " + str(item) + " Appended by " + str(self.name))
            
class consumer(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue
        
    def run(self):
        while True:
            item = self.queue.get()
            print("Consumer notify : " + str(item) + " popped by " + str(self.name)) 
            
            self.queue.task_done()
            
            
if __name__ == '__main__':
    queue = queue.Queue()
    t1    = producer(queue)
    t2    = consumer(queue)
    t3    = consumer(queue)
    
    t1.start()
    t2.start()
    t3.start()
    
    t1.join()
    t2.join()
    t3.join()