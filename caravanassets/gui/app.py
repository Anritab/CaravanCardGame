from PyQt5.QtWidgets import QApplication

from .buttons import Window


class Application(QApplication):
    def __init__(self, *args, **kwargs):
        QApplication.__init__(self, *args, **kwargs)
        window = Window()
        window.show()
        self.window = window

    def exec(self):
        result = QApplication.exec()
        return result