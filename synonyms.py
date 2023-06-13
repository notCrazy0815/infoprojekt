import json
import os

import spelling_mistakes


def get_synonyms(word, search_history, auto_correct, search_history_enabled):
    data = get_json_data(word[0])
    synonyms = get_word_data(data, word.lower())

    if auto_correct:
        if len(synonyms) < 1:
            word = spelling_mistakes.auto_correct(word).lower()
            synonyms = get_word_data(data, word)

    if search_history_enabled:
        search_history.add_search(word)

    return synonyms, word


def get_json_data(char):
    try:
        if not os.path.exists(f"data/synonyms/{char}/data.json"):
            return {"synonyms": []}

        with open(f"data/synonyms/{char}/data.json", "r") as file:
            return json.loads(file.read())
    except Exception as e:
        return {"synonyms": []}


def get_word_data(data, word):
    try:
        return_data = []

        for i in range(len(data)):
            if data[i]["word"] == word:
                for j in range(len(data[i]["synonyms"])):
                    return_data.append(data[i]["synonyms"][j])

        return_data.sort()

        return return_data
    except Exception as e:
        return []


def get_auto_complete(text):
    try:
        data = get_json_data(text[0])

        return_data = []

        for i in range(len(data)):
            if data[i]["word"].startswith(text):
                return_data.append(data[i]["word"])

        return return_data
    except Exception as e:
        return []

