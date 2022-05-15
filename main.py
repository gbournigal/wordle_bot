# -*- coding: utf-8 -*-
"""
Created on Sat May 14 16:40:58 2022

@author: georg
"""

import pandas as pd
import random
import streamlit as st
from wordle_game_class import WordleGame, WordleBot, valid_words, valid_solutions

st.header('Wordle Bot Solver')

if 'wordle' not in st.session_state:
    st.session_state['wordle'] = WordleGame(valid_words, valid_solutions)

    
st.session_state['wordle'] = WordleGame(valid_words, valid_solutions) 
secret_word = str.lower(st.text_input('Define the secret word for the Bot', value='hello', max_chars=5))
if secret_word not in valid_solutions:
    st.write('The word is not valid, try again.')
else:
    st.session_state['wordle'].define_secret(secret_word)
    wordlebot = WordleBot()
    wordlebot.get_wordle_game(st.session_state['wordle'])
    wordlebot.solve_wordle()
    
    
    tries = []
    for i in st.session_state['wordle'].tries:
        tries.append(list(st.session_state['wordle'].tries[i]))
    df = pd.DataFrame(tries, columns=['1', '2', '3', '4', '5'])
    
    def style_specific_cell(x):
        df1 = pd.DataFrame('', index=x.index, columns=x.columns)
        for i in st.session_state['wordle'].colors.keys():
            for j in range(5):
                df1.iloc[i-1, j] = f"background-color: light{st.session_state['wordle'].colors[i][j]}"
        return df1
    
    st.write(df.style.apply(style_specific_cell, axis=None))
        