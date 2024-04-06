import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton


# Класс калькулятора
class Calculator(QWidget):

    # Инициализация экземпляра класса
    def __init__(self):
        super(Calculator, self).__init__()

        # Инициализация кнопок и окна
        self.vbox = QVBoxLayout(self)
        self.hbox_input = QHBoxLayout()
        self.hbox_first = QHBoxLayout()
        self.hbox_second = QHBoxLayout()
        self.hbox_third = QHBoxLayout()
        self.hbox_fourth = QHBoxLayout()
        self.hbox_fifth = QHBoxLayout()
        self.hbox_result = QHBoxLayout()

        # Слои в списке
        layouts = [
            self.hbox_input,
            self.hbox_first,
            self.hbox_second,
            self.hbox_third,
            self.hbox_fourth,
            self.hbox_fifth,
            self.hbox_result
        ]

        # Добавление слоев в калькулятор
        for layout in layouts:
            self.vbox.addLayout(layout)

        # Строка для ввода и вывода
        self.input = QLineEdit(self)
        self.input.setText("0")
        self.hbox_input.addWidget(self.input)

        # Номера слоев из списка layouts для кнопок
        button_layers = {
            '1': 1, '2': 1, '3': 1,
            '4': 2, '5': 2, '6': 2,
            '7': 3, '8': 3, '9': 3,
            '0': 4, '+': 4, '-': 4,
            '*': 5, ':': 5,
                        }

        # Множество кнопок для чисел
        dig = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}
        # Множество для операций
        opers = {'+', '-', '*', '/'}
        # Слои в окне
        layouts = [self.hbox_first, self.hbox_second, self.hbox_third,
                   self.hbox_fourth, self.hbox_fifth]

        # Функции для привязки кнопок
        def connect_dig_button(butt, txt):
            butt.clicked.connect(lambda: self._button(txt))

        def connect_oper_button(butt, txt):
            butt.clicked.connect(lambda: self._operation(txt))

        # Привзяка кнопок для множеств
        for text, layer in button_layers.items():

            button = QPushButton(text, self)
            layouts[layer-1].addWidget(button)

            if text in dig:
                connect_dig_button(button, text)

            elif text in opers:
                connect_oper_button(button, text)

        # Добавление и привязка остальных элементов калькулятора
        self.b_dot = QPushButton(".", self)
        self.hbox_fifth.addWidget(self.b_dot)

        self.b_result = QPushButton("=", self)
        self.hbox_result.addWidget(self.b_result)

        self.b_clear = QPushButton("C", self)
        self.hbox_result.addWidget(self.b_clear)

        self.b_clear.clicked.connect(lambda: self._clear())
        self.b_result.clicked.connect(self._result)
        self.b_dot.clicked.connect(lambda: self._dot("."))

        self.num_1 = float(0)
        self.op = ""

    # Функция точки для дробных чисел
    def _dot(self, param):
        line = self.input.text()
        k = str(self.input.text())
        if k[-1] == '.':
            pass
        else:
            self.input.setText(line + param)

    # Функция очистки
    def _clear(self):
        self.num_1 = float(0)
        self.input.setText("0")
        self.op = ""

    # Функция для цифр
    def _button(self, param):
        line = self.input.text()
        if line == "0":
            line = ""
        self.input.setText(line + param)

    # Функция для операций
    def _operation(self, op):
        self.num_1 = float(self.input.text())
        self.op = op
        self.input.setText("")

    # Функция подсчета результата
    def _result(self):
        try:
            self.num_2 = float(self.input.text())
            if self.op == "":
                self.num_1 = float(self.input.text())
                if self.num_1 % 1 == 0:
                    k = str(self.num_1)
                    self.input.setText(k[:-2])
            elif self.op == "+":
                k = float(self.num_1 + self.num_2)
                if k % 1 == 0:
                    k = str(k)
                    self.input.setText(k[:-2])
                else:
                    self.input.setText(str(self.num_1 + self.num_2))
            elif self.op == "-":
                k = float(self.num_1 - self.num_2)
                if k % 1 == 0:
                    k = str(k)
                    self.input.setText(k[:-2])
                else:
                    self.input.setText(str(self.num_1 - self.num_2))
            elif self.op == "*":
                k = float(self.num_1 * self.num_2)
                if k % 1 == 0:
                    k = str(k)
                    self.input.setText(k[:-2])
                else:
                    self.input.setText(str(self.num_1 * self.num_2))
            elif self.op == "/":
                k = float(self.num_1 / self.num_2)
                if k % 1 == 0:
                    k = str(k)
                    self.input.setText(k[:-2])
                else:
                    self.input.setText(str(self.num_1 / self.num_2))
            self.op = ""
            self.num_1 = float(self.input.text())
        except ZeroDivisionError:
            print("введите число, не равное 0")
            self.input.setText(str(''))
        except ValueError:
            if self.num_1 % 1 == 0:
                k = str(self.num_1)
                self.input.setText(k[:-2])
            else:
                self.input.setText(str(self.num_1 / self.num_2))


# Запуск приложения
app = QApplication(sys.argv)
win = Calculator()
win.show()
sys.exit(app.exec_())
