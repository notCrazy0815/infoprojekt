"""
    synonyms.py - Schnittstelle um die Synonyme aus der Datei auszulesen
"""

# imports
import json
import os

import spelling_mistakes


# holen der Synonyme für ein Wort
def get_synonyms(word, search_history, auto_correct, search_history_enabled):
    data = get_json_data(word[0])
    synonyms = get_word_data(data, word.lower())

    if auto_correct:
        # falls das Wort falsch geschrieben ist und deswegen keine Synonyme gefunden werden, wird nach Synonymen für
        # die korrigierte Version geschaut
        if len(synonyms) < 1:
            word = spelling_mistakes.auto_correct(word).lower()
            synonyms = get_word_data(data, word)

    # Wenn Suchverlauf aktiviert ist, füge diese Suche hinzu
    if search_history_enabled:
        search_history.add_search(word)

    return synonyms, word


# Daten aus der Datei laden
def get_json_data(char):
    if not os.path.exists(f"data/synonyms/{char}/data.json"):
        return {"synonyms": []}

    with open(f"data/synonyms/{char}/data.json", "r") as file:
        return json.loads(file.read())


# Synonyme für das bestimmte gesuchte Wort laden
def get_word_data(data, word):
    return_data = []

    for i in range(len(data)):
        if data[i]["word"] == word:
            for j in range(len(data[i]["synonyms"])):
                return_data.append(data[i]["synonyms"][j])

    return_data.sort()

    return return_data


# Autovervollständigung
def get_auto_complete(text):
    data = get_json_data(text[0])

    return_data = []

    # Suche nach Wörtern, die mit dem Text beginnen
    for i in range(len(data)):
        if data[i]["word"].startswith(text):
            return_data.append(data[i]["word"])

    return return_data

