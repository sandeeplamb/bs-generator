#!/usr/bin/env python3.7
# coding: utf-8
"""
    Generat Bull-Shit for your Manager
    Handy tool to save your time to innovate
"""


import random
import sys

def select_bs_word(filename):
    """
    Select Random Word from File
    """
    with open(filename, 'r') as fname:
        return random.choice(fname.readlines()).replace('\n', '')

def generate_bs():
    """
    Generate now
    """
    print(select_bs_word("adverbs")+" "+
        select_bs_word("verbs")+" "+
        select_bs_word("adjectives")+" "+
        select_bs_word("nouns"))


#############################################
### 
if __name__ == "__main__":
    generate_bs()
else:
    print("Not a Script. Exiting now...")
    sys.exit(2)