# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 12:04:18 2019

@author: Tanvir.Duggal
"""

import os
import sys

program = 'python'
print('Calling Process')

argument = ['process.py']

os.execvp(program, (program,) + tuple(argument))