
from PyQt6.QtWidgets import *

class MainWindow(QMainWindow):
    def closeEvent(self, e):
        if not text.document().isModified():
            return
        answer = QMessageBox.question(
            window, None,
            "You have unsaved changes. Save before closing?",
            QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel
        )
        if answer & QMessageBox.Save:
            save()
            if text.document().isModified():
                e.ignore()
        elif answer & QMessageBox.Cancel:
            e.ignore()