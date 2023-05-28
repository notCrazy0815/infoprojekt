""" synonyms.py - Schnittstelle um die Synonyme aus der Datei auszulesen """

# imports
import json
import os

import spelling_mistakes


# holen der Synonyme für ein Wort
def get_synonyms(word, search_history):
    data = get_json_data(word[0])
    synonyms = get_word_data(data, word.lower())

    # falls das wort falsch geschrieben ist und deswegen keine synonyme gefunden werden, wird nach synonymen für die korrigierte version geschaut
    if len(synonyms) < 1:
        word = spelling_mistakes.auto_correct(word).lower()
        synonyms = get_word_data(data, word)

    search_history.add_search(word)

    return synonyms, word


# Data aus der Datei holen
def get_json_data(char):
    if not os.path.exists(f"data/synonyms/{char}/data.json"):
        return {"synonyms": []}

    with open(f"data/synonyms/{char}/data.json", "r") as file:
        return json.loads(file.read())


# Synonyme für das bestimmte gesuchte Wort holen
def get_word_data(data, word):
    return_data = []

    for i in range(len(data)):
        if data[i]["word"] == word:
            for j in range(len(data[i]["synonyms"])):
                return_data.append(data[i]["synonyms"][j])

    return_data.sort()

    return return_data


def get_auto_complete(text):
    data = get_json_data(text[0])

    return_data = []

    for i in range(len(data)):
        if data[i]["word"].startswith(text):
            return_data.append(data[i]["word"])

    return return_data

