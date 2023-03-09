from PyQt6.QtGui import QKeySequence, QAction
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtCore import Qt


from window import MainWindow

#========================app init=========================
app = QApplication([])

app.setStyle("Fusion")
#possible options are Windows, Fusion

app.setApplicationName("Notepad")
text = QPlainTextEdit()
window = MainWindow()
window.setCentralWidget(text)

FilePath = None
#========================dark mode palette========================

palette = app.palette()

darkgrey= '#7393B3'
lightblue='#EAEAEA'
black='#151a1c'
white='#FFFFFF'

palette.setColor(QPalette.ColorRole.Window, QColor(darkgrey))
palette.setColor(QPalette.ColorRole.WindowText, QColor(white)) 
palette.setColor(QPalette.ColorRole.Base, QColor(black))
palette.setColor(QPalette.ColorRole.AlternateBase, QColor(black))
palette.setColor(QPalette.ColorRole.ToolTipBase, QColor(darkgrey))
palette.setColor(QPalette.ColorRole.ToolTipText, Qt.GlobalColor.white)
palette.setColor(QPalette.ColorRole.Text, QColor(white))
palette.setColor(QPalette.ColorRole.Button, QColor(black))
palette.setColor(QPalette.ColorRole.ButtonText, Qt.GlobalColor.white)
palette.setColor(QPalette.ColorRole.BrightText, QColor(white))
palette.setColor(QPalette.ColorRole.Link, QColor(white))

app.setPalette(palette)

#=====================functions========================== 
def openFile():
    global FilePath
    path = QFileDialog.getOpenFileName(window, "Open")[0]
    if path:
        text.setPlainText(open(path).read())
        FilePath = path

def saveAs():
    global FilePath
    path = QFileDialog.getSaveFileName(window, "Save As")[0]
    if path:
        FilePath = path
        save()
        
def changeFont():
       font, ok = QFontDialog.getFont()
       if ok:
            text.setFont(font)



def save():
    if FilePath is None:
        saveAs()
    else:
        with open(FilePath, "w") as f:
            f.write(text.toPlainText())
        text.document().setModified(False)

#=======================buttons/events==========================

fileButton = window.menuBar().addMenu("&File")

openEvent = QAction("&Open")
openEvent.triggered.connect(openFile)
openEvent.setShortcut(QKeySequence.StandardKey.Open)
fileButton.addAction(openEvent)

saveFileEvent = QAction("&Save")
saveFileEvent.triggered.connect(save)
saveFileEvent.setShortcut(QKeySequence.StandardKey.Save)
fileButton.addAction(saveFileEvent)

saveFileAsEvent = QAction("Save &As...")
saveFileAsEvent.triggered.connect(saveAs)
fileButton.addAction(saveFileAsEvent)

closeEvent = QAction("&Close")
closeEvent.triggered.connect(window.close)
fileButton.addAction(closeEvent)


optionsButton = window.menuBar().addMenu("&Options")

editFontEvent = QAction("&Font")
editFontEvent.triggered.connect(changeFont)
optionsButton.addAction(editFontEvent)



#==========================exit app==================================
window.show()
app.exec()