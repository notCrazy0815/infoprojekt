""" synonyms_formatter.py - formatiert synonyms.json, Ergebnis in synonyms_data.json """
# nur einmalige verwendung

# imports
import json

# zu formatierenden Text einlesen
old_text = ""

with open("data/synonyms.json", "r") as file:
    old_text = file.read()

file.close()

# formatieren
old_text_rows = old_text.split("\n")
synonyms_as_json = json.loads('{ "synonyms": {} }')
for i in range(len(old_text_rows)):
    word_data = json.loads(old_text_rows[i])
    word = word_data["word"]
    synonyms_as_json["synonyms"][word] = word_data

# in neue Datei schreiben
with open("data/synonyms_data.json", "w") as file:
    json.dump(synonyms_as_json, file, indent=2)
