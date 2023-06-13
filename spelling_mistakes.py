from autocorrect import Speller

spell = Speller(lang='en')

def auto_correct(word):
    return spell(word)
