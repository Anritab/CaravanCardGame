from pytestqt.qt_compat import qt_api

from caravanassets.gui.buttons import Window


import PyQt5.QtCore

print(PyQt5.QtCore)


class TestGUI:
    def test_price(self, qtbot):

        window = Window()
        window.show()
        qtbot.addWidget(window)

        window.input_caravan.setText('2 1 3 3')
        window.combobox.setCurrentText('price')

        qtbot.mouseClick(window.button, qt_api.QtCore.Qt.MouseButton.LeftButton)
        assert window.result.text() == '7'

    def test_direction(self, qtbot):

        window = Window()
        window.show()
        qtbot.addWidget(window)

        window.input_caravan.setText('2 1 3 3')
        window.combobox.setCurrentText('direction')

        qtbot.mouseClick(window.button, qt_api.QtCore.Qt.MouseButton.LeftButton)
        assert window.result.text() == 'up'

    def test_suit(self, qtbot):

        window = Window()
        window.show()
        qtbot.addWidget(window)

        window.input_caravan.setText('2 1 3 3')
        window.combobox.setCurrentText('last_suit')

        qtbot.mouseClick(window.button, qt_api.QtCore.Qt.MouseButton.LeftButton)
        assert window.result.text() == 'Clubs'

    def test_card(self, qtbot):

        window = Window()
        window.show()
        qtbot.addWidget(window)

        window.input_caravan.setText('2 1 3 3')
        window.combobox.setCurrentText('last_nonpic')

        qtbot.mouseClick(window.button, qt_api.QtCore.Qt.MouseButton.LeftButton)
        assert window.result.text() == 'Four Clubs'