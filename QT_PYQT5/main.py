# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import ticker, cm
import time

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1323, 996)
        MainWindow.setMinimumSize(QtCore.QSize(120, 64))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setStyleSheet("background-image:url(:/home/sindhu/PycharmProjects/sindhu/neural_network/NEUROCAD_GUI/images/index.jpg)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gaussian_frame = QtWidgets.QFrame(self.centralwidget)
        self.gaussian_frame.setGeometry(QtCore.QRect(80, 30, 301, 451))
        self.gaussian_frame.setStyleSheet("background-image:url(:/home/sindhu/PycharmProjects/sindhu/neural_network/NEUROCAD_GUI/images/grey_image.png);background-color:rgb(255, 255, 255)")
        self.gaussian_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.gaussian_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.gaussian_frame.setObjectName("gaussian_frame")
        self.guassian = QtWidgets.QPushButton(self.gaussian_frame)
        self.guassian.setGeometry(QtCore.QRect(0, 400, 301, 51))
        self.guassian.setStyleSheet("background-image:url(:/home/sindhu/PycharmProjects/sindhu/neural_network/NEUROCAD_GUI/images/gaussian_formula.jpg)")
        self.guassian.setText("")
        self.guassian.setObjectName("guassian")
        self.gaussian_label = QtWidgets.QLabel(self.gaussian_frame)
        self.gaussian_label.setGeometry(QtCore.QRect(0, 290, 121, 17))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook L")
        font.setBold(True)
        font.setWeight(75)
        self.gaussian_label.setFont(font)
        self.gaussian_label.setStyleSheet("background-color:rgb(255, 255, 255)\n"
"")
        self.gaussian_label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.gaussian_label.setTextFormat(QtCore.Qt.AutoText)
        self.gaussian_label.setObjectName("gaussian_label")
        self.A = QtWidgets.QLabel(self.gaussian_frame)
        self.A.setGeometry(QtCore.QRect(0, 310, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook L")
        font.setBold(True)
        font.setWeight(75)
        self.A.setFont(font)
        self.A.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.A.setObjectName("A")
        self.sigmax = QtWidgets.QLabel(self.gaussian_frame)
        self.sigmax.setGeometry(QtCore.QRect(0, 340, 81, 20))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook L")
        font.setBold(True)
        font.setWeight(75)
        self.sigmax.setFont(font)
        self.sigmax.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.sigmax.setObjectName("sigmax")
        self.sigmay = QtWidgets.QLabel(self.gaussian_frame)
        self.sigmay.setGeometry(QtCore.QRect(0, 370, 81, 17))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook L")
        font.setBold(True)
        font.setWeight(75)
        self.sigmay.setFont(font)
        self.sigmay.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.sigmay.setObjectName("sigmay")
        self.y = QtWidgets.QLineEdit(self.gaussian_frame)
        self.y.setGeometry(QtCore.QRect(130, 370, 113, 27))
        self.y.setObjectName("y")
        self.x = QtWidgets.QLineEdit(self.gaussian_frame)
        self.x.setGeometry(QtCore.QRect(130, 340, 113, 27))
        self.x.setObjectName("x")
        self.A_value = QtWidgets.QLineEdit(self.gaussian_frame)
        self.A_value.setGeometry(QtCore.QRect(130, 310, 113, 27))
        self.A_value.setObjectName("A_value")
        self.gaussianWidget = gaussianWidget(self.gaussian_frame)
        self.gaussianWidget.setGeometry(QtCore.QRect(0, 0, 301, 281))
        self.gaussianWidget.setMouseTracking(True)
        self.gaussianWidget.setStyleSheet("")
        self.gaussianWidget.setObjectName("gaussianWidget")
        self.uniform_frame = QtWidgets.QFrame(self.centralwidget)
        self.uniform_frame.setGeometry(QtCore.QRect(80, 500, 301, 441))
        self.uniform_frame.setStyleSheet("background-image:url(:/home/sindhu/PycharmProjects/sindhu/neural_network/NEUROCAD_GUI/images/grey_image.png);background-color:rgb(255,255,255)")
        self.uniform_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.uniform_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.uniform_frame.setObjectName("uniform_frame")
        self.uniform_noise_formula = QtWidgets.QPushButton(self.uniform_frame)
        self.uniform_noise_formula.setGeometry(QtCore.QRect(0, 400, 301, 41))
        self.uniform_noise_formula.setStyleSheet("background-image:url(:/home/sindhu/PycharmProjects/sindhu/neural_network/NEUROCAD_GUI/images/uniform_noise_formula.jpg)")
        self.uniform_noise_formula.setText("")
        self.uniform_noise_formula.setObjectName("uniform_noise_formula")
        self.uniformCloudWidget = uniformCloudWidget(self.uniform_frame)
        self.uniformCloudWidget.setGeometry(QtCore.QRect(0, 0, 301, 271))
        self.uniformCloudWidget.setObjectName("uniformCloudWidget")
        self.uniform_clouds_label = QtWidgets.QLabel(self.uniform_frame)
        self.uniform_clouds_label.setGeometry(QtCore.QRect(0, 280, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook L")
        font.setBold(True)
        font.setWeight(75)
        self.uniform_clouds_label.setFont(font)
        self.uniform_clouds_label.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.uniform_clouds_label.setObjectName("uniform_clouds_label")
        self.Sx = QtWidgets.QLabel(self.uniform_frame)
        self.Sx.setGeometry(QtCore.QRect(0, 310, 91, 17))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook L")
        font.setBold(True)
        font.setWeight(75)
        self.Sx.setFont(font)
        self.Sx.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.Sx.setObjectName("Sx")
        self.Sy = QtWidgets.QLabel(self.uniform_frame)
        self.Sy.setGeometry(QtCore.QRect(0, 340, 91, 17))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook L")
        font.setBold(True)
        font.setWeight(75)
        self.Sy.setFont(font)
        self.Sy.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.Sy.setObjectName("Sy")
        self.Contrast = QtWidgets.QLabel(self.uniform_frame)
        self.Contrast.setGeometry(QtCore.QRect(0, 380, 91, 17))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook L")
        font.setBold(True)
        font.setWeight(75)
        self.Contrast.setFont(font)
        self.Contrast.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.Contrast.setObjectName("Contrast")
        self.x_2 = QtWidgets.QLineEdit(self.uniform_frame)
        self.x_2.setGeometry(QtCore.QRect(140, 300, 111, 31))
        self.x_2.setObjectName("x_2")
        self.y_2 = QtWidgets.QLineEdit(self.uniform_frame)
        self.y_2.setGeometry(QtCore.QRect(140, 340, 113, 31))
        self.y_2.setObjectName("y_2")
        self.c = QtWidgets.QLineEdit(self.uniform_frame)
        self.c.setGeometry(QtCore.QRect(140, 380, 113, 21))
        self.c.setObjectName("c")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.guassian.clicked.connect(self.gaussianWidget.update_graph)
        self.guassian.clicked.connect(self.update_graph)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.y, self.A_value)
        MainWindow.setTabOrder(self.A_value, self.x)
        MainWindow.setTabOrder(self.x, self.guassian)
    def update_graph(self):
        A = self.A_value.text()
        sigma_x = self.x.text()
        sigma_y= self.y.text()
        list = [int(A),int(sigma_x),int(sigma_y)]
        import json
        with open('list_gaussian_value.json', 'w') as outfile:
            json.dump(list, outfile)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.gaussian_label.setText(_translate("MainWindow", "2D GAUSSIAN"))
        self.A.setText(_translate("MainWindow", "A"))
        self.sigmax.setText(_translate("MainWindow", "SigmaX"))
        self.sigmay.setText(_translate("MainWindow", "SigmaY"))
        self.uniform_clouds_label.setText(_translate("MainWindow", "UNIFORM CLOUDS"))
        self.Sx.setText(_translate("MainWindow", "Sx"))
        self.Sy.setText(_translate("MainWindow", "Sy"))
        self.Contrast.setText(_translate("MainWindow", "Contrast"))

from gaussianwidget import gaussianWidget
from uniformcloudwidget import uniformCloudWidget
import gaussian_formula_rc
import gaussian_rc
import image_rc
import uniform_noise_formula_rc
import white_image_rc

if __name__ == "__main__":
    import sys
    while True:
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())
        time.sleep(2)

