# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'App.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import cv2 
import numpy as np
import os
import time
from windowcapture import WindowCapture
import win32api, win32gui, win32con
from PIL.ImageQt import ImageQt

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(707, 383)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setMovable(False)
        self.tabWidget.setObjectName("tabWidget")
        self.About = QtWidgets.QWidget()
        self.About.setObjectName("About")
        self.label = QtWidgets.QLabel(self.About)
        self.label.setGeometry(QtCore.QRect(10, 10, 266, 33))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.tabWidget.addTab(self.About, "")
        self.Build = QtWidgets.QWidget()
        self.Build.setObjectName("Build")
        self.gridLayout = QtWidgets.QGridLayout(self.Build)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox_2 = QtWidgets.QGroupBox(self.Build)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_4.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_4.addWidget(self.pushButton_4, 1, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 0, 1, 1, 1, QtCore.Qt.AlignBottom)
        self.verticalLayout_2.addWidget(self.groupBox_4)
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_2.addWidget(self.groupBox_3)
        self.gridLayout.addWidget(self.groupBox_2, 0, 1, 1, 1)
        self.tabWidget.addTab(self.Build, "")
        self.Test = QtWidgets.QWidget()
        self.Test.setObjectName("Test")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.Test)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.test_Label = QtWidgets.QLabel(self.Test)
        self.test_Label.setFrameShape(QtWidgets.QFrame.Panel)
        self.test_Label.setMidLineWidth(0)
        self.test_Label.setText("")
        self.test_Label.setPixmap(QtGui.QPixmap("../../template.png"))
        self.test_Label.setScaledContents(True)
        self.test_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.test_Label.setObjectName("test_Label")
        self.gridLayout_2.addWidget(self.test_Label, 1, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.Test)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 50))
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.test_Stop_Button = QtWidgets.QPushButton(self.groupBox)
        self.test_Stop_Button.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.test_Stop_Button.setFont(font)
        self.test_Stop_Button.setObjectName("test_Stop_Button")
        self.gridLayout_5.addWidget(self.test_Stop_Button, 0, 1, 1, 1)
        self.test_Start_Button = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.test_Start_Button.setFont(font)
        self.test_Start_Button.setObjectName("test_Start_Button")
        self.gridLayout_5.addWidget(self.test_Start_Button, 0, 0, 1, 1)
        self.test_lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.test_lineEdit.setObjectName("test_lineEdit")
        self.gridLayout_5.addWidget(self.test_lineEdit, 0, 2, 1, 1)
        self.test_Browse_Button = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.test_Browse_Button.setFont(font)
        self.test_Browse_Button.setObjectName("test_Browse_Button")
        self.gridLayout_5.addWidget(self.test_Browse_Button, 0, 3, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 2, 0, 1, 1)
        self.tabWidget.addTab(self.Test, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 707, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
#My code
        self.test_Start_Button.clicked.connect(self.startTest)
    
    def startTest(self):
        self.test = True
        wincap = WindowCapture('Aeldra')
        Model = cv2.CascadeClassifier("Models/cascade.xml")
        while self.test:
            screen = wincap.get_screenshot()
            model = Model.detectMultiScale(screen, 1.05, 3)
            self.test_Label.setText(model)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Haar Cascade Creator!"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.About), _translate("MainWindow", "About"))
        self.groupBox_4.setTitle(_translate("MainWindow", "GroupBox"))
        self.pushButton_4.setText(_translate("MainWindow", "Browse"))
        self.label_3.setText(_translate("MainWindow", "Model Folder"))
        self.groupBox_3.setTitle(_translate("MainWindow", "GroupBox"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Build), _translate("MainWindow", "Build"))
        self.groupBox.setTitle(_translate("MainWindow", "Control Panel"))
        self.test_Stop_Button.setText(_translate("MainWindow", "Stop"))
        self.test_Start_Button.setText(_translate("MainWindow", "Start"))
        self.test_Browse_Button.setText(_translate("MainWindow", "Browse"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Test), _translate("MainWindow", "Test"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
