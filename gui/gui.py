import sys
from functools import partial
import cv2
import numpy as np

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *

import rospy
from std_msgs.msg import String
from sensor_msgs.msg import CompressedImage, NavSatFix


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        # initialize
        self.window_w = 1000
        self.window_h = 500

        # ros pub and subs
        rospy.Subscriber('/usb_camera_0/image_raw/compressed', CompressedImage, self._usb_camera_callback_0)
        rospy.Subscriber('/usb_camera_1/image_raw/compressed', CompressedImage, self._usb_camera_callback_1)
        rospy.Subscriber('/fix', NavSatFix, self._gps_callback)

        # create window
        self.setWindowTitle('Robotics at Iowa GUI')
        self.setFixedSize(self.window_w, self.window_h)

        # create general layout
        self.main_layout = QVBoxLayout()
        self.top_layout = QHBoxLayout()
        self.bottom_layout = QHBoxLayout()

        self.main_layout.addLayout(self.top_layout)
        self.main_layout.addLayout(self.bottom_layout)

        self.central_widget = QWidget()
        self.central_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.central_widget)

        # create gui within layout
        self._create_video_feeds()
        self._create_gps_labels()

    def _create_video_feeds(self):
        # create two video feeds
        self.vid1 = QLabel(self)
        self.vid2 = QLabel(self)

        self.top_layout.addWidget(self.vid1)
        self.top_layout.addWidget(self.vid2)

    def _create_gps_labels(self):
        self.lat_label = QLabel(self)
        self.long_label = QLabel(self)


        self.top_layout.addWidget(QLabel("Latitude: ", self))
        self.bottom_layout.addWidget(self.lat_label)
        self.top_layout.addWidget(QLabel("Longitude: ", self))
        self.bottom_layout.addWidget(self.long_label)

    def _usb_camera_callback_0(self, data):
        pixmap = self._compressed_image_to_pixmap(data.data, width_scale=self.window_w//2)
        self.vid1.setPixmap(pixmap)

    def _usb_camera_callback_1(self, data):
        pixmap = self._compressed_image_to_pixmap(data.data, width_scale=self.window_w//2)
        self.vid2.setPixmap(pixmap)

    def _compressed_image_to_pixmap(self, compressed_img, width_scale):
        # convert image: compressed string --> np --> cv2 --> pyqt
        np_img = np.fromstring(compressed_img, np.uint8)
        bgr_img = cv2.imdecode(np_img, cv2.IMREAD_COLOR)
        rgb_img = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2RGB)

        h, w, ch = rgb_img.shape
        bytes_per_line = ch * w
        qt_img = QImage(rgb_img.data, w, h, bytes_per_line, QImage.Format_RGB888)
        qt_img = qt_img.scaledToWidth(width_scale)

        pixmap = QPixmap.fromImage(qt_img)

        return pixmap

    def _gps_callback(self, data):
        self.lat_label.setText(str(data.latitude))
        self.long_label.setText(str(data.longitude))


if __name__ == '__main__':
    try:
        # initialize ros node
        rospy.init_node('gui')

        # create gui
        app = QApplication(sys.argv)
        win = Window()
        win.show()

        sys.exit(app.exec_())
    except rospy.ROSInterruptException:
        pass