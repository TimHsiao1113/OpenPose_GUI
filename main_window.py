"""
In this example, we demonstrate how to create simple camera viewer using Opencv3 and PyQt5

Author: Berrouba.A
Last edited: 21 Feb 2018
"""

# import system module
import sys

# import some PyQt5 modules
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer
from PyQt5.QtCore import Qt

# import Opencv module
import cv2

# import PoseModule
import pose_name as op

from queue import Queue

from ui_main_window import *

class MainWindow(QWidget):
    # class constructor
    def __init__(self):
        # call QWidget constructor
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # initial camera
        self.cap = cv2.VideoCapture(0)
        # create a timer
        self.timer = QTimer()
        self.timer.start()
        # set timer timeout callback function
        self.timer.timeout.connect(self.viewCam)


        # define clicked function of each button
        self.ui.btn_Mountain.clicked.connect(lambda: op.mountain(self.ui.text_poseName, self.ui.text_poseProb))
        self.ui.btn_Side.clicked.connect(lambda: op.mountain(self.ui.text_poseName, self.ui.text_poseProb))
        self.ui.btn_Warrior.clicked.connect(lambda: op.mountain(self.ui.text_poseName, self.ui.text_poseProb))
        self.ui.btn_Seat_Stretch_One.clicked.connect(lambda: op.mountain(self.ui.text_poseName, self.ui.text_poseProb))
        self.ui.btn_Seat_Stretch_Two.clicked.connect(lambda: op.mountain(self.ui.text_poseName, self.ui.text_poseProb))
        # set control_bt callback clicked  function
        # self.ui.control_bt.clicked.connect(self.controlTimer)

    # view camera
    def viewCam(self):
        # read image in BGR format
        ret, image = self.cap.read()
        # convert image to RGB format
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        # get image infos
        height, width, channel = image.shape
        step = channel * width
        # create QImage from image
        qImg = QImage(image.data, width, height, step, QImage.Format_RGB888)
        # show image in img_label
        self.ui.image_label.setPixmap(QPixmap.fromImage(qImg))

    # start/stop timer
    def controlTimer(self):
        # if timer is stopped
        if not self.timer.isActive():
            # create video capture
            self.cap = cv2.VideoCapture(0)
            # start timer
            self.timer.start()
            # update control_bt text
            self.ui.control_bt.setText("Stop")
        # if timer is started
        else:
            # stop timer
            self.timer.stop()
            # release video capture
            self.cap.release()
            # update control_bt text
            self.ui.control_bt.setText("Start")


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # create and show mainWindow
    mainWindow = MainWindow()
    mainWindow.show()

    sys.exit(app.exec_())