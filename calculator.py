from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class Calculator(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.__result = 0
        self.__input = []
        self._initKeys()
        self._initButtons()

    def initUI(self):
        self.ui = uic.loadUi("calculator.ui", self)
        self.show()
        # self.ui.pushButton.clicked.connect(self.countUp)

    # declaring every possible input
    def _initKeys(self):
        self.__KEYBOARD_SHIFT = 16777248
        self.__KEYBOARD_DIGITS = ("0", "1", "2",
                                  "3", "4", "5", "6", "7", "8", "9")
        self.__KEYBOARD_OPERATOR = (".", "/", "*", "-", "+", "=")
        self.__UI_DIGITS = ("btnZero", "btnOne", "btnTwo", "btnThree",
                            "btnFour", "btnFive", "btnSix", "btnSeven", "btnEight", "btnNine")
        self.__UI_OPERATOR = ("btnDecimal", "btnCalculate", "btnPlus", "btnMinus",
                              "btnMultiply", "btnDivide", "btnClear", "btnDelete")

    # connecting buttons for event handling
    def _initButtons(self):
        # // TODO: dynamic init of buttons would be prefered
        # for a, b in zip(self.__KEYBOARD_DIGITS, self.__UI_DIGITS):
        #     self.ui.b.clicked.connect(lambda x: self.onClick(a))
        self.ui.btnZero.clicked.connect(lambda x: self.onClick("0"))
        self.ui.btnOne.clicked.connect(lambda x: self.onClick("1"))
        self.ui.btnTwo.clicked.connect(lambda x: self.onClick("2"))
        self.ui.btnThree.clicked.connect(lambda x: self.onClick("3"))
        self.ui.btnFour.clicked.connect(lambda x: self.onClick("4"))
        self.ui.btnFive.clicked.connect(lambda x: self.onClick("5"))
        self.ui.btnSix.clicked.connect(lambda x: self.onClick("6"))
        self.ui.btnSeven.clicked.connect(lambda x: self.onClick("7"))
        self.ui.btnEight.clicked.connect(lambda x: self.onClick("8"))
        self.ui.btnNine.clicked.connect(lambda x: self.onClick("9"))
        self.ui.btnDecimal.clicked.connect(lambda x: self.onClick("."))
        self.ui.btnCalculate.clicked.connect(lambda x: self.onClick("="))
        self.ui.btnPlus.clicked.connect(lambda x: self.onClick("+"))
        self.ui.btnMinus.clicked.connect(lambda x: self.onClick("-"))
        self.ui.btnMultiply.clicked.connect(lambda x: self.onClick("*"))
        self.ui.btnDivide.clicked.connect(lambda x: self.onClick("/"))
        self.ui.btnDelete.clicked.connect(lambda x: self.onClick(self.delete))
        self.ui.btnClear.clicked.connect(lambda x: self.onClick(self.clear))

    def displayInput(self):
        print(''.join(self.__input))
        self.ui.labelResult.setText(''.join(self.__input))

    def displayResult(self):
        result = str(eval(''.join(self.__input)))
        self.ui.labelResult.setText(result)
        # TODO: func clear
        # TODO: set result in index 0

    def checkMathExpression(self, newValue):
        try:
            # first check if only one operator is following a digit
            if (len(self.__input) == 0 and newValue in self.__KEYBOARD_DIGITS):
                return True
            elif (newValue in self.__KEYBOARD_DIGITS):
                return True
            elif (newValue in self.__KEYBOARD_OPERATOR and self.__input[-1] in self.__KEYBOARD_DIGITS):
                return True

            return False
        except Exception as e:
            print(e)

    def onClick(self, event):
        if (event == "=" and self.checkMathExpression(event)):
            self.displayResult()

        elif (self.checkMathExpression(event)):
            self.__input.append(event)
            self.displayInput()

    # keyboard inputs

    def keyPressEvent(self, event):
        correctInputs = self.__KEYBOARD_DIGITS + self.__KEYBOARD_OPERATOR

        # check if valid keyboard input was given
        if (event.key() != self.__KEYBOARD_SHIFT and chr(event.key()) in correctInputs):
            self.onClick(chr(event.key()))


def main():
    app = QtWidgets.QApplication(sys.argv)
    calculator = Calculator()
    sys.exit(app.exec_())
    # TODO: 3: on result give display result
    # TODO: 3.5: add removing and clearing
    # TODO: 4: add logging
    # TODO: 5: add error display


if __name__ == '__main__':
    main()
