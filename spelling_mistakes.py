"""
    spelling_mistakes.py - Modul um Rechtschreibfehler zu korrigieren
"""

# imports
from autocorrect import Speller

spell = Speller(lang='en')

# korrigiert mögliche kleine Rechtschreibfehler
def auto_correct(word):
    return spell(word)
