""" synonyms.py - Schnittstelle um die Synonyme aus der Datei auszulesen """

# imports
import json
import search_history
import spelling_mistakes


# holen der Synonyme für ein Wort
def get_synonyms(word):
    data = get_json_data()
    synonyms = get_word_data(data, word.lower())

    # falls das wort falsch geschrieben ist und deswegen keine synonyme gefunden werden, wird nach synonymen für die korrigierte version geschaut
    if len(synonyms) < 1:
        word = spelling_mistakes.auto_correct(word).lower()
        synonyms = get_word_data(data, word)

    search_history.add_search(word)

    return synonyms, word


# Data aus der Datei holen
def get_json_data():
    with open("data/synonyms_data.json", "r") as file:
        return json.loads(file.read())


# Synonyme für das bestimmte gesuchte Wort holen
def get_word_data(data, word):
    return_data = []
    try:
        return_data = data["synonyms"][word]
    except:
        # falls das wort nicht gefunden wird
        return_data = []

    return return_data

