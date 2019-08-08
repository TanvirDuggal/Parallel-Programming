# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 10:17:06 2019

@author: Tanvir.Duggal
"""

import concurrent.futures
import time

number_list = [1,2,3,4,5,6,7,8,9,10]

def evaluate_item(x):
    result_item = count(x)
    print("Item : " + str(x) + " result : " + str(result_item))
    
def count(number):
    for i in range(0, 1000000):
        i = i + 1
    return i*number

if __name__ == '__main__':
    start_time = time.process_time()
    
    for item in number_list:
        evaluate_item(item)
        
    print("Sequential execution in : " + str(time.process_time() - start_time)) 
    
    start_time_1 = time.process_time()
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        for item in number_list:
            executor.submit(evaluate_item, item)
            
    print("Thread Pool execution in : " + str(time.process_time()-start_time_1))