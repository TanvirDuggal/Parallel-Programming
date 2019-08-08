# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 14:21:02 2019

@author: Tanvir.Duggal
"""

import asyncio
import sys

@asyncio.coroutine
def first_coroutine(future, N):
    count = 0
    for i in range(N):
        count += 1
    yield from asyncio.sleep(4)
    future.set_result("First Coroutine, Sum of Integers      : " + str(count))
    
@asyncio.coroutine
def second_coroutine(future, N):
    count = 0
    for i in range(N):
        count *= i
    yield from asyncio.sleep(4)
    future.set_result("Second Coroutine, Multiple of Integers : " + str(count))
    
def got_result(future):
    print(future.result())
    
if __name__ == '__main__':
    N1 = int(sys.argv[1])
    N2 = int(sys.argv[2])
    
    loop = asyncio.get_event_loop()
    future1 = asyncio.Future()
    future2 = asyncio.Future()
    
    tasks   = [
                first_coroutine(future1, N1),
                second_coroutine(future2, N2)
            ]
    
    future1.add_done_callback(got_result)
    future2.add_done_callback(got_result)
    
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()