# -*- coding: utf-8 -*-
"""
Created on Mon May  9 15:51:45 2022

@author: gbournigal
"""


import string
import time

valid_words = []

with open('words\wordle-words.txt', "r") as f:
    for line in f:
        valid_words.extend(line.split())
        

letter_position = {i: [0, 1, 2, 3, 4] for i in string.ascii_lowercase}

letter_position['a'].remove(0)

words_to_delete = []

start = time.time()
for i in valid_words:
    for k in range(5):
        if k not in letter_position[i[k]]:
            words_to_delete.append(i)
            break
            
new_valid_words = list(set(valid_words) - set(words_to_delete))
end = time.time()

print(end - start)
