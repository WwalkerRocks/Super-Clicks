# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'super_clicks.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QTextBrowser, QWidget)
import super_main
class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.setWindowModality(Qt.ApplicationModal)
        mainWindow.resize(496, 279)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainWindow.sizePolicy().hasHeightForWidth())
        mainWindow.setSizePolicy(sizePolicy)
        mainWindow.setMinimumSize(QSize(496, 279))
        mainWindow.setMaximumSize(QSize(496, 279))
        font = QFont()
        font.setFamilies([u"Microsoft Sans Serif"])
        mainWindow.setFont(font)
        mainWindow.setMouseTracking(False)
        self.centralwidget = QWidget(mainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.mainTitle = QLabel(self.centralwidget)
        self.mainTitle.setObjectName(u"mainTitle")
        self.mainTitle.setGeometry(QRect(167, 0, 158, 33))
        font1 = QFont()
        font1.setPointSize(25)
        self.mainTitle.setFont(font1)
        self.startButton = QPushButton(self.centralwidget)
        self.startButton.setObjectName(u"startButton")
        self.startButton.setGeometry(QRect(10, 180, 191, 81))
        font2 = QFont()
        font2.setPointSize(16)
        self.startButton.setFont(font2)
        self.stopButton = QPushButton(self.centralwidget)
        self.stopButton.setObjectName(u"stopButton")
        self.stopButton.setGeometry(QRect(260, 180, 191, 81))
        font3 = QFont()
        font3.setPointSize(20)
        self.stopButton.setFont(font3)
        self.msInput = QLineEdit(self.centralwidget)
        self.msInput.setObjectName(u"msInput")
        self.msInput.setGeometry(QRect(10, 150, 114, 20))
        self.delayLabel = QLabel(self.centralwidget)
        self.delayLabel.setObjectName(u"delayLabel")
        self.delayLabel.setGeometry(QRect(50, 30, 46, 20))
        font4 = QFont()
        font4.setPointSize(15)
        self.delayLabel.setFont(font4)
        self.msLabel = QLabel(self.centralwidget)
        self.msLabel.setObjectName(u"msLabel")
        self.msLabel.setGeometry(QRect(130, 145, 71, 31))
        self.sInput = QLineEdit(self.centralwidget)
        self.sInput.setObjectName(u"sInput")
        self.sInput.setGeometry(QRect(10, 120, 114, 20))
        self.sLabel = QLabel(self.centralwidget)
        self.sLabel.setObjectName(u"sLabel")
        self.sLabel.setGeometry(QRect(130, 115, 71, 31))
        self.mInput = QLineEdit(self.centralwidget)
        self.mInput.setObjectName(u"mInput")
        self.mInput.setGeometry(QRect(10, 90, 114, 20))
        self.mLabel = QLabel(self.centralwidget)
        self.mLabel.setObjectName(u"mLabel")
        self.mLabel.setGeometry(QRect(130, 85, 71, 31))
        self.hInput = QLineEdit(self.centralwidget)
        self.hInput.setObjectName(u"hInput")
        self.hInput.setGeometry(QRect(10, 60, 114, 20))
        self.hLabel = QLabel(self.centralwidget)
        self.hLabel.setObjectName(u"hLabel")
        self.hLabel.setGeometry(QRect(130, 55, 71, 31))
        self.descLabel = QTextBrowser(self.centralwidget)
        self.descLabel.setObjectName(u"descLabel")
        self.descLabel.setGeometry(QRect(240, 50, 211, 101))
        mainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(mainWindow)

        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"Super-Clicker", None))
        self.mainTitle.setText(QCoreApplication.translate("mainWindow", u"Super Clicks", None))
        self.startButton.setText(QCoreApplication.translate("mainWindow", u"Start Autoclicker (F6)", None))
        self.stopButton.setText(QCoreApplication.translate("mainWindow", u"Stop Autoclicker", None))
        self.msInput.setText(QCoreApplication.translate("mainWindow", u"10", None))
        self.delayLabel.setText(QCoreApplication.translate("mainWindow", u"Delay", None))
        self.msLabel.setText(QCoreApplication.translate("mainWindow", u"Milliseconds", None))
        self.sInput.setText("")
        self.sInput.setPlaceholderText(QCoreApplication.translate("mainWindow", u"0", None))
        self.sLabel.setText(QCoreApplication.translate("mainWindow", u"Seconds", None))
        self.mInput.setText("")
        self.mInput.setPlaceholderText(QCoreApplication.translate("mainWindow", u"0", None))
        self.mLabel.setText(QCoreApplication.translate("mainWindow", u"Minutes", None))
        self.hInput.setText("")
        self.hInput.setPlaceholderText(QCoreApplication.translate("mainWindow", u"0", None))
        self.hLabel.setText(QCoreApplication.translate("mainWindow", u"Hours", None))
        self.descLabel.setHtml(QCoreApplication.translate("mainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Microsoft Sans Serif'; font-size:8.1pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-style:italic;\">To use this application you can either press the start button or you can use the hotkey button, which is F6. To stop the program you can press F6 again or you can force shut the program with F7.</span></p></body></html>", None))
    # retranslateUi
    
