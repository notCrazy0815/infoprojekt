import json
import datetime
import os.path

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow

from searchhistory import Ui_SearchWindow


class AppHistory(QMainWindow):
    NO_SEARCH_TEXT = "Noch keine Einträge"
    SynonymsWindow = None

    def __init__(self, synonyms_window):
        super().__init__()

        self.setWindowIcon(QIcon("assets/logo.png"))
        self.SynonymsWindow = synonyms_window
        self.ui = Ui_SearchWindow()
        self.ui.setupUi(self)
        self.ui.actionSuchverlauf_l_schen.triggered.connect(self.clear_search_history)

    def view(self):
        history = self.get_search_history()
        self.show()

        self.ui.outputList.clear()

        for i in range(len(history["search_history"])):
            self.ui.outputList.addItem(history["search_history"][i]["time"] + " - " + history["search_history"][i]["word"])

        if len(history["search_history"]) == 0:
            self.ui.outputList.addItem(self.NO_SEARCH_TEXT)

        self.ui.outputList.scrollToBottom()
        self.ui.outputList.itemDoubleClicked.connect(self.search_past_search)

    def search_past_search(self, list_item):
        word = list_item.text().split(" - ")

        if len(word) == 1:
            return

        word = word[1]
        self.SynonymsWindow.ui.searchInput.setText(word)
        self.SynonymsWindow.search()
        self.close()

    def init_search_history(self):
        search_history_obj = {"search_history": []}

        with open("data/search_history.json", "w") as f:
            json.dump(search_history_obj, f, indent=2)

    def clear_search_history(self):
        self.init_search_history()
        self.ui.outputList.clear()
        self.ui.outputList.addItem(self.NO_SEARCH_TEXT)

    def get_search_history(self):
        if not os.path.exists("data/search_history.json"):
            self.init_search_history()

        with open("data/search_history.json", "r") as f:
            return json.load(f)

    def add_search(self, word):
        data = self.get_search_history()
        time = datetime.datetime.now()

        data["search_history"].append({"word": word, "time": time.strftime('%d/%m/%Y %H:%M:%S')})


        with open("data/search_history.json", "w") as f:
            json.dump(data, f, indent=2)

