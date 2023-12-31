from PyQt5.QtWidgets import (
    QMainWindow,
    QLabel,
    QPushButton,
    QLineEdit,
    QVBoxLayout,
    QWidget,
    QComboBox,
)
from PyQt5.QtCore import pyqtSlot

from caravanassets.cards import NAMES, SUITS, Card
from caravanassets.moves import (
    price,
    last_nonpic_card,
    last_suit_check,
    direction_check,
    add_card
)

class MyComboBox(QComboBox):
    def __init__(self):
        super().__init__()

class MyQLineEdit(QLineEdit):
    def __init__(self):
        super().__init__()

class MyQBoxLayout(QVBoxLayout):
    def __init__(self):
        super().__init__()
class MyQWidget(QWidget):
    def __init__(self):
        super().__init__()

class MyQLabel(QLabel):
    def __init__(self):
        super().__init__()

class MyQPushButton(QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.input_caravan = MyQLineEdit()

        self.combobox = MyComboBox()
        self.combobox.addItems(['price', 'last_nonpic', 'last_suit', 'direction'])

        self.button = MyQPushButton('Use', self)
        self.button.clicked.connect(self.caratools)

        self.result = MyQLabel()

        self.layout = MyQBoxLayout()
        self.layout.addWidget(self.input_caravan)
        self.layout.addWidget(self.combobox)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.result)

        container = MyQWidget()
        container.setLayout(self.layout)

        self.setCentralWidget(container)

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Caravan Tools')
        self.show()

    @pyqtSlot()
    def caratools(self):
        try:
            Caravan = []
            scaravan = list(map(int, self.input_caravan.text().split()))
            for i in range(0, len(scaravan), 2):
                Caravan.append(Card(scaravan[i], scaravan[i + 1]))

            temp = self.combobox.currentText()

            if temp == 'price':
                self.result.setText(str(price(Caravan)))

            elif temp == 'last_nonpic':
                self.result.setText(last_nonpic_card(Caravan).name + " " + last_nonpic_card(Caravan).suit)

            elif temp == 'last_suit':
                self.result.setText(str(SUITS[last_suit_check(Caravan)]))

            elif temp == 'direction':
                self.result.setText(str(direction_check(Caravan)))
            else:
                print(0/0)

        except:
            self.result.setText('error')
