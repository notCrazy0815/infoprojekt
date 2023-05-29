"""
    main.py - Startet die App
"""

__author__ = "Erik Andress & Phillip Leutloff"

# Imports
from PyQt5.QtWidgets import QApplication
from SynonymsWindow import AppMain


def main():
    # Initialisiert die App
    app = QApplication([])
    window = AppMain()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()
