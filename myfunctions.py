import flet as ft
import random as rd
import re

#Level of security
def number_and_letters(string):
    ""
    if re.search(r'[a-zA-Z]', string) and re.search(r'\d', string):
        return True
    return False

def and_special_char(string):
    if number_and_letters(string):
        if re.search(r'[\w\s]'):
            return True
    return False
