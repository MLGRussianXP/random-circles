import sys

from PyQt5 import uic
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow

from random import randint

if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        # self.setupUi(self)

        self.pushButton.clicked.connect(self.update)

    def create_circles(self, qp: QtGui.QPainter):
        qp.setBrush(QtGui.QColor(255, 241, 50))
        r = randint(10, 200)
        qp.drawEllipse(
            QtCore.QPoint(randint(50, self.width() - 50), randint(50, self.height() - 50)), r, r
        )

    def paintEvent(self, event):
        qp = QtGui.QPainter()
        qp.begin(self)
        self.create_circles(qp)
        qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
