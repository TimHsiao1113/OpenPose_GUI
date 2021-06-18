# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1102, 742)
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout.addItem(spacerItem, 2, 2, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout.addItem(spacerItem1, 6, 2, 1, 2)
        self.btn_Exit = QtWidgets.QPushButton(Form)
        self.btn_Exit.setMinimumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.btn_Exit.setFont(font)
        self.btn_Exit.setObjectName("btn_Exit")
        self.gridLayout.addWidget(self.btn_Exit, 7, 2, 1, 2)
        self.btn_Mountain = QtWidgets.QPushButton(Form)
        self.btn_Mountain.setMinimumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.btn_Mountain.setFont(font)
        self.btn_Mountain.setObjectName("btn_Mountain")
        self.gridLayout.addWidget(self.btn_Mountain, 3, 0, 1, 2)
        self.cap_img = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.cap_img.setFont(font)
        self.cap_img.setAlignment(QtCore.Qt.AlignCenter)
        self.cap_img.setObjectName("cap_img")
        self.gridLayout.addWidget(self.cap_img, 0, 2, 1, 2)
        self.btn_Seat_Stretch_Two = QtWidgets.QPushButton(Form)
        self.btn_Seat_Stretch_Two.setMinimumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.btn_Seat_Stretch_Two.setFont(font)
        self.btn_Seat_Stretch_Two.setObjectName("btn_Seat_Stretch_Two")
        self.gridLayout.addWidget(self.btn_Seat_Stretch_Two, 7, 0, 1, 2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout.addItem(spacerItem2, 6, 0, 1, 2)
        self.btn_Side = QtWidgets.QPushButton(Form)
        self.btn_Side.setMinimumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.btn_Side.setFont(font)
        self.btn_Side.setObjectName("btn_Side")
        self.gridLayout.addWidget(self.btn_Side, 3, 2, 1, 2)
        self.btn_Warrior = QtWidgets.QPushButton(Form)
        self.btn_Warrior.setMinimumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.btn_Warrior.setFont(font)
        self.btn_Warrior.setObjectName("btn_Warrior")
        self.gridLayout.addWidget(self.btn_Warrior, 5, 0, 1, 2)
        self.btn_Seat_Stretch_One = QtWidgets.QPushButton(Form)
        self.btn_Seat_Stretch_One.setMinimumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.btn_Seat_Stretch_One.setFont(font)
        self.btn_Seat_Stretch_One.setObjectName("btn_Seat_Stretch_One")
        self.gridLayout.addWidget(self.btn_Seat_Stretch_One, 5, 2, 1, 2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout.addItem(spacerItem3, 2, 0, 1, 2)
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout.addItem(spacerItem4, 4, 0, 1, 2)
        self.image_label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.image_label.setFont(font)
        self.image_label.setAlignment(QtCore.Qt.AlignCenter)
        self.image_label.setObjectName("image_label")
        self.gridLayout.addWidget(self.image_label, 0, 0, 1, 2)
        spacerItem5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout.addItem(spacerItem5, 4, 2, 1, 2)
        self.idx_poseName = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.idx_poseName.sizePolicy().hasHeightForWidth())
        self.idx_poseName.setSizePolicy(sizePolicy)
        self.idx_poseName.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.idx_poseName.setFont(font)
        self.idx_poseName.setAlignment(QtCore.Qt.AlignCenter)
        self.idx_poseName.setObjectName("idx_poseName")
        self.gridLayout.addWidget(self.idx_poseName, 1, 0, 1, 1)
        self.text_poseName = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setUnderline(True)
        self.text_poseName.setFont(font)
        self.text_poseName.setAlignment(QtCore.Qt.AlignCenter)
        self.text_poseName.setObjectName("text_poseName")
        self.gridLayout.addWidget(self.text_poseName, 1, 1, 1, 1)
        self.idx_prob = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.idx_prob.sizePolicy().hasHeightForWidth())
        self.idx_prob.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.idx_prob.setFont(font)
        self.idx_prob.setAlignment(QtCore.Qt.AlignCenter)
        self.idx_prob.setObjectName("idx_prob")
        self.gridLayout.addWidget(self.idx_prob, 1, 2, 1, 1)
        self.text_poseProb = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setUnderline(True)
        self.text_poseProb.setFont(font)
        self.text_poseProb.setAlignment(QtCore.Qt.AlignCenter)
        self.text_poseProb.setObjectName("text_poseProb")
        self.gridLayout.addWidget(self.text_poseProb, 1, 3, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(Form)
        self.btn_Exit.clicked.connect(Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "OpenPose"))
        self.btn_Exit.setText(_translate("Form", "Exit"))
        self.btn_Mountain.setText(_translate("Form", "Mountain Pose Forward Bend"))
        self.cap_img.setText(_translate("Form", "Capture Image"))
        self.btn_Seat_Stretch_Two.setText(_translate("Form", "Seated Stretch Pose Two"))
        self.btn_Side.setText(_translate("Form", "Side Forward Bend"))
        self.btn_Warrior.setText(_translate("Form", "Warrior Pose"))
        self.btn_Seat_Stretch_One.setText(_translate("Form", "Seated Stretch Pose One"))
        self.image_label.setText(_translate("Form", "Camera"))
        self.idx_poseName.setText(_translate("Form", "Pose Name :"))
        self.text_poseName.setText(_translate("Form", "Actual Pose Name"))
        self.idx_prob.setText(_translate("Form", "Probability :"))
        self.text_poseProb.setText(_translate("Form", "Prob"))
