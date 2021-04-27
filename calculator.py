from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class Calculator(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.__result = 0
        self.__input = ""
        self._setKeyboardKeys()

    def _setKeyboardKeys(self): 
        self.__KEYBOARD_DIGIT = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.__KEYBOARD_OPERATOR = [".", ",", "/", "*", "-", "+", "="]

    def initUI(self):
        self.ui = uic.loadUi("calculator.ui", self)
        self.show()
        # self.ui.pushButton.clicked.connect(self.countUp)

    def checkInput(self, key):
        print(key)

    def countUp(self):
        self.count += 1
        self.ui.lineDisplay.display()

    # key inputs
    def keyPressEvent(self, event):
        # if(self.checkInput(event.key())):
        #     # calculate
        #     print(0)
        # else:
        #     # ignore
        #     print("1")

        if event.text() == "1":
            self.__input += "1"

        if event.text() == "+":
            self.__input += "+"

        self.ui.labelResult.setText(self.__input)


def main():
    app = QtWidgets.QApplication(sys.argv)
    calculator = Calculator()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
