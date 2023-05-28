from PyQt5.QtGui import QIcon, QStandardItemModel, QStandardItem, QFont
from PyQt5.QtWidgets import *
from mainwindow import Ui_MainWindow
import synonyms
from HistoryWindow import AppHistory

class AppMain(QMainWindow):
    NO_INPUT_TEXT = "Bitte geben Sie ein Wort ein"
    NO_SYNONYMS_TEXT = "Keine Synonyme gefunden"

    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon("assets/logo.png"))

        font = QFont()
        font.setPointSize(12)
        self.setFont(font)

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

        self.ui.outputList.clear()

        if word.replace(" ", "") == "":
            self.ui.outputList.addItem(self.NO_INPUT_TEXT)
            return

        word_synonyms, search_word = synonyms.get_synonyms(word, self.history_window)

        # Ausgabe der Synonyme
        for i in range(len(word_synonyms)):
            self.ui.outputList.addItem(word_synonyms[i])

        if len(word_synonyms) == 0:
            self.ui.outputList.addItem(self.NO_SYNONYMS_TEXT)

        self.ui.outputList.itemDoubleClicked.connect(self.copy_word)

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

    def copy_word(self, list_item):
        word = list_item.text()

        if word == self.NO_INPUT_TEXT or word == self.NO_SYNONYMS_TEXT:
            return

        clipboard = QApplication.clipboard()
        clipboard.setText(word)
        self.ui.consoleLbl.setText("Wort kopiert: " + word)

    # Zeigt das Suchverlaufwindow
    def view_search_history(self):
        self.history_window.view()

