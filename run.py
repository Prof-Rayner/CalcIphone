from PyQt5.QtWidgets import QApplication
from interface import Calculadora

if __name__ == "__main__":
    app = QApplication([])
    login = Calculadora()
    app.exec_()
