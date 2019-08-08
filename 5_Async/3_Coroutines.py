# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 15:19:18 2019

@author: Tanvir.Duggal
"""

import asyncio
import time
from random import randint

import nest_asyncio
nest_asyncio.apply()

@asyncio.coroutine
def Start_State():
    print("Start state called")
    input_value = randint(0,1)
    time.sleep(1)
    if input_value == 0:
        result = yield from State2(input_value)
    else:
        result = yield from State1(input_value)
    print("Resume of Transition : " + result)
    
@asyncio.coroutine
def State1(transition_value):
    output_value = str("State 1 with transition value : " + str(transition_value))
    input_value = randint(0,1)
    time.sleep(1)
    print("Evaluating in STATE 1 with value : " + str(input_value))
    if input_value == 0:
        result = yield from State2(input_value)
    else:
        result = yield from Final_State(input_value)
    return (output_value + str(result))

@asyncio.coroutine
def State2(transition_value):
    output_value = str("State 2 with transition value : " + str(transition_value))
    input_value = randint(0,1)
    time.sleep(1)
    print("Evaluating in STATE 2 with value : " + str(input_value))
    if input_value == 0:
        result = yield from State1(input_value)
    else:
        result = yield from Final_State(input_value)
    return (output_value + str(result))
        
@asyncio.coroutine
def Final_State(transition_value):
    output_value = str("End of transition value : " + str(transition_value))
    print("STOPPING COMPUTING")
    return output_value

if __name__ == '__main__':
    print("Finite State Machine Simulation")
    loop = asyncio.get_event_loop()
    loop.run_until_complete(Start_State())