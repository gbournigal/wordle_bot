# -*- coding: utf-8 -*-
"""
Created on Tue May 10 15:20:57 2022

@author: gbournigal
"""


import string
import time
from collections import Counter

valid_words = []
valid_solutions = []

with open('words\wordle-words.txt', "r") as f:
    for line in f:
        valid_words.extend(line.split())
        

with open('words\wordle-solutions.txt', "r") as f:
    for line in f:
        valid_solutions.extend(line.split())
        
valid_letters = {i: [0, 1, 2, 3, 4] for i in string.ascii_lowercase}


 
class WordleGame():
    def __init__(self, valid_words, valid_solutions):
        valid_letters = {i: [0, 1, 2, 3, 4] for i in string.ascii_lowercase}
        self.round = 0
        self.valid_words = valid_words
        self.valid_solutions = valid_solutions
        self.valid_letters = valid_letters
        self.colors = {}
        self.tries = {}
        self.secret_word = None
        
    
    def define_secret(self, secret_word):
        self.secret_word = secret_word
        
    
    def check_valid_word(self, guess):
        pass
        
    def try_word(self, guess):
        if guess in self.valid_letters:
            
            for i in range(5):
                if guess[i] == self.secret_word[i]:
                    self.colors[i] = 'green'
                    
                    
                elif guess[i] in self.secret_word:
                    self.colors[i] = 'yellow'
    
                else:
                    self.colors[i] = 'black'
                    
            self.round += 1
        
        else:
            print('Invalid word. Try again')
        
    
