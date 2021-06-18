"""
In this example, we demonstrate how to create simple camera viewer using Opencv3 and PyQt5

Author: Berrouba.A
Last edited: 21 Feb 2018
"""

# import system module
import sys

# import some PyQt5 modules
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout
from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt, QThread, QTimer
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui

import sys

import numpy as np

# import Opencv module
import cv2

# import PoseModule
import pose_name 

from queue import Queue

from ui_main_window import *


# Video
class VideoThread(QThread):
    change_pixmap_signal = pyqtSignal(np.ndarray)

    def __init__(self, frame_queue):
        super().__init__()
        self._run_flag = True
        self.frame_queue = frame_queue

    def run(self):
        # capture from web cam
        cap = cv2.VideoCapture(0)
        while self._run_flag:
            ret, cv_img = cap.read()
            if ret:
                self.change_pixmap_signal.emit(cv_img)
                self.frame_queue.put(cv_img)
        # shut down capture system
        cap.release()

    def stop(self):
        """Sets run flag to False and waits for thread to finish"""
        self._run_flag = False
        self.wait()



class MainWindow(QWidget):
    # class constructor
    def __init__(self):
        # call QWidget constructor
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # Image Initial
        self.cv_img = None
        frame_queue = Queue(maxsize=1)

        # create the video capture thread
        self.thread = VideoThread(frame_queue)
        # connect its signal to the update_image slot
        self.thread.change_pixmap_signal.connect(lambda:self.update_image(frame_queue))
        # start the thread
        self.thread.start()


        # define clicked function of each button
        op = pose_name.OpenPose(self.ui.text_poseName, self.ui.text_poseProb)
        self.ui.btn_Mountain.clicked.connect(lambda: op.mountain(self.cv_img))
        self.ui.btn_Side.clicked.connect(lambda: op.mountain(self.cv_img))
        self.ui.btn_Warrior.clicked.connect(lambda: op.mountain(self.cv_img))
        self.ui.btn_Seat_Stretch_One.clicked.connect(lambda: op.mountain(self.cv_img))
        self.ui.btn_Seat_Stretch_Two.clicked.connect(lambda: op.mountain(self.cv_img))

        # Check get image or not, 
        # True: enable button 
        # False: disable button
        self.checkCamera()


        
    def checkCamera(self):
        if(self.cv_img is None):
            self.ui.btn_Mountain.setEnabled(False)
            self.ui.btn_Side.setEnabled(False)
            self.ui.btn_Warrior.setEnabled(False)
            self.ui.btn_Seat_Stretch_One.setEnabled(False)
            self.ui.btn_Seat_Stretch_Two.setEnabled(False)

        else:
            self.ui.btn_Mountain.setEnabled(True)
            self.ui.btn_Side.setEnabled(True)
            self.ui.btn_Warrior.setEnabled(True)
            self.ui.btn_Seat_Stretch_One.setEnabled(True)
            self.ui.btn_Seat_Stretch_Two.setEnabled(True)



    def closeEvent(self, event):
        self.thread.stop()
        event.accept()

    @pyqtSlot(np.ndarray)
    def update_image(self, frame_queue):
        """Updates the image_label with a new opencv image"""
        self.cv_img = frame_queue.get()
        self.qt_img = self.convert_cv_qt(self.cv_img)
        self.ui.image_label.setPixmap(self.qt_img)
    
    def convert_cv_qt(self, cv_img):
        """Convert from an opencv image to QPixmap"""
        rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        # convert_to_Qt_format = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
        # p = convert_to_Qt_format.scaled(self.disply_width, self.display_height, Qt.KeepAspectRatio)
        qImg = QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
        return QPixmap.fromImage(qImg)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # create and show mainWindow
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())