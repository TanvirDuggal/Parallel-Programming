# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 11:25:54 2019

@author: Tanvir.Duggal
"""

import multiprocessing

class MyProcess(multiprocessing.Process):
    def run(self):
        print('Called run in : ' + self.name)
        return
    
if __name__ == '__main__':
    jobs = []
    
    for i in range(5):
        p = MyProcess()
        jobs.append(p)
        p.start()
        p.join()