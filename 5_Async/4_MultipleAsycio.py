# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 10:42:30 2019

@author: Tanvir.Duggal
"""

import asyncio

import nest_asyncio
nest_asyncio.apply()

@asyncio.coroutine
def factorial(number):
    f = 1
    for i in range(2, number+1):
        print("Asyncio.Task : Compute Factorial : " + str(i))
        yield from asyncio.sleep(1)
        f *= i
    print("Asyncio.Task factorial : " + str(f))
    
@asyncio.coroutine
def fibonacci(number):
    a,b = 0,1
    for i in range(number):
        print("Asyncio.Task : Computer Fibonacci : " + str(i))
        yield from asyncio.sleep(1)
        a,b = b, a+ b
        print("Asyncio.Task : Fibnacco : " + str(a))
        
@asyncio.coroutine
def binomialCoeff(n, k):
    result = 1
    for i in range(1, k+1):
        result = result * ((n-i+1)/i)
        print("Asyncio.Task : Computer Binomial : " + str(i))
        yield from asyncio.sleep(1)
    print("Asyncio.Task : Binomial Coeff : " + str(result))
    
if __name__ == '__main__':
        tasks = [asyncio.Task(factorial(10)),
                 asyncio.Task(fibonacci(10)),
                 asyncio.Task(binomialCoeff(20, 10))]
        
        loop  = asyncio.get_event_loop()
        loop.run_until_complete(asyncio.wait(tasks))
        loop.close()