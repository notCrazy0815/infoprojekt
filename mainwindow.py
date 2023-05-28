# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(402, 459)
        font = QtGui.QFont()
        font.setFamily("Arial")
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(240,240,240);\n"
"color: black;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.searchButton = QtWidgets.QPushButton(self.centralwidget)
        self.searchButton.setGeometry(QtCore.QRect(280, 10, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        self.searchButton.setFont(font)
        self.searchButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.searchButton.setStyleSheet("background-color: #0098fa;\n"
"color: white;\n"
"border-radius: 3px;\n"
"cursor: pointer;")
        self.searchButton.setObjectName("searchButton")
        self.searchInput = QtWidgets.QLineEdit(self.centralwidget)
        self.searchInput.setGeometry(QtCore.QRect(10, 10, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.searchInput.setFont(font)
        self.searchInput.setStyleSheet("background-color: white;\n"
"border: none;\n"
"padding-top: 3px;\n"
"padding-bottom: 3px;\n"
"padding-left: 8px;\n"
"padding-right: 8px;\n"
"border-radius: 3px;")
        self.searchInput.setObjectName("searchInput")
        self.outputList = QtWidgets.QListWidget(self.centralwidget)
        self.outputList.setGeometry(QtCore.QRect(10, 50, 381, 341))
        self.outputList.setObjectName("outputList")
        self.consoleLbl = QtWidgets.QLabel(self.centralwidget)
        self.consoleLbl.setGeometry(QtCore.QRect(10, 400, 381, 21))
        self.consoleLbl.setObjectName("consoleLbl")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 402, 21))
        self.menubar.setObjectName("menubar")
        self.menuDatei = QtWidgets.QMenu(self.menubar)
        self.menuDatei.setObjectName("menuDatei")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSuchverlauf = QtWidgets.QAction(MainWindow)
        self.actionSuchverlauf.setObjectName("actionSuchverlauf")
        self.actionSchliessen = QtWidgets.QAction(MainWindow)
        self.actionSchliessen.setObjectName("actionSchliessen")
        self.actionEinstellungen = QtWidgets.QAction(MainWindow)
        self.actionEinstellungen.setObjectName("actionEinstellungen")
        self.menuDatei.addAction(self.actionEinstellungen)
        self.menuDatei.addAction(self.actionSuchverlauf)
        self.menuDatei.addSeparator()
        self.menuDatei.addAction(self.actionSchliessen)
        self.menubar.addAction(self.menuDatei.menuAction())

        self.retranslateUi(MainWindow)
        self.searchButton.clicked.connect(MainWindow.update) # type: ignore
        self.actionSuchverlauf.triggered.connect(MainWindow.update) # type: ignore
        self.actionSchliessen.triggered.connect(MainWindow.close) # type: ignore
        self.actionEinstellungen.triggered.connect(MainWindow.update) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Synonyms"))
        self.searchButton.setText(_translate("MainWindow", "Suchen"))
        self.searchInput.setPlaceholderText(_translate("MainWindow", "Suchwort eingeben"))
        self.consoleLbl.setText(_translate("MainWindow", "Doppelklicke ein Wort um es in die Zwischenablage zu kopieren."))
        self.menuDatei.setTitle(_translate("MainWindow", "Datei"))
        self.actionSuchverlauf.setText(_translate("MainWindow", "Suchverlauf"))
        self.actionSchliessen.setText(_translate("MainWindow", "Schliessen"))
        self.actionEinstellungen.setText(_translate("MainWindow", "Einstellungen"))
