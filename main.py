from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from mainwindow import Ui_MainWindow
from searchhistory import Ui_SearchWindow
import synonyms
import search_history

# yellow #ffca3e
# blue #0098fa
# red #ff6c4c

# formatiert den Output der Synonyme
def format_output(data):
    text = ""
    if len(data["synonyms"]) > 0:
        for i in range(len(data["synonyms"])):
            text += data["synonyms"][i] + "\n"
    else:
        text = "Keine Synonyme gefunden"

    return text


# formatiert den Output des Suchverlaufs
def format_history_output(data):
    text = ""
    i = len(data["search_history"]) - 1
    while i >= 0:
        text += data["search_history"][i]["time"] + " - " + data["search_history"][i]["word"] + "\n"
        i -= 1

    return text


# suche Synonyme + Ausgabe
def search():
    # Suche
    word = ui.searchInput.text()

    if word.replace(" ", "") == "":
        ui.outputTa.setText("Gib zuerst ein Suchwort ein")
        return

    app.setOverrideCursor(Qt.WaitCursor)
    word_synonyms, search_word = synonyms.get_synonyms(word)

    # Ausgabe der Synonyme
    ui.outputTa.setText(format_output(word_synonyms))

    # falls Rechtschreibfehler gefunden werden, werden diese dann in der Suchleiste korrigiert
    if search_word != word:
        ui.searchInput.setText(search_word)

    app.restoreOverrideCursor()


# Zeigt das Suchverlaufwindow
def view_search_history():
    history = search_history.get_search_history()
    searchwindow.show()
    searchUi.outputTa.setText(format_history_output(history))


# initieren des Windows
app = QApplication([])
window = QMainWindow()
searchwindow = QMainWindow()

ui = Ui_MainWindow()
ui.setupUi(window)
searchUi = Ui_SearchWindow()
searchUi.setupUi(searchwindow)

# Events
ui.searchButton.clicked.connect(search)
ui.actionSuchverlauf.triggered.connect(view_search_history)

# ausführen
window.show()
app.exec()
