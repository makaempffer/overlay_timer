import sys
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel
from user import User
from engine import Engine
import keyboard


class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(
            QtCore.Qt.WindowStaysOnTopHint |
            QtCore.Qt.FramelessWindowHint |
            QtCore.Qt.X11BypassWindowManagerHint
        )
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setGeometry(
            QtWidgets.QStyle.alignedRect(
                QtCore.Qt.LeftToRight, QtCore.Qt.AlignCenter,
                QtCore.QSize(220, 200),
                QtWidgets.qApp.desktop().availableGeometry()
            )
        )
        self.setFixedSize(220, 200)
        self.setup()

        # Call key pressed function
        keyboard.on_press(self.logic_engine.handleKeyPress)
        main_layout = QHBoxLayout()
        self.setLayout(main_layout)

        # First column
        first_column_layout = QVBoxLayout()
        main_layout.addLayout(first_column_layout)

        self.label1 = QLabel("LEVEL")
        self.label1.setStyleSheet("color: white")
        self.label2 = QLabel("PROGRESS")
        self.label2.setStyleSheet("color: white")
        first_column_layout.addWidget(self.label1)
        first_column_layout.addWidget(self.label2)

        # Second column
        second_column_layout = QVBoxLayout()
        main_layout.addLayout(second_column_layout)

        self.big_label = QLabel("Big Text")
        self.big_label.setStyleSheet("color: white")
        second_column_layout.addWidget(self.big_label)

        # Third column
        third_column_layout = QVBoxLayout()
        main_layout.addLayout(third_column_layout)

        self.label3 = QLabel("LAST KEY")
        self.label3.setStyleSheet("color: white")
        self.label4 = QLabel("CUR. DAY")
        self.label4.setStyleSheet("color: white")
        third_column_layout.addWidget(self.label3)
        third_column_layout.addWidget(self.label4)
    
    def setup(self):
        self.user = User()
        self.logic_engine = Engine(self.user, self)

    


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mywindow = MainWindow()
    mywindow.show()
    app.exec_()
