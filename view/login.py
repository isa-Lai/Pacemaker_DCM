# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import  QFormLayout, QMessageBox


class Ui_Form(QtWidgets.QWidget): #change the class name here
    # add init function
    def __init__(self):
        super(Ui_Form, self).__init__()
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(560, 200)

        formbody = QFormLayout() #use form layout
        self.B_Login = QtWidgets.QPushButton(Form)
        self.B_Login.setObjectName("B_Login")
        self.B_Register = QtWidgets.QPushButton(Form)
        self.B_Register.setObjectName("B_Register")
        self.I_UserName = QtWidgets.QLineEdit(Form)
        self.I_UserName.setObjectName("I_UserName")
        self.I_Password = QtWidgets.QLineEdit(Form)
        self.I_Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.I_Password.setObjectName("I_Password")

        # add component to form
        formbody.addRow(QtWidgets.QLabel("Welcome to PaceMaker Deivce Controller & Monitor System"))
        formbody.addRow("User Name",self.I_UserName)
        formbody.addRow("Password", self.I_Password )
        formbody.addRow(self.B_Register)
        formbody.addRow(self.B_Login)
        formbody.setSpacing(20)
        self.setLayout(formbody) #set layout

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "PaceMaker Device Controller Monitor")) # change window name here
        self.B_Login.setText(_translate("Form", "Login"))
        self.B_Register.setText(_translate("Form", "Register New User"))
    
    def showMsg(self,str):
        QMessageBox.about(self, "Login Error", str)
