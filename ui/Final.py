# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Cayden\PycharmProjects\nettest\ui\Final.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1186, 791)
        self.gridLayout_2 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setEnabled(True)
        self.label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)
        self.target = QtWidgets.QLineEdit(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.target.sizePolicy().hasHeightForWidth())
        self.target.setSizePolicy(sizePolicy)
        self.target.setMaximumSize(QtCore.QSize(16777215, 25))
        self.target.setAutoFillBackground(False)
        self.target.setMaxLength(15)
        self.target.setObjectName("target")
        self.gridLayout_4.addWidget(self.target, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem, 4, 0, 1, 1)
        self.beginTest = QtWidgets.QPushButton(self.frame_2)
        self.beginTest.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.beginTest.setFont(font)
        self.beginTest.setObjectName("beginTest")
        self.gridLayout_4.addWidget(self.beginTest, 2, 0, 1, 1)
        self.outputBox = QtWidgets.QPlainTextEdit(self.frame_2)
        self.outputBox.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.outputBox.sizePolicy().hasHeightForWidth())
        self.outputBox.setSizePolicy(sizePolicy)
        self.outputBox.setMinimumSize(QtCore.QSize(0, 210))
        self.outputBox.setMaximumSize(QtCore.QSize(16777215, 210))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.outputBox.setFont(font)
        self.outputBox.setPlainText("")
        self.outputBox.setObjectName("outputBox")
        self.gridLayout_4.addWidget(self.outputBox, 3, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.frame_2, 0, 1, 1, 1)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.listWidget = QtWidgets.QListWidget(self.frame_3)
        self.listWidget.setMaximumSize(QtCore.QSize(16777215, 300))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.listWidget.setFont(font)
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.gridLayout_3.addWidget(self.listWidget, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem1, 1, 0, 1, 1)
        self.gridLayout_5.addWidget(self.frame_3, 0, 0, 2, 1)
        self.gridLayout_2.addWidget(self.frame, 0, 0, 3, 2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Target IP</span></p></body></html>"))
        self.target.setPlaceholderText(_translate("Dialog", "8.8.8.8"))
        self.beginTest.setText(_translate("Dialog", "Begin Test"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("Dialog", "Python Network Stability Test"))
        item = self.listWidget.item(1)
        item.setText(_translate("Dialog", "Speed Test"))
        item = self.listWidget.item(2)
        item.setText(_translate("Dialog", "Ping Test"))
        item = self.listWidget.item(3)
        item.setText(_translate("Dialog", "Jitter Test"))
        item = self.listWidget.item(4)
        item.setText(_translate("Dialog", "Download Speed Test"))
        item = self.listWidget.item(5)
        item.setText(_translate("Dialog", "Upload Speed Test"))
        self.listWidget.setSortingEnabled(__sortingEnabled)