import sys
import random
from PyQt6 import QtWidgets
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
        color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.circles.append((x, y, diameter, color))
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        for x, y, diameter, color in self.circles:
            painter.setBrush(color)
            painter.drawEllipse(QRect(x, y, diameter, diameter))

        painter.end()


class MainApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Random Circles")
        self.setGeometry(100, 100, 800, 600)

        central_widget = QtWidgets.QWidget(self)
        self.setCentralWidget(central_widget)

        self.button = QtWidgets.QPushButton("Add Circle", self)
        self.button.setGeometry(10, 10, 150, 40)

        self.draw_widget = DrawWidget(self)
        self.draw_widget.setGeometry(10, 60, 780, 530)
        self.draw_widget.setStyleSheet("background-color: white;")

        self.button.clicked.connect(self.draw_widget.add_circle)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec())
