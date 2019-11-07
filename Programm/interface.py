# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1157, 483)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableOfProcesses = QtWidgets.QTableWidget(self.centralwidget)
        self.tableOfProcesses.setGeometry(QtCore.QRect(0, 0, 631, 391))
        self.tableOfProcesses.setColumnCount(0)
        self.tableOfProcesses.setObjectName("tableOfProcesses")
        self.tableOfProcesses.setRowCount(0)
        self.tableOfProcesses.horizontalHeader().setCascadingSectionResizes(False)
        self.printButton = QtWidgets.QPushButton(self.centralwidget)
        self.printButton.setGeometry(QtCore.QRect(0, 410, 89, 25))
        self.printButton.setObjectName("printButton")
        self.createButton = QtWidgets.QPushButton(self.centralwidget)
        self.createButton.setGeometry(QtCore.QRect(860, 190, 89, 25))
        self.createButton.setObjectName("createButton")
        self.deleteButton = QtWidgets.QPushButton(self.centralwidget)
        self.deleteButton.setGeometry(QtCore.QRect(540, 410, 89, 25))
        self.deleteButton.setObjectName("deleteButton")
        self.inputField = QtWidgets.QTextEdit(self.centralwidget)
        self.inputField.setGeometry(QtCore.QRect(670, 120, 461, 41))
        font = QtGui.QFont()
        font.setFamily("Tlwg Mono")
        font.setPointSize(12)
        self.inputField.setFont(font)
        self.inputField.setObjectName("inputField")
        self.aboutButton = QtWidgets.QPushButton(self.centralwidget)
        self.aboutButton.setGeometry(QtCore.QRect(1060, 410, 89, 25))
        self.aboutButton.setObjectName("aboutButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.printButton.setText(_translate("MainWindow", "Processes"))
        self.createButton.setText(_translate("MainWindow", "Do it!"))
        self.deleteButton.setText(_translate("MainWindow", "Delete"))
        self.aboutButton.setText(_translate("MainWindow", "About"))


