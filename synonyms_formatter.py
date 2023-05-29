"""
    synonyms_formatter.py - Formatiert die Quelle (data/synonyms.json) in einzelne Dateien für jedes Zeichen,
    dient nur für uns, wäre später nicht mit im Projekt enthalten
"""

# imports
import json
import os

# Öffnen der Datei
with open("data/synonyms.json", "r") as f:
    # Lesen der Datei
    data = f.read().split("\n")

    # Umwandeln der einzelnen Zeilen in ein JSON-Objekt
    for i in range(len(data)):
        data[i] = json.loads(data[i])

    current_char = ""
    current_char_data = []

    new_data = []

    # Sortieren der Daten nach dem ersten Buchstaben, Aufteilen in einzelne Arrays pro Buchstabe
    for i in range(len(data)):
        char = data[i]["word"][0].lower()

        if current_char == "":
            # bei Vorbelegung
            current_char = char
            current_char_data.append(data[i])
        elif current_char == char:
            # bei gleichem Buchstaben wie dem vorherigen
            current_char_data.append(data[i])
        else:
            # bei anderem Buchstaben als dem vorherigen
            new_data.append({"char": current_char, "data": current_char_data})
            current_char = char
            current_char_data = [data[i]]

    # letztes Array hinzufügen
    new_data.append({"char": current_char, "data": current_char_data})

    # Erstellen der Dateien
    for i in range(len(new_data)):
        if not os.path.exists("data/synonyms/" + new_data[i]["char"]):
            # Datei bzw. Ordner existiert noch nicht
            os.mkdir("data/synonyms/" + new_data[i]["char"])
            with open("data/synonyms/" + new_data[i]["char"] + "/data.json", "w") as file:
                file.write(json.dumps(new_data[i]["data"]))
        else:
            # Datei existiert schon
            # da die Ursprungsdatei nicht vollständig alphabetisch sortiert ist,
            # müssen die Daten aus der Datei nochmal ausgelesen und um die neuen Daten erweitert werden

            old_data = []
            with open("data/synonyms/" + new_data[i]["char"] + "/data.json", "r") as file:
                old_data = json.loads(file.read())

            for j in range(len(new_data[i]["data"])):
                old_data.append(new_data[i]["data"][j])

            with open("data/synonyms/" + new_data[i]["char"] + "/data.json", "w") as file:
                file.write(json.dumps(old_data, indent=4))

