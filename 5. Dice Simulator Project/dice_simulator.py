# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 16:24:00 2021

@author: Rajat Verma
"""



import random as rd

def roll_dice():
    cond = True
    while cond:
        x = rd.randint(1, 6)
        print(x)
        
        user_input = input("Press \"y\" if you want to roll again \n")
        if user_input.lower() == 'y':
            continue
        else:
            cond = False
       
        

roll_dice()