from PySide6 import QtWidgets

import super_clicks

class SuperClick(super_clicks.Ui_mainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(SuperClick, self).__init__()
        self.setupUi(self)

if __name__ == '__main__':
    app = QtWidgets.QApplication()
    qt_app = SuperClick()
    qt_app.show()
    app.exec_()