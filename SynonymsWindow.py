from PyQt5.QtGui import QIcon, QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import *
from mainwindow import Ui_MainWindow
import synonyms
from HistoryWindow import AppHistory


# yellow #ffca3e
# blue #0098fa
# red #ff6c4c

# black #000000
# grey #1c1c1e
# white #dcdcdc

class AppMain(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon("assets/logo.png"))

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.model = QStandardItemModel()
        completer = QCompleter(self.ui.model, self)
        self.ui.searchInput.setCompleter(completer)

        self.ui.searchInput.textChanged.connect(self.auto_complete)
        self.ui.searchInput.returnPressed.connect(self.search)
        self.ui.searchButton.clicked.connect(self.search)
        self.ui.actionSuchverlauf.triggered.connect(self.view_search_history)

        self.history_window = AppHistory(self)

        # self.ui.model.appendRow(QStandardItem(entryItem))

    def search(self):
        # Suche
        word = self.ui.searchInput.text()

        if word.replace(" ", "") == "":
            self.ui.outputTa.setText("Gib zuerst ein Suchwort ein")
            return

        word_synonyms, search_word = synonyms.get_synonyms(word, self.history_window)

        # Ausgabe der Synonyme
        self.ui.outputTa.setText(self.format_output(word_synonyms, word))

        # falls Rechtschreibfehler gefunden werden, werden diese dann in der Suchleiste korrigiert
        if search_word != word:
            self.ui.searchInput.setText(search_word)


    def auto_complete(self):
        text = self.ui.searchInput.text()

        if text.replace(" ", "") == "":
            return

        data = synonyms.get_auto_complete(text)

        self.ui.model.clear()

        words = []
        for i in range(len(data)):
            if data[i] not in words:
                words.append(data[i])
                self.ui.model.appendRow(QStandardItem(data[i]))

            if len(words) >= 3:
                break


    # Zeigt das Suchverlaufwindow
    def view_search_history(self):
        self.history_window.view()

    # formatiert den Output der Synonyme
    def format_output(self, data, word):
        text = ""
        if len(data) > 0:
            for i in range(len(data)):
                text += data[i] + "\n"
        else:
            text = "Keine Synonyme gefunden"

        return text
