# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 15:07:27 2019

@author: Tanvir.Duggal
"""

import threading
import time

exit_flag = 0

class myThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name     = name
        self.counter  = counter
        
    def run(self):
        print("Starting " + self.name)
        print_time(self.name, self.counter, 5)
        print("Exiting  " + self.name)
    

def print_time(threadName, delay, counter):
    while counter:
        if exit_flag:
            thread.exit()
        time.sleep(delay)
        print(threadName + str(time.ctime(time.time())))
        counter -= 1
        

if __name__ == '__main__':
    thread1 = myThread(1, 'T1', 1)
    thread2 = myThread(2, 'T2', 2)
    
    thread1.start()
    thread2.start()
    
    thread1.join()
    thread2.join()