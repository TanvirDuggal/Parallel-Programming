# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 16:05:38 2019

@author: Tanvir.Duggal
"""

import threading
import time
import random

semaphores = threading.Semaphore(0)

def consumer():
    print("Consumer is waiting")
    semaphores.acquire()
    print("Consumer Notify : consumed item number " + str(item))
    
def producer():
    global item
    time.sleep(10)
    item = random.randint(0, 1000)
    print("Producer notify : producted item number " + str(item))
    semaphores.release()
    
def main():
    t1 = threading.Thread(target = consumer)
    t2 = threading.Thread(target = producer)
    
    t1.start()
    t2.start()

    t1.join()
    t2.join()    

if __name__ == '__main__':
    main()