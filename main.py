import sys

from PyQt5.QtCore import Qt, QPoint
from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
from PyQt5.QtGui import QPainter, QColor, QPolygon
from random import randrange as rd


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.do_paint = False
        uic.loadUi('UI.ui', self)
        self.size_min_rad = 5
        self.size_max_rad = 100
        self.btn.clicked.connect(self.run)

    def run(self):
        self.x, self.y = rd(50, 650), rd(50, 650)
        self.type = 'circle'
        self.paint()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_flag(self, qp):
        k = [255, 255, 0]
        qp.setBrush(QColor(k[0], k[1], k[2]))
        self.size_rad = rd(self.size_min_rad, self.size_max_rad)
        if self.type == 'circle':
            qp.drawEllipse(self.x - self.size_rad, self.y - self.size_rad, 2 * self.size_rad,
                           2 * self.size_rad)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
