# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Perameter.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(575, 856)
        self.spinBox = QtWidgets.QSpinBox(Form)
        self.spinBox.setGeometry(QtCore.QRect(40, 20, 42, 22))
        self.spinBox.setMinimum(30)
        self.spinBox.setMaximum(175)
        self.spinBox.setProperty("value", 60)
        self.spinBox.setObjectName("spinBox")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(Form)
        self.doubleSpinBox.setGeometry(QtCore.QRect(40, 70, 62, 22))
        self.doubleSpinBox.setMinimum(0.05)
        self.doubleSpinBox.setMaximum(1.9)
        self.doubleSpinBox.setSingleStep(0.1)
        self.doubleSpinBox.setProperty("value", 0.4)
        self.doubleSpinBox.setObjectName("doubleSpinBox")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))