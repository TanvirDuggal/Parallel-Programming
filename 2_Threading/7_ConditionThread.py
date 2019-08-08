# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 10:07:43 2019

@author: Tanvir.Duggal
"""

import threading
import time

items = []
condition = threading.Condition()

class consumer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        
    def consume(self):
        global items
        global condition
        
        condition.acquire()
        if len(items) == 0:
            condition.wait()
            print("Consumer Waiting as no items available")
            
        items.pop()
        print("Consumer consumed 1 item, Length of item remaining : " + str(len(items)))
        
        condition.notify()
        condition.release()
        
    def run(self):
        for i in range(10):
            time.sleep(10)
            self.consume()


class producer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        
    def produce(self):
        global items
        global condition
        
        condition.acquire()
        if len(items) == 10:
            condition.wait()
            print("Producer Waiting as items is full")
            
        items.append(1)
        print("Producer added 1 item, Length of item remaining : " + str(len(items)))
        
        condition.notify()
        condition.release()

    def run(self):
        for i in range(10):
            time.sleep(5)
            self.produce()        
        
def main():
    t1 = consumer()
    t2 = producer()

    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    
    print("Thread Ended")
    
if __name__ == '__main__':
    main()