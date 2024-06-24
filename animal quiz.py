# -*- coding: utf-8 -*-
"""
Created on Fri May 31 18:25:00 2024

@author: LENOVO
"""

score=0
print('Guess the animal!')

def check_guess(guess, answer):
    global score
    if guess.lower() == answer.lower():
        print ('Correct answer')
        score=score+1
        
guess1=input('Which bear lives at the north pole?')
check_guess(guess1, 'polar bear')

guess2=input('which is the fastest animal?')
check_guess(guess2, 'cheetah')

guess3=input('which is the largest animal?')
check_guess(guess3, 'blue whale')
        
print('your score is' +str(score))


        