import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor


app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Who wants to be a programmer?")
window.setStyleSheet("background: #161219;")

grid = QGridLayout()

def frame1():
    image = QPixmap("logo.png")
    logo = QLabel()
    logo.setPixmap(image)
    logo.setAlignment(QtCore.Qt.AlignCenter)
    logo.setStyleSheet("margin-top: 100px;")

    button = QPushButton("Start")
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button.setStyleSheet(
        "*{border: 4px solid '#006CBC';" + 
        "border-radius: 15px;"+
        "font-size: 35px;"+
        "color: '#006CBC';" +
        "width: 50%;}"+
        "*:hover{background: '#006CBC';" +
        "color: 'white';}"
    )

    grid.addWidget(logo, 0, 0)
    grid.addWidget(button, 1, 0)

frame1()

window.setLayout(grid)

window.show()
sys.exit(app.exec())