from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        # self.count = 0
        self.initUI()

    def initUI(self):
        self.ui = uic.loadUi("calculator.ui", self)
        self.show()
        # self.ui.pushButton.clicked.connect(self.countUp)

    def countUp(self):
        self.count += 1
        self.ui.lcdDisplay.display()

    # key input
    def keyPressEvent(self, event):
        if event.text() == 'r':
            self.count = 0
            self.ui.lcdDisplay.display(self.count)


def main():
    app = QtWidgets.QApplication(sys.argv)
    cnt = Calculator()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
