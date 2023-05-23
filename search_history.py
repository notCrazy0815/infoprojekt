""" search_history.py - Suchverlauf erstellen, holen und neue Suchen hinzufügen """

# imports
import json
import datetime

# leert bzw erstellt den Suchverlauf
def init_search_history():
    search_history_obj = {"search_history": []}

    with open("data/search_history.json", "w") as f:
        json.dump(search_history_obj, f, indent=2)


# holt den Suchverlauf aus der Datei
def get_search_history():
    with open("data/search_history.json", "r") as f:
        return json.load(f)


# hinzufügen einer Suche
def add_search(word):
    data = get_search_history()
    time = datetime.datetime.now()

    data["search_history"].append({"word": word, "time": time.strftime('%d/%m/%Y %H:%M:%S')})

    # schreiben in die neue Datei
    with open("data/search_history.json", "w") as f:
        json.dump(data, f, indent=2)
