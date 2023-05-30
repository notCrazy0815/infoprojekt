"""
    SynonymsWindow.py - das Hauptwindow der Anwendung
"""

# Imports
from PyQt5.QtGui import QIcon, QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import *
from mainwindow import Ui_MainWindow
import synonyms
from HistoryWindow import AppHistory
from SettingsWindow import AppSettings


class AppMain(QMainWindow):
    NO_INPUT_TEXT = "Bitte geben Sie ein Wort ein"
    NO_SYNONYMS_TEXT = "Keine Synonyme gefunden"

    config = None

    def __init__(self):
        # Initialisierung des Windows
        super().__init__()

        # Setzen des Icons
        self.setWindowIcon(QIcon("assets/logo.png"))

        # UI laden
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Initialisierung der anderen Windows
        self.history_window = AppHistory(self)
        self.settings_window = AppSettings(self)

        # Laden der Einstellungen
        self.config = AppSettings(self).get_settings()

        # Erstellen des Models für die Suchvorschläge
        self.ui.model = QStandardItemModel()
        completer = QCompleter(self.ui.model, self)
        self.ui.searchInput.setCompleter(completer)

        # Events
        self.ui.searchInput.textChanged.connect(self.auto_complete)
        self.ui.searchInput.returnPressed.connect(self.search)
        self.ui.searchButton.clicked.connect(self.search)
        self.ui.actionSuchverlauf.triggered.connect(self.view_search_history)
        self.ui.actionEinstellungen.triggered.connect(self.view_settings)

    # Suche Synonyme
    def search(self):
        # Laden der Einstellungen
        self.config = self.settings_window.get_settings()

        # Laden des Suchbegriffs
        word = self.ui.searchInput.text()

        # Zurücksetzen der Ausgabe
        self.ui.outputList.clear()

        # Falls kein Suchbegriff eingegeben wurde, wird eine Fehlermeldung ausgegeben
        if word.replace(" ", "") == "":
            self.ui.outputList.addItem(self.NO_INPUT_TEXT)
            return

        # Laden der Synonyme
        word_synonyms, search_word = synonyms.get_synonyms(word, self.history_window,
                                                           self.config["settings"]["auto_correct"],
                                                           self.config["settings"]["search_history"])

        # Ausgabe der Synonyme
        for i in range(len(word_synonyms)):
            self.ui.outputList.addItem(word_synonyms[i])

        # Falls keine Synonyme gefunden wurden, wird eine Fehlermeldung ausgegeben
        if len(word_synonyms) == 0:
            self.ui.outputList.addItem(self.NO_SYNONYMS_TEXT)

        self.ui.outputList.itemDoubleClicked.connect(self.copy_word)

        # falls Rechtschreibfehler gefunden wurden, werden diese dann in der Suchleiste korrigiert
        if search_word != word:
            self.ui.searchInput.setText(search_word)

    # Suchvorschläge
    def auto_complete(self):
        # Laden der Einstellungen
        self.config = self.settings_window.get_settings()

        # Wenn Suchvorschläge aktiviert sind
        if self.config["settings"]["auto_complete"] > 0:
            # Laden des Suchbegriffs
            text = self.ui.searchInput.text()

            # Falls kein Suchbegriff eingegeben wurde
            if text.replace(" ", "") == "":
                return

            # Laden der Suchvorschläge
            data = synonyms.get_auto_complete(text)

            # Zurücksetzen der Suchvorschläge
            self.ui.model.clear()

            # Ausgabe der Suchvorschläge
            words = []
            for i in range(len(data)):
                if data[i] not in words:
                    words.append(data[i])

                    self.ui.model.appendRow(QStandardItem(data[i]))

                if len(words) >= self.config["settings"]["auto_complete"]:
                    break

    # Kopieren eines Synonyms
    def copy_word(self, list_item):
        # Laden des Wortes
        word = list_item.text()

        # Falls kein Wort gefunden wurde, wird die Funktion abgebrochen
        if word == self.NO_INPUT_TEXT or word == self.NO_SYNONYMS_TEXT:
            return

        # Kopieren des Wortes
        clipboard = QApplication.clipboard()
        clipboard.setText(word)

        # Meldung, dass das Wort kopiert wurde
        self.ui.consoleLbl.setText("Wort kopiert: " + word)

    # Zeigt das Suchverlaufwindow
    def view_search_history(self):
        self.history_window.view()

    # Zeigt das Einstellungswindow
    def view_settings(self):
        self.settings_window.view()
