# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/searchhistory.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SearchWindow(object):
    def setupUi(self, SearchWindow):
        SearchWindow.setObjectName("SearchWindow")
        SearchWindow.resize(281, 417)
        SearchWindow.setStyleSheet("background-color: #eee;\n"
"color: black;")
        self.centralwidget = QtWidgets.QWidget(SearchWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.outputList = QtWidgets.QListWidget(self.centralwidget)
        self.outputList.setGeometry(QtCore.QRect(10, 0, 256, 371))
        self.outputList.setObjectName("outputList")
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
        self.actionSuchverlauf_l_schen = QtWidgets.QAction(SearchWindow)
        self.actionSuchverlauf_l_schen.setObjectName("actionSuchverlauf_l_schen")
        self.menuDatei.addAction(self.actionSuchverlauf_l_schen)
        self.menuDatei.addSeparator()
        self.menuDatei.addAction(self.actionSchliessen)
        self.menubar.addAction(self.menuDatei.menuAction())

        self.retranslateUi(SearchWindow)
        self.actionSchliessen.triggered.connect(SearchWindow.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(SearchWindow)

    def retranslateUi(self, SearchWindow):
        _translate = QtCore.QCoreApplication.translate
        SearchWindow.setWindowTitle(_translate("SearchWindow", "Suchverlauf"))
        self.menuDatei.setTitle(_translate("SearchWindow", "Datei"))
        self.actionSchliessen.setText(_translate("SearchWindow", "Schliessen"))
        self.actionSuchverlauf_l_schen.setText(_translate("SearchWindow", "Suchverlauf löschen"))
