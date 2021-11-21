# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys
from random import random
import decimal

from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader

class calculations():
    def montecalro(self):
        a = i = y = x = progress = 1
        output = ""
        while i < self:
            x = random()
            y = random()
            z = (x**2) + (y**2)
            if z <= 1:
                a += 1
            else:
                pass
            i += 1
            progress += 1
        output = decimal.Decimal(a) / decimal.Decimal(self)
        print(output)
    
    def riemmanzeta(self):
        i = 1
        a = 0
        progress = 0
        output = ""
        while i < self:
            a += (i**2)**-1
            i += 1
            progress += 1
        output = a
        print(output)


class Widget(QWidget):
    def __init__(self):
        super(Widget, self).__init__()
        self.load_ui()
        self.setWindowTitle('Python PI')

    def load_ui(self):
        loader = QUiLoader()
        path = os.fspath(Path(__file__).resolve().parent / "form.ui")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        loader.load(ui_file, self)
        ui_file.close()


if __name__ == "__main__":
    app = QApplication([])
    widget = Widget()
    widget.show()
    sys.exit(app.exec_())
