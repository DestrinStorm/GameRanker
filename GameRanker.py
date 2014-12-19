# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Dropbox\Coding\GameRanker\Gameranker.ui'
#
# Created: Fri Dec 19 17:02:43 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_GameRanker(object):
    def setupUi(self, GameRanker):
        GameRanker.setObjectName(_fromUtf8("GameRanker"))
        GameRanker.resize(1194, 900)
        self.centralwidget = QtGui.QWidget(GameRanker)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.btnLoadData = QtGui.QPushButton(self.centralwidget)
        self.btnLoadData.setGeometry(QtCore.QRect(220, 40, 151, 23))
        self.btnLoadData.setObjectName(_fromUtf8("btnLoadData"))
        self.btnGame1 = QtGui.QPushButton(self.centralwidget)
        self.btnGame1.setGeometry(QtCore.QRect(500, 70, 191, 111))
        self.btnGame1.setObjectName(_fromUtf8("btnGame1"))
        self.leUsername = QtGui.QLineEdit(self.centralwidget)
        self.leUsername.setGeometry(QtCore.QRect(100, 10, 113, 20))
        self.leUsername.setText(_fromUtf8(""))
        self.leUsername.setObjectName(_fromUtf8("leUsername"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 81, 20))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 40, 91, 16))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.leMinRating = QtGui.QLineEdit(self.centralwidget)
        self.leMinRating.setGeometry(QtCore.QRect(100, 40, 113, 20))
        self.leMinRating.setObjectName(_fromUtf8("leMinRating"))
        self.btnGame2 = QtGui.QPushButton(self.centralwidget)
        self.btnGame2.setGeometry(QtCore.QRect(500, 350, 191, 111))
        self.btnGame2.setObjectName(_fromUtf8("btnGame2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(550, 260, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lcdCollection = QtGui.QLCDNumber(self.centralwidget)
        self.lcdCollection.setGeometry(QtCore.QRect(500, 30, 191, 31))
        self.lcdCollection.setObjectName(_fromUtf8("lcdCollection"))
        self.taCollection = QtGui.QTableWidget(self.centralwidget)
        self.taCollection.setGeometry(QtCore.QRect(0, 70, 491, 830))
        self.taCollection.setColumnCount(4)
        self.taCollection.setObjectName(_fromUtf8("taCollection"))
        self.taCollection.setRowCount(0)
        self.taCollection.verticalHeader().setVisible(False)
        self.taTop = QtGui.QTableWidget(self.centralwidget)
        self.taTop.setGeometry(QtCore.QRect(700, 70, 491, 831))
        self.taTop.setColumnCount(2)
        self.taTop.setObjectName(_fromUtf8("taTop"))
        self.taTop.setRowCount(0)
        self.txtGame1 = QtGui.QPlainTextEdit(self.centralwidget)
        self.txtGame1.setGeometry(QtCore.QRect(500, 190, 191, 51))
        self.txtGame1.setPlainText(_fromUtf8(""))
        self.txtGame1.setObjectName(_fromUtf8("txtGame1"))
        self.txtGame2 = QtGui.QPlainTextEdit(self.centralwidget)
        self.txtGame2.setGeometry(QtCore.QRect(500, 290, 191, 51))
        self.txtGame2.setPlainText(_fromUtf8(""))
        self.txtGame2.setObjectName(_fromUtf8("txtGame2"))
        GameRanker.setCentralWidget(self.centralwidget)

        self.retranslateUi(GameRanker)
        QtCore.QMetaObject.connectSlotsByName(GameRanker)
        GameRanker.setTabOrder(self.leUsername, self.leMinRating)
        GameRanker.setTabOrder(self.leMinRating, self.btnLoadData)
        GameRanker.setTabOrder(self.btnLoadData, self.btnGame1)
        GameRanker.setTabOrder(self.btnGame1, self.btnGame2)

    def retranslateUi(self, GameRanker):
        GameRanker.setWindowTitle(_translate("GameRanker", "MainWindow", None))
        self.btnLoadData.setText(_translate("GameRanker", "Load Data", None))
        self.btnGame1.setText(_translate("GameRanker", "Game 1", None))
        self.label.setText(_translate("GameRanker", "BGG Username:", None))
        self.label_2.setText(_translate("GameRanker", "Minimum Rating:", None))
        self.btnGame2.setText(_translate("GameRanker", "Game2", None))
        self.label_3.setText(_translate("GameRanker", "OR", None))

