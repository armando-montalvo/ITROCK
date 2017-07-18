# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 09:41:51 2017

@author: Mario
"""



def search4vowels(phrase:str)-> set:
    vowels=set('aeiou')
    return vowels.intersection(set(phrase))


def search4letters(phrase:str,letters:str)-> set:
    return set(letters).intersection(set(phrase))

