## Ex 6-4. QFileDialog.

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QPushButton, QHBoxLayout, QVBoxLayout, QWidget

import matplotlib
matplotlib.use('Qt5Agg')
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

class ImgCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        self.axes.axis('off')
        #plt.savefig('image.png', bbox_inches='tight',pad_inches = 0)
        super(ImgCanvas, self).__init__(fig)

class PdafToolApp(QMainWindow):

    def __init__(self):
        super().__init__()
        # Acquire default dots per inch value of matplotlib
        dpi = matplotlib.rcParams['figure.dpi']
        print(dpi)
        self.initUI()

        self.setWindowTitle('PDAF Tool')
        self.setGeometry(300, 300, 800, 400)
        self.show()

    def initUI(self):
        self.rawCanvas = ImgCanvas(self, width=5, height=4, dpi=300)

        openBtn = QPushButton('&File Open', self)
        openBtn.clicked.connect(self.loadRawFile)

        hbox = QHBoxLayout()
        hbox.addWidget(openBtn)
        hbox.addWidget(self.rawCanvas)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox)

        widget = QWidget()
        widget.setLayout(vbox)

        self.setCentralWidget(widget)

    def loadRawFile(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', './')

        if fname[0]:
            with open(fname[0], "rb") as f:
                Img=np.fromfile(f,dtype='int8', sep="")
                Img=np.reshape(Img, [512,512])
                #plt.imshow(Img, cmap='gray', vmin=0, vmax=1024)
                #plt.show()
                self.rawCanvas.axes.imshow(Img, cmap='gray', vmin=0, vmax=1024)

        #self.sc.axes.plot([0,1,2,3,4,5,6,7], [1,2,3,10,20,30,100,200])
        self.rawCanvas.draw()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PdafToolApp()
    sys.exit(app.exec_())
