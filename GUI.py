# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(496, 279)
        mainWindow.setMinimumSize(QtCore.QSize(496, 279))
        mainWindow.setMaximumSize(QtCore.QSize(496, 279))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        mainWindow.setFont(font)
        mainWindow.setMouseTracking(False)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.mainTitle = QtWidgets.QLabel(self.centralwidget)
        self.mainTitle.setGeometry(QtCore.QRect(167, 0, 158, 33))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.mainTitle.setFont(font)
        self.mainTitle.setObjectName("mainTitle")
        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Super-Clicker"))
        self.mainTitle.setText(_translate("mainWindow", "Super Clicks"))
