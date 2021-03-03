# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 16:47:42 2021

@author: Rajat Verma
"""

import json

data = json.load(open("data.json"))

# Counting the number of items in file

count = 0

for item in data:
    count = count + 1
    
print(count)

# function for finding the entered word and returning its meaning

def find_word(word):
    word = word.lower()
    if word in data:
        return data["word"]
    elif len(get_close_matches(word, data.keys(), 5)) > 0:
        list = get_close_matches(word, data.keys(), 5)
        for item in list:
            print("Is {} the word you wanted to search ? ".format(item))
            dec = input("press y for yes and n for next word, press e for exiting: \n")
            if dec.lower() == "y":
                return data[item]
            elif dec.lower() == "n":
                continue
            else:
                return False
    else:
        return False
    
# Function for dictionary    
from difflib import get_close_matches
def run_dict():
    cond = True
    while cond:
        word = input("Please enter the word you want to search: \n")
        if find_word(word) != False:
            print("This is the meaning of {} ".format(word))
            print(find_word(word))
            dec = input("do you want to continue ?, press y for yes else any key for no: \n")
            if dec.lower() == 'y':
                continue
            else:
                cond = False
                break
        else:
            print("The word you entered can not be found, do yoy want to try again ?")
            dec = input("Enter y for yes and any other key for exiting: \n")
            if dec.lower() == "y":
                continue
            else:
                cond = False
            
run_dict()
            