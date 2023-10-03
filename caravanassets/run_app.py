from .gui.app import Application


def start():
    app = Application([])
    quit(app.exec())