import json
import os

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow

from configwindow import Ui_MainWindow


class AppSettings(QMainWindow):
    SynonymsWindow = None

    def __init__(self, synonyms_window):
        super().__init__()
        self.setWindowIcon(QIcon("assets/logo.png"))

        self.SynonymsWindow = synonyms_window

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.correctCheck.stateChanged.connect(self.save_settings)
        self.ui.historyCheck.stateChanged.connect(self.save_settings)
        self.ui.anwendenBtn.clicked.connect(self.save_settings)

    def init_settings(self):
        settings_obj = {
            "settings": {
                "search_history": True,
                "auto_correct": True,
                "auto_complete": 3,
            }
        }

        with open("data/config.json", "w") as f:
            json.dump(settings_obj, f, indent=4)

    def save_settings(self):
        try:
            auto_complete = int(self.ui.completeInput.text())

            if auto_complete < 0:
                auto_complete = 0

            if auto_complete > 10:
                auto_complete = 10
        except ValueError:
            auto_complete = 3

        self.ui.completeInput.setText(str(auto_complete))

        settings_obj = {
            "settings": {
                "search_history": self.ui.historyCheck.isChecked(),
                "auto_correct": self.ui.correctCheck.isChecked(),
                "auto_complete": auto_complete,
            }
        }

        with open("data/config.json", "w") as f:
            json.dump(settings_obj, f, indent=4)

    def view(self):
        settings = self.get_settings()

        self.ui.correctCheck.setChecked(settings["settings"]["auto_correct"])
        self.ui.historyCheck.setChecked(settings["settings"]["search_history"])
        self.ui.completeInput.setText(str(settings["settings"]["auto_complete"]))

        self.show()

    def get_settings(self):
        if os.path.exists("data/config.json"):
            with open("data/config.json", "r") as f:
                settings = json.load(f)
        else:
            self.init_settings()
            with open("data/config.json", "r") as f:
                settings = json.load(f)

        return settings
