# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 11:37:22 2019

@author: Tanvir.Duggal
"""

import multiprocessing
import random
import time

class producer(multiprocessing.Process):
    def __init__(self, queue):
        multiprocessing.Process.__init__(self)
        self.queue = queue
            
    def run(self):
        for i in range(10):
            item = random.randint(0, 256)
            self.queue.put(item)
            print("Producer appended item to queue : " + str(item))
            time.sleep(1)
            print("Size of queue : " + str(self.queue.qsize()))
            
class consumer(multiprocessing.Process):
    def __init__(self, queue):
        multiprocessing.Process.__init__(self)
        self.queue = queue
        
    def run(self):
        while True:
            if self.queue.empty():
                print("Queue is empty")
            else:
                time.sleep(2)
                item = self.queue.get()
                print("Consumed : " + str(item) + " from list : " + self.name)
                time.sleep(1)
                
if __name__ == '__main__':
    queue = multiprocessing.Queue()
    t1 = producer(queue)
    t2 = consumer(queue)
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()