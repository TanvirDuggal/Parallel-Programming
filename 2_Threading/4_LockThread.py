# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 10:39:44 2019

@author: Tanvir.Duggal
"""

import threading

shared_resources_with_lock = 0
shared_resources_no_lock   = 0

count = 100
shared_resources_lock      = threading.Lock()


def increment_with_lock():
    global shared_resources_with_lock
    
    for i in range(count):
        shared_resources_lock.acquire()
        shared_resources_with_lock += 1
        shared_resources_lock.release()
    print("Value : " + str(shared_resources_with_lock))

def decrement_with_lock():
    global shared_resources_with_lock
    
    for i in range(count):
        shared_resources_lock.acquire()
        shared_resources_with_lock -= 1
        shared_resources_lock.release()
    print("Value : " + str(shared_resources_with_lock))

def increment_without_lock():
    global shared_resources_no_lock
    
    for i in range(count):
        shared_resources_no_lock += 1

        
def decrement_without_lock():
    global shared_resources_no_lock
    
    for i in range(count):
        shared_resources_no_lock -= 1


if __name__ == '__main__':
    t1 = threading.Thread(target = increment_with_lock)
    t2 = threading.Thread(target = decrement_with_lock)
    t3 = threading.Thread(target = increment_without_lock)
    t4 = threading.Thread(target = decrement_without_lock)
    
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    
    print("Value with    lock : " + str(shared_resources_with_lock))
    print("Value with No lock : " + str(shared_resources_no_lock))