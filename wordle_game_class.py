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
        self.round = 0
        self.valid_words = valid_words
        self.valid_solutions = valid_solutions
        self.colors = {}
        self.tries = {}
        self.secret_word = None
        self.status = None
        
    
    def define_secret(self, secret_word):
        if secret_word in self.valid_solutions:
            self.secret_word = secret_word
        else:
            print('Invalid word. Try again.')
        
    
    def try_word(self, guess):
        if guess in self.valid_words:
            self.round += 1
            self.tries[self.round] = guess
            self.colors[self.round] = {}
            
            if self.secret_word == None:
                for i in range(5):
                    self.colors[self.round][i] = input(f'Write the colors of the letter: {i+1}')
            
            else:
                for i in range(5):
                    if guess[i] == self.secret_word[i]:
                        self.colors[self.round][i] = 'green'
                        
                        
                    elif guess[i] in self.secret_word:
                        self.colors[self.round][i] = 'yellow'
        
                    else:
                        self.colors[self.round][i] = 'black'
            
            self.check_status()
                    
        else:
            print('Invalid word. Try again.')
    
    
    def check_status(self):
        if self.round == 6:
            self.status = 'end'
            
        elif self.colors[self.round] == {0: 'green', 1: 'green', 2: 'green', 3: 'green', 4: 'green'}:
            self.status = 'end'
        
        else:
            self.status = 'playing'
            
    
class WordleBot():
    def __init__(self):
        self.valid_words = None
        self.left_words = None
        self.must_letters = []
        self.green_letters = []
        self.black_letters = []
        self.wordle = None
        
    
    def get_wordle_game(self, wordle):
        self.wordle = wordle
        self.valid_words = wordle.valid_words
        self.left_words = wordle.valid_solutions
        
        
    def solve_wordle(self):
        pass
    
    
    def update_left_words(self):
        pass
    
    
    def word_selector(self):
        pass
        
    
            
        
    
wordle = WordleGame(valid_words, valid_solutions)

wordle.define_secret('hello')

wordle.try_word('hello')

wordle.colors
