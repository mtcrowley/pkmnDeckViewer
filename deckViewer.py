from PyQt5.QtWidgets import (QMessageBox,QApplication, QWidget, QToolTip, QPushButton,
                             QDesktopWidget, QMainWindow, QAction, qApp, QToolBar, QVBoxLayout,
                             QComboBox,QLabel,QLineEdit,QGridLayout,QMenuBar,QMenu,QStatusBar,
                             QTextEdit,QDialog,QFrame,QProgressBar
                             )
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QIcon,QFont,QPixmap,QPalette
from PyQt5.QtCore import QCoreApplication, Qt,QBasicTimer, QPoint

import sys

from deckList import Deck

class cssden(QMainWindow):
    def __init__(self, deckPath = "Z:/Python/deckLists/main.txt"):
        super().__init__()


        self.mwidget = QMainWindow(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)

        #label
        self.thumbs = []

        totalHeight = 5

        deck = Deck(deckPath)

        for path in deck.getPaths("img/crop/"):

            self.thumbs.append(self.makeImg(path))
            self.thumbs[-1].move(int(self.thumbs[0].width()*2.5),totalHeight)
            totalHeight += self.thumbs[-1].height()

        self.lbls = []

        y = 5

        for item in deck.deckList:

            self.lbl = QLabel(self)
            self.lbl.setStyleSheet("background-color: rgb(0,0,0)")
            self.lbl.setGeometry(5,y,int(self.thumbs[0].width()*3),self.thumbs[-1].height())
            self.lbl.lower()

            self.lbl = QLabel(self)
            self.lbl.setText( str(item.count) + " " + item.card.name)
            self.lbl.setStyleSheet("background: transparent;"
                                   "color: rgb(255,255,255);"
                                   "font: bold 18pt 'ModMatrix';")
            self.lbl.setGeometry(4,y,int(self.thumbs[0].width()*3),self.thumbs[-1].height())
            y += self.thumbs[-1].height() + 1

        #size
        self.setFixedSize(int(self.thumbs[0].width()*3.5)+5, totalHeight+5)
        self.center()

        self.oldPos = self.pos()

        self.show()


    def makeImg(self, path):

        lbl = QLabel(self)
        lbl.setStyleSheet("border: 1px solid silver;")
        pixmap = QPixmap(path)
        lbl.setPixmap(pixmap)
        lbl.setScaledContents(True)
        lbl.resize(int(pixmap.width()*3/8.0),int(pixmap.height()*3/8.0))
        return lbl

    #center
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint (event.globalPos() - self.oldPos)
        #print(delta)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

app = QApplication(sys.argv)
app.setStyleSheet("QMainWindow{background-color: silver;border: 1px solid black}")

ex = cssden()
sys.exit(app.exec_())