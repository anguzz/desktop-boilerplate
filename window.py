from PyQt6.QtWidgets import QApplication, QMainWindow,QPushButton,QWidget
from PyQt6.QtCore import QSize, Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("App")
        button = QPushButton("Button")
        button.setFixedSize(QSize(100, 100))

        self.setFixedSize(QSize(500, 500))
        self.setCentralWidget(button)
      