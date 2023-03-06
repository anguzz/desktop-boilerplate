import sys
from window import MainWindow
from PyQt6.QtWidgets import QApplication

app = QApplication(sys.argv)
window = MainWindow()
window.show()  #window hidden by default

app.exec()


