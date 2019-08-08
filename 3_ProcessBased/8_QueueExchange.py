# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 11:16:13 2019

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
            print("Produced : " + str(item) + " Appended to : " + str(self.name))
            time.sleep(1)
            
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
                print("Consumed : " + str(item) + " from : " + str(self.name))
                time.sleep(1)
                
if __name__ == '__main__':
    queue = multiprocessing.Queue()
    m1 = producer(queue)
    m2 = consumer(queue)
    
    m1.start()
    m2.start()
    
    m1.join()
    m2.join()