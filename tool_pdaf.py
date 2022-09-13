## Ex 6-4. QFileDialog.

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QPushButton, QHBoxLayout, QVBoxLayout

import numpy as np
from matplotlib import pyplot as plt

class PdafToolApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        openBtn = QPushButton('&File Open', self)
        openBtn.clicked.connect(self.loadRawFile)

        hbox = QHBoxLayout()
        hbox.addWidget(openBtn)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox)

        self.setWindowTitle('PDAF Tool')
        self.setGeometry(300, 300, 800, 400)
        self.show()

    def loadRawFile(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', './')

        if fname[0]:
            with open(fname[0], "rb") as f:
                Img=np.fromfile(f,dtype='int8', sep="")
                Img=np.reshape(Img, [512,512])
                plt.imshow(Img,cmap='gray', vmin=0, vmax=1024)
                plt.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PdafToolApp()
    sys.exit(app.exec_())
