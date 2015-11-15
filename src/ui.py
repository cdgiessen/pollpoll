#!/usr/bin/env python2.7
import sys
from PyQt4 import QtGui, QtCore

class PollPollUI(QtGui.QMainWindow):
        def __init__(self):
                super(PollPollUI, self).__init__()
                self.initUI()

        def initUI(self):
                exitAction = QtGui.QAction(QtGui.QIcon('exit.png'), '&Exit', self)
                exitAction.setShortcut('Ctrl+Q')
                exitAction.setStatusTip('Exit application')
                exitAction.triggered.connect(QtGui.qApp.quit)

                self.statusBar()

                menubar = self.menuBar()
                fileMenu = menubar.addMenu('&File')
                fileMenu.addAction(exitAction)
                self.setGeometry(300, 300, 250, 200)
                self.setWindowTitle('Icon')
                self.setWindowIcon(QtGui.QIcon('pp_icon.png'))
                self.show()

def main():
        app = QtGui.QApplication(sys.argv)
        g = PollPollUI()
        sys.exit(app.exec_())
if __name__ == '__main__':
        main()
