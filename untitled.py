# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(485, 430)
        Form.setMaximumSize(QtCore.QSize(485, 430))
        Form.setStyleSheet("")
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 451, 46))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(20, 100, 451, 71))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.line1 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.line1.setObjectName("line1")
        self.verticalLayout_2.addWidget(self.line1)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 190, 451, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn1 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn1.setObjectName("btn1")
        self.horizontalLayout.addWidget(self.btn1)
        self.line2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.line2.setObjectName("line2")
        self.horizontalLayout.addWidget(self.line2)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(30, 240, 341, 16))
        self.label_3.setStyleSheet("color: rgb(150, 153, 153);")
        self.label_3.setObjectName("label_3")
        self.btn2 = QtWidgets.QPushButton(Form)
        self.btn2.setGeometry(QtCore.QRect(160, 280, 151, 41))
        self.btn2.setStyleSheet("background-color: rgb(89, 94, 255);\n"
"font: 14pt \"Kaiti SC\";")
        self.btn2.setObjectName("btn2")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(170, 60, 151, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(20, 170, 451, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(Form)
        self.line_3.setGeometry(QtCore.QRect(20, 260, 451, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(30, 330, 441, 78))
        self.label_4.setObjectName("label_4")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(-1, -1, 491, 431))
        self.widget.setStyleSheet("\n"
"background-image: url(:/Users/leif/PycharmProjects/v_down/images/timg.png);\n"
"")
        self.widget.setObjectName("widget")
        self.widget.raise_()
        self.verticalLayoutWidget.raise_()
        self.verticalLayoutWidget_2.raise_()
        self.horizontalLayoutWidget.raise_()
        self.label_3.raise_()
        self.btn2.raise_()
        self.line.raise_()
        self.line_2.raise_()
        self.line_3.raise_()
        self.label_4.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "全网视频下载神器"))
        self.label_2.setText(_translate("Form", "将您要下载的视频网址粘贴到下方（必须得有哦）"))
        self.btn1.setText(_translate("Form", "请选择存储目录"))
        self.label_3.setText(_translate("Form", "备注：若您不选择目录，则自动下载在当前目录下"))
        self.btn2.setText(_translate("Form", "开始下载"))
        self.label_4.setText(_translate("Form", "小提示：下载过程中会有卡顿问题，不关注即可，下载完成后自动退出"))
import css_rc
