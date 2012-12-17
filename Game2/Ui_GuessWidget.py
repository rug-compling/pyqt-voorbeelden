# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GuessWidget.ui'
#
# Created: Mon Dec 17 11:12:13 2012
#      by: PyQt4 UI code generator 4.9.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_GuessWidget(object):
    def setupUi(self, GuessWidget):
        GuessWidget.setObjectName(_fromUtf8("GuessWidget"))
        GuessWidget.resize(400, 114)
        self.verticalLayout = QtGui.QVBoxLayout(GuessWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(GuessWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.numberLineEdit = QtGui.QLineEdit(GuessWidget)
        self.numberLineEdit.setObjectName(_fromUtf8("numberLineEdit"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.numberLineEdit)
        self.verticalLayout.addLayout(self.formLayout)
        self.resultLabel = QtGui.QLabel(GuessWidget)
        self.resultLabel.setText(_fromUtf8(""))
        self.resultLabel.setObjectName(_fromUtf8("resultLabel"))
        self.verticalLayout.addWidget(self.resultLabel)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.guessPushButton = QtGui.QPushButton(GuessWidget)
        self.guessPushButton.setObjectName(_fromUtf8("guessPushButton"))
        self.horizontalLayout.addWidget(self.guessPushButton)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(GuessWidget)
        QtCore.QMetaObject.connectSlotsByName(GuessWidget)

    def retranslateUi(self, GuessWidget):
        GuessWidget.setWindowTitle(QtGui.QApplication.translate("GuessWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("GuessWidget", "Enter a number (1-10):", None, QtGui.QApplication.UnicodeUTF8))
        self.guessPushButton.setText(QtGui.QApplication.translate("GuessWidget", "Guess", None, QtGui.QApplication.UnicodeUTF8))

