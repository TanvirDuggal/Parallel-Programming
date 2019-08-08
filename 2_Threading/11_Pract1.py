# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 10:29:02 2019

@author: Tanvir.Duggal
"""

import threading
import time

item = []

lock = threading.Lock()

def emptyList():
    while True:
        lock.acquire()
        if len(item) <= 0:
            lock.release()
            break
        else:
            item.pop()
            lock.release()
#            print("Length of Item left : " + str(len(item)) + " Thread Worker : " + str(threading.current_thread().getName()))
        return
    
def main():
    
    for i in range(1000000):
        item.append(1)
    a1 = time.time()    
    t1 = threading.Thread(target=emptyList)
    t2 = threading.Thread(target=emptyList)
    t3 = threading.Thread(target=emptyList)
    
    t1.start()
    t2.start()
    t3.start()
    
    t1.join()
    t2.join()
    t3.join()
    
    print("Thread Ended")
    a2 = time.time()
    
    print("Time Used : " + str(a2-a1))
    
def main2():
    for i in range(1000000):
        item.append(1)
    a1 = time.time()    
    while True:
        if len(item) <= 0:
            break
        else:
            item.pop()
            
    print("Ended")
    a2 = time.time()
    print("Time Used : " + str(a2-a1))

if __name__ == '__main__':
    main()
    main2()
    
