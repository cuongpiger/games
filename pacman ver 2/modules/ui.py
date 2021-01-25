# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(811, 355)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.box_maze = QLabel(self.centralwidget)
        self.box_maze.setObjectName(u"box_maze")
        self.box_maze.setGeometry(QRect(330, 20, 461, 291))
        self.box_maze.setPixmap(QPixmap(u"C:/Users/cuong/Google Drive/blackpink-rose-chia-se-suy-nghi-ve-giong-hat-cua-chinh-ban-than-1-1603332638.jpg"))
        self.box_maze.setScaledContents(True)
        self.cb_mazes = QComboBox(self.centralwidget)
        self.cb_mazes.setObjectName(u"cb_mazes")
        self.cb_mazes.setGeometry(QRect(110, 20, 191, 22))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 20, 47, 21))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 70, 47, 21))
        self.cb_algorithms = QComboBox(self.centralwidget)
        self.cb_algorithms.setObjectName(u"cb_algorithms")
        self.cb_algorithms.setGeometry(QRect(110, 70, 191, 22))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 120, 47, 21))
        self.cb_heuristic = QComboBox(self.centralwidget)
        self.cb_heuristic.setObjectName(u"cb_heuristic")
        self.cb_heuristic.setGeometry(QRect(110, 120, 191, 22))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 170, 71, 21))
        self.sld_feed_density = QSlider(self.centralwidget)
        self.sld_feed_density.setObjectName(u"sld_feed_density")
        self.sld_feed_density.setGeometry(QRect(110, 170, 141, 22))
        self.sld_feed_density.setOrientation(Qt.Horizontal)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 220, 91, 21))
        self.sld_pacman_speed = QSlider(self.centralwidget)
        self.sld_pacman_speed.setObjectName(u"sld_pacman_speed")
        self.sld_pacman_speed.setGeometry(QRect(110, 220, 141, 22))
        self.sld_pacman_speed.setOrientation(Qt.Horizontal)
        self.btn_run = QPushButton(self.centralwidget)
        self.btn_run.setObjectName(u"btn_run")
        self.btn_run.setGeometry(QRect(100, 270, 131, 41))
        self.sb_feed_density = QSpinBox(self.centralwidget)
        self.sb_feed_density.setObjectName(u"sb_feed_density")
        self.sb_feed_density.setGeometry(QRect(260, 170, 42, 22))
        self.sb_pacman_speed = QSpinBox(self.centralwidget)
        self.sb_pacman_speed.setObjectName(u"sb_pacman_speed")
        self.sb_pacman_speed.setGeometry(QRect(260, 220, 42, 22))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 811, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.box_maze.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Maze:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Algorithm:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Heuristic:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Feed density:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Pacman's speed:", None))
        self.btn_run.setText(QCoreApplication.translate("MainWindow", u"RUN", None))
    # retranslateUi

