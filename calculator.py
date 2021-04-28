from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
import sys


class Calculator(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.__input = []
        self._initKeys()
        self._initButtons()

    def initUI(self):
        self.ui = uic.loadUi("calculator.ui", self)
        self.show()

    # declaring every possible input
    def _initKeys(self):
        self.__DELETE = "delete"
        self.__CLEAR = "clear"
        self.__KEYBOARD_SHIFT = 16777248
        self.__KEYBOARD_DIGITS = ("0", "1", "2",
                                  "3", "4", "5", "6", "7", "8", "9")
        self.__KEYBOARD_OPERATOR = (".", "/", "*", "-", "+", "=")
        self.__UI_DIGITS = ("btnZero", "btnOne", "btnTwo", "btnThree",
                            "btnFour", "btnFive", "btnSix", "btnSeven",
                            "btnEight", "btnNine")

    # connecting buttons for event handling
    def _initButtons(self):
        # // NOTE: dynamic init of buttons would be prefered
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
        self.ui.btnDelete.clicked.connect(
            lambda x: self.onClick(self.__DELETE))
        self.ui.btnClear.clicked.connect(lambda x: self.onClick(self.__CLEAR))

    def logButton(message):
        def funcDecorator(func):
            def newFunc(self, event):
                print(message + event)
                func(self, event)

                print("Current expression: " + (''.join(self.__input)))

                if (event == "="):
                    print("Result is: " + str(eval(''.join(self.__input))))

            return newFunc
        return funcDecorator

    def logKeyboard(message):
        def funcDecorator(func):
            def newFunc(self, event):
                if (event.key() != self.__KEYBOARD_SHIFT):
                    print(message + (chr(event.key())))
                func(self, event)

                print("Current expression: " + (''.join(self.__input)))

                if (event == "="):
                    print("Result is: " + str(eval(''.join(self.__input))))

            return newFunc
        return funcDecorator

    def logError(message):
        def funcDecorator(func):
            def newFunc(self, err):
                print(message + str(err))
                func(self, err)

            return newFunc
        return funcDecorator

    def displayInput(self):
        self.ui.labelResult.setText(''.join(self.__input))

    def displayResult(self, result):
        self.ui.labelResult.setText(result)

    def calculateResult(self):
        try:
            result = str(eval(''.join(self.__input)))
            self.clear()
            self.__input.append(result)
            self.displayResult(result)
        except Exception as err:
            self.displayError(err)

    @logError("Error: ")
    def displayError(self, err):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Error")
        msg.setWindowTitle("Error")
        msg.setInformativeText(str(err))
        msg.exec_()

    def checkMathExpression(self, newValue):
        # first check if only one operator is following a digit
        if (len(self.__input) == 0 and newValue in self.__KEYBOARD_DIGITS):
            return True
        elif (newValue in self.__KEYBOARD_DIGITS):
            return True
        elif (newValue in self.__KEYBOARD_OPERATOR and
                self.__input[-1] in self.__KEYBOARD_DIGITS):
            return True

        return False

    def clear(self):
        self.__input = []

    def delete(self):
        del self.__input[-1]

    def handleInput(self, event):
        if (event == self.__CLEAR):
            self.clear()
            self.displayInput()
        elif (event == self.__DELETE):
            self.delete()
            self.displayInput()

        if (event == "=" and self.checkMathExpression(event)):
            self.calculateResult()

        elif (self.checkMathExpression(event)):
            self.__input.append(event)
            self.displayInput()

    # button inputs
    @logButton("Button clicked: ")
    def onClick(self, event):
        self.handleInput(event)

    # keyboard inputs
    @logKeyboard("Keyboard clicked: ")
    def keyPressEvent(self, event):
        correctInputs = self.__KEYBOARD_DIGITS + self.__KEYBOARD_OPERATOR

        # check if valid keyboard input was given
        if (event.key() != self.__KEYBOARD_SHIFT and
                chr(event.key()) in correctInputs):
            self.handleInput((chr(event.key())))


def main():
    app = QtWidgets.QApplication(sys.argv)
    calculator = Calculator()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
