# -*- coding: utf-8 -*-
"""
Created on Tue May 10 15:20:57 2022

@author: gbournigal
"""


import string
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
        valid_letters = {i: [0, 1, 2, 3, 4] for i in string.ascii_lowercase}
        self.left_words = None
        self.must_letters = []
        self.valid_letters = valid_letters
        self.green_letters = []
        self.wordle = None
        
    
    def get_wordle_game(self, wordle):
        self.wordle = wordle
        self.left_words = wordle.valid_solutions
        
        
    def solve_wordle(self):
        if self.wordle.round != 0:
            self.update_left_words()
            
        
        while self.wordle.status != 'end':
            guess = self.word_selector()
            self.update_left_words(guess=guess, copy=False)
            
    
    def update_left_words(self, guess=None, copy=True):
        wordle_cp = self.wordle
        valid_letters_cp = self.valid_letters
        must_letters_cp = self.must_letters
        green_letters_cp = self.green_letters
             
        if guess == None:
            pass
        else:
            wordle_cp.try_word(guess)
            
        for i in wordle_cp.tries.keys():
            for j in range(len(wordle_cp.tries[i])):
                if wordle_cp.colors[i][j] == 'green':
                    for k in valid_letters_cp.keys():
                        if k !=  wordle_cp.tries[i][j]:
                            try:
                                valid_letters_cp[k].remove(j)
                            except Exception:
                                pass
                    must_letters_cp.append(wordle_cp.tries[i][j])
                    green_letters_cp.append(wordle_cp.tries[i][j])
                        
                elif wordle_cp.colors[i][j] == 'yellow':
                    try:
                        valid_letters_cp[wordle_cp.tries[i][j]].remove(j)
                    except Exception:
                        pass

                    must_letters_cp.append(wordle_cp.tries[i][j])
                
                elif wordle_cp.colors[i][j] == 'black':
                    valid_letters_cp[wordle_cp.tries[i][j]] = []           
            
            
            words_to_delete = []
            for i in self.left_words:
                for k in range(5):
                    if k not in valid_letters_cp[i[k]]:
                        words_to_delete.append(i)
                        break
             
            if any(must_letters_cp):
                for i in self.left_words:
                    if all(letter not in must_letters_cp for letter in i):
                        words_to_delete.append(i)

            
            left_words = list(set(self.left_words) - set(words_to_delete))
            
        if copy and guess is not None:
            return left_words
        
        elif copy == False:
            self.left_words = left_words
            self.wordle = wordle_cp
            self.valid_letters = valid_letters_cp
            self.must_letters = must_letters_cp
            self.green_letters = green_letters_cp
                     
        elif guess == None:
            self.left_words = left_words
            self.wordle = wordle_cp
            self.valid_letters = valid_letters_cp
            self.must_letters = must_letters_cp
            self.green_letters = green_letters_cp
                
                
    def word_selector(self):
        counts = Counter(letter for word in self.left_words for letter in word)
        for i in self.green_letters:
            del counts[i]
        words_values = {}
        for i in self.wordle.valid_words:
            value = 0
            for j in set(i):
                value += counts[j]
            words_values[i] = value
        
        if len(self.left_words) <= 2 or self.wordle.round == 6:
            self.selected_word = self.left_words[0]
        else:
            self.selected_word = max(words_values, key=words_values.get)
        print(self.selected_word)
        return self.selected_word