# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 14:23:41 2019

@author: Tanvir.Duggal
"""

import scoop
import operator
import time

def simulateWorkLoad(inputData):
    time.sleep(0.01)
    return sum(inputData)


def compareMapReduce():
    mapScoopTime = time.time()
    res = scoop.futures.mapReduce(simulateWorkLoad, operator.add, list([a] * a for a in range(1000)),
                                  )
    mapScoopTime = time.time() - mapScoopTime
    print("Time Taken : " + str(mapScoopTime))
    
    mapPythonTime = time.time()
    res           = sum(
                        map(
                                simulateWorkLoad, list([a] * a for a in range(1000))
                                ))
    
    mapPythonTime  =time.time() - mapPythonTime
    print("Time Taken : " + str(mapPythonTime))
    
    
if __name__ == '__main__':
    compareMapReduce()