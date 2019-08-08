# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 10:03:56 2019

@author: Tanvir.Duggal
"""

import scoop
import math
import random
import time

def evaluate_points_in_circle(attempts):
    points_fallen_in_unit_disk = 0
    for i in range(0, attempts):
        x = random.random()
        y = random.random()
        
        radius = math.sqrt(x*x + y*y)
        
        if radius < 1:
            points_fallen_in_unit_disk = points_fallen_in_unit_disk + 1
    return points_fallen_in_unit_disk


def pi_calculate_with_MonteCarlo_Method(workers, attempts):
    print("Number of worker %i - number of attempts %i" %(workers, attempts))
    bt = time.time()
    
    evaluate_task = scoop.futures.map(evaluate_points_in_circle, [attempts]*workers)
    taskresult = sum(evaluate_task)
    print("%i points fallen in a unit disk after " %(taskresult/attempts))
    piValue = (4. * taskresult/float(workers*attempts))
    
    computationTime  = time.time()-bt
    print("Value of Pi      : " + str(piValue))
    print("Error Percentage : " + str(((abs(piValue-math.pi)*100)/math.pi)))
    print("Total Time       : " + str(computationTime))
    
if __name__ == "__main__":
    for i in range (1,3):
        pi_calculate_with_MonteCarlo_Method(i*100, i*100)
        print(" ")
