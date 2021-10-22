"""参数说明
Usage:
  Cv2qt hk ((-u|--username) <username>) ((-w|--password) <password>) ((-i|--ip) <ip>) ((-p|port) <port>)
  Cv2qt dh ((-u|--username) <username>) ((-w|--password) <password>) ((-i|ip) <ip>)
  Cv2qt -h | --help
  Cv2qt --version

Options:
    -h --help   帮助.
    -v --version    查看版本号.
    -u --username   用户名
    -w --password   密码
    -i --ip     ip地址
    -p --port   端口号

Examples:
    Cv2qt hk -u admin -w Admin12345 -i 192.168.3.252 -p 554
    Cv2qt dh -u admin -w abc123++ -i 172.16.248.70
"""

from PyQt5 import QtGui
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout, QMessageBox
from PyQt5.QtGui import QPixmap
import sys
import cv2
from cv2 import COLOR_BGR2RGB, cvtColor, VideoCapture
from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt, QThread
import numpy as np
from docopt import docopt


rtsp_str = ""
ip=""

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
        self.setWindowTitle(ip)
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
    arguments = docopt(__doc__, version="1.0.0")
    username = arguments['<username>']
    password = arguments['<password>']
    ip = arguments['<ip>']
    if arguments['hk']:
        port = arguments['<port>']
        rtsp_str = "rtsp://{}:{}@{}:{}/Streaming/Channels/1".format(username, password, ip, port)
    elif arguments['dh']:
        rtsp_str = "rtsp://{}:{}@{}/cam/realmonitor?channel=1&subtype=0".format(username, password, ip)
    print(rtsp_str)
    app = QApplication(sys.argv)
    a = App()
    a.show()
    sys.exit(app.exec_())
