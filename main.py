from PyQt5.QtWidgets import *
from styles import *

from PyQt5.QtCore import *
from PyQt5.QtGui import *


app = QApplication([])


class CalculatorWindow(QWidget):
    def __init__(self, save_to_history):
        super().__init__()
        self.setMinimumSize(400, 600)

        self.setWindowTitle("Kalkulyator")

        self.calc_input = QLabel("")
        self.calc_input.setFixedHeight(50)
        self.calc_input.setAlignment(Qt.AlignRight)
        self.calc_input.setFont(QFont("Arial", 20))

        grid = QGridLayout()
        buttons = [
            ('AC', 0, 0), ('back', 0, 1), ('%', 0, 2), ('/', 0, 3),
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('*', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('+', 3, 3),
            ('+/-', 4, 0), ('0', 4, 1), (',', 4, 2), ('=', 4, 3),
        ]

        for (text, row, col) in buttons:
            button = QPushButton(text)
            button.setFont(QFont("Arial", 19))
            button.clicked.connect(self.show_btn)
            button.setFixedSize(100, 80)
            grid.addWidget(button, row, col)

            if row == 0 or col == 3:
                button.setStyleSheet("color: #FF6D00")
            if text == '=':
                button.setStyleSheet("background-color: #FF6D00; color: white; border-radius: 40px; border: none")
            if text == '+/-':
                button.setStyleSheet("color: #FF6D00")
            if text == 'back':
                button.setStyleSheet("font-size: 25px; color: #FF6D00")
            if text == 'AC':
                button.setStyleSheet("font-size: 25px; color: #FF6D00")


        vertical = QVBoxLayout()
        vertical.addWidget(self.calc_input)
        vertical.addLayout(grid)


        self.setLayout(vertical)
        self.save_to_history = save_to_history
    def show_btn(self):
        sender = self.sender()
        text = sender.text()
        if text == '=':
            expression = self.calc_input.text()
            try:
                result = str(eval(expression.replace(',', '.')))
                self.calc_input.setText(result)
                self.save_to_history(expression + " = " + result)
            except Exception as e:
                self.calc_input.setText("Error")
        elif text == 'AC':
            self.calc_input.setText("")
        elif text == 'back':
            current_text = self.calc_input.text()
            self.calc_input.setText(current_text[:-1])
        elif text == '+/-':
            current_text = self.calc_input.text()
            if current_text:
                if current_text.startswith('-'):
                    self.calc_input.setText(current_text[1:])
                else:
                    self.calc_input.setText('-' + current_text)
        else:
            current_text = self.calc_input.text()
            self.calc_input.setText(current_text + text)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.calculator_window = CalculatorWindow(self.save_to_history)

        screen = QApplication.primaryScreen()
        self.setMinimumSize(screen.size().width(), screen.size().height())

        self.setWindowTitle("Kalkulyator oynasi")
        self.setStyleSheet("background-color: white")

        self.label = QLabel("Калькулятор")
        self.label.setStyleSheet(labelStyle)

        self.qoshishBtn = QPushButton("Add")
        self.qoshishBtn.setStyleSheet("font-size: 24px; background-color: #008744; border-radius: 5px; color: white")
        self.qoshishBtn.setFixedSize(300, 75)
        self.qoshishBtn.clicked.connect(self.show_calculator)

        self.list = QListWidget()
        self.list.setStyleSheet(qlistwidget_style)
        self.list.clicked.connect(self.show_list)

        container = QHBoxLayout()
        container.addWidget(self.label)
        container.addWidget(self.qoshishBtn)

        vertical = QVBoxLayout()
        vertical.addLayout(container)
        vertical.addWidget(self.list)

        widget = QWidget()
        widget.setLayout(vertical)

        self.setCentralWidget(widget)

    def show_calculator(self):
        self.calculator_window.show()

    def save_to_history(self, entry):
        self.list.addItem(entry)

    def show_list(self):
        item = self.list.currentItem()
        if item:
            QMessageBox.information(self, "Tarix", item.text(), QMessageBox.Ok)


main = MainWindow()
main.show()

app.exec_()