# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'searchhistory.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SearchWindow(object):
    def setupUi(self, SearchWindow):
        SearchWindow.setObjectName("SearchWindow")
        SearchWindow.resize(281, 411)
        SearchWindow.setStyleSheet("background-color: #eee;\n"
"color: black;")
        self.centralwidget = QtWidgets.QWidget(SearchWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.outputTa = QtWidgets.QTextEdit(self.centralwidget)
        self.outputTa.setGeometry(QtCore.QRect(10, 10, 261, 371))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.outputTa.setFont(font)
        self.outputTa.setStyleSheet("border: none;\n"
"color: black;\n"
"background-color: #fff;")
        self.outputTa.setObjectName("outputTa")
        SearchWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SearchWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 281, 21))
        self.menubar.setObjectName("menubar")
        self.menuDatei = QtWidgets.QMenu(self.menubar)
        self.menuDatei.setObjectName("menuDatei")
        SearchWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SearchWindow)
        self.statusbar.setObjectName("statusbar")
        SearchWindow.setStatusBar(self.statusbar)
        self.actionSchliessen = QtWidgets.QAction(SearchWindow)
        self.actionSchliessen.setObjectName("actionSchliessen")
        self.menuDatei.addAction(self.actionSchliessen)
        self.menubar.addAction(self.menuDatei.menuAction())

        self.retranslateUi(SearchWindow)
        self.actionSchliessen.triggered.connect(SearchWindow.close)
        QtCore.QMetaObject.connectSlotsByName(SearchWindow)

    def retranslateUi(self, SearchWindow):
        _translate = QtCore.QCoreApplication.translate
        SearchWindow.setWindowTitle(_translate("SearchWindow", "Suchverlauf"))
        self.menuDatei.setTitle(_translate("SearchWindow", "Datei"))
        self.actionSchliessen.setText(_translate("SearchWindow", "Schliessen"))
