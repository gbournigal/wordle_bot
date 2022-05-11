# -*- coding: utf-8 -*-
"""
Created on Mon May  9 15:51:45 2022

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
        self.left_words = valid_solutions
        self.valid_letters = valid_letters
        self.colors = {}
        self.tries = {}
        self.must_letters = []
        self.green_letters = []
        self.black_letters = []
        
    
    def delete_unvalid_words(self):
        words_to_delete = []
        for i in self.left_words:
            for k in range(5):
                if k not in self.valid_letters[i[k]]:
                    words_to_delete.append(i)
                    break
         
        if any(self.must_letters):
            for i in self.left_words:
                if all(letter not in self.must_letters for letter in i):
                    words_to_delete.append(i)

        
        self.words_to_delete = words_to_delete
        self.left_words = list(set(self.left_words) - set(words_to_delete))
        
    
    def try_word(self, secret_word, guess, must_letters = []):
        for i in range(5):
            if guess[i] == secret_word[i]:
                self.colors[i] = 'green'
                for j in self.valid_letters.keys():
                    if j != guess[i]:
                        try:
                            self.valid_letters[j].remove(i)
                        except Exception:
                            pass
                            # print(f'La {j} ya se eliminó de la posición {i}')
                self.must_letters.append(guess[i])
                self.green_letters.append(guess[i])
                
            elif guess[i] in secret_word:
                self.colors[i] = 'yellow'
                try:
                    self.valid_letters[guess[i]].remove(i)
                except Exception:
                    pass
                    # print(f'La {guess[i]} ya se eliminó de la posición {i}')
                self.must_letters.append(guess[i])
            else:
                self.colors[i] = 'black'
                self.valid_letters[guess[i]] = []
                self.black_letters.append(guess[i])
                
        self.delete_unvalid_words()
        self.round += 1
    
    
    def word_selector(self):
        counts = Counter(letter for word in self.left_words for letter in word)
        for i in self.green_letters:
            del counts[i]
        words_values = {}
        for i in self.valid_words:
            value = 0
            for j in set(i):
                value += counts[j]
            words_values[i] = value
        
        if len(self.left_words) == 1:
            self.selected_word = self.left_words[0]
        else:
            self.selected_word = max(words_values, key=words_values.get)
        print(self.selected_word)
        return self.selected_word
        

wordle = WordleGame(valid_words, valid_solutions)



word = wordle.word_selector()



wordle.try_word('cigar', word)
len(wordle.left_words)

