from autocorrect import Speller

spell = Speller(lang='en')

# korrigiert mögliche kleine rechtschreibfehler
def auto_correct(word):
    return spell(word)

