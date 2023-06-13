from PyQt5.QtWidgets import QApplication
from SynonymsWindow import AppMain


def main():
    app = QApplication([])
    window = AppMain()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()
