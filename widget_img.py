#!/usr/bin/env/ python
# -*- coding: utf-8 -*-

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import Image
import ImageQt
import ImageEnhance
import time

class MainWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.scene = QGraphicsScene()
        self.view = QGraphicsView(self.scene)
        self.button = QPushButton("Do test")

        
        layout = QVBoxLayout()
        layout.addWidget(self.button)
        layout.addWidget(self.view)
        self.setLayout(layout)
        img = Image.open('image.png')
        enhancer = ImageEnhance.Brightness(img)
        self.display_image(img)


    def do_test(self):
       for i in range(1, 2):
            img = enhancer.enhance(i)
            QCoreApplication.processEvents()  # let Qt do his work
            time.sleep(0.5)

    def display_image(self, img):
        self.scene.clear()
        w, h = img.size
        self.imgQ = ImageQt.ImageQt(img)  # we need to hold reference to imgQ, or it will crash
        pixMap = QPixmap.fromImage(self.imgQ)
        self.scene.addPixmap(pixMap)
        self.view.fitInView(QRectF(0, 0, w, h), Qt.KeepAspectRatio)
        self.scene.update()

