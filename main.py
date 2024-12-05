import sys
import random
from PyQt6 import QtWidgets, uic
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import QRect


class DrawWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.circles = []

    def add_circle(self):
        x = random.randint(10, self.width() - 50)
        y = random.randint(10, self.height() - 50)
        diameter = random.randint(10, 100)
        self.circles.append((x, y, diameter))
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        for x, y, diameter in self.circles:
            painter.setBrush(QColor("yellow"))
            painter.drawEllipse(QRect(x, y, diameter, diameter))

        painter.end()


class MainApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)

        self.widget = self.findChild(QtWidgets.QWidget, "drawArea")

        self.layout = QtWidgets.QVBoxLayout(self.widget)
        self.draw_widget = DrawWidget(self.widget)
        self.layout.addWidget(self.draw_widget)

        self.button = self.findChild(QtWidgets.QPushButton, "pushButton")
        self.button.clicked.connect(self.draw_widget.add_circle)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec())
