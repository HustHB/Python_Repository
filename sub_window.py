# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\HB\Desktop\python作业\hb2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLCDNumber,QPushButton,QWidget,QDesktopWidget
from PyQt5.Qt import QPoint, QTimer, QTime, QRect
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont,QIntValidator

class Ui_Dialog_second(object):
    def setupUi_second(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(421, 246)
        
        #输入区
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setMaxLength(6)#限制最大字符串长度
        pIntvalidator=QIntValidator(self.lineEdit)#限制输入为整数
        pIntvalidator.setRange(1,999999)#限制的范围
        self.lineEdit.setValidator(pIntvalidator)#限制输入6位以内整数
        self.lineEdit.setGeometry(QtCore.QRect(60, 20, 291, 41))
        self.lineEdit.setObjectName("lineEdit")
        
        #输入提示label
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(60, 90, 331, 51))
        self.label.setObjectName("label")
        
        #确认按钮
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(70, 160, 121, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(Dialog.close)
        
        #取消按钮
        self.pushButton_Cancel = QtWidgets.QPushButton(Dialog)
        self.pushButton_Cancel.setGeometry(QtCore.QRect(230, 160, 121, 51))
        self.pushButton_Cancel.setObjectName("pushButton_Cancel")
        self.pushButton_Cancel.clicked.connect(Dialog.close)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p>请输入一个6位以内的正整数，作为计数的秒数</p></body></html>"))
        self.pushButton.setText(_translate("Dialog", "OK"))
        self.pushButton_Cancel.setText(_translate("Dialog", "Cancel"))
        


