from PyQt5 import QtGui
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout, QMessageBox
from PyQt5.QtGui import QPixmap
from sys import argv
import sys
from cv2 import COLOR_BGR2RGB, cvtColor, VideoCapture
from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt, QThread
import numpy as np


class VideoThread(QThread):
    change_pixmap_signal = pyqtSignal(np.ndarray)

    def run(self):
        # capture from web cam
        cap = VideoCapture(rtsp_str)
        while True:
            ret, cv_img = cap.read()
            if ret:
                self.change_pixmap_signal.emit(cv_img)


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(arguments[3])
        self.resize(1200, 700)
        self.disply_width = 1200
        self.display_height = 1500
        # create the label that holds the image
        self.image_label = QLabel(self)
        self.image_label.resize(self.disply_width, self.display_height)
        # create a text label
        # self.textLabel = QLabel('Webcam')

        # create a vertical box layout and add the two labels
        vbox = QVBoxLayout()
        vbox.addWidget(self.image_label)
        # vbox.addWidget(self.textLabel)
        # set the vbox layout as the widgets layout
        self.setLayout(vbox)

        # create the video capture thread
        self.thread = VideoThread()
        # connect its signal to the update_image slot
        self.thread.change_pixmap_signal.connect(self.update_image)
        # start the thread
        self.thread.start()

    @pyqtSlot(np.ndarray)
    def update_image(self, cv_img):
        """Updates the image_label with a new opencv image"""
        qt_img = self.convert_cv_qt(cv_img)
        self.image_label.setPixmap(qt_img)

    def convert_cv_qt(self, cv_img):
        """Convert from an opencv image to QPixmap"""
        rgb_image = cvtColor(cv_img, COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
        p = convert_to_Qt_format.scaled(self.disply_width, self.display_height, Qt.KeepAspectRatio)
        return QPixmap.fromImage(p)


if __name__ == "__main__":
    str1 = sys.argv[1][8:]
    str2 = str1.replace("%20", " ")[:-1]
    arguments = str2.split(" ")
    if arguments[0] == "hk":
        rtsp_str = "rtsp://{}:{}@{}:554/Streaming/Channels/1".format(arguments[1], arguments[2], arguments[3])
    elif arguments[0] == "dh":
        rtsp_str = "rtsp://{}:{}@{}/cam/realmonitor?channel=1&subtype=0".format(arguments[1], arguments[2],
                                                                                arguments[3])
    app = QApplication(argv)
    a = App()
    a.show()
    sys.exit(app.exec_())
