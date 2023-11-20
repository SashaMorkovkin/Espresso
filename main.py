from PyQt5.QtWidgets import QMainWindow, QApplication
import sys
from PyQt5 import uic
import sqlite3


class Espresso(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.arr = []
        self.arr2 = []
        self.zakaz.clicked.connect(self.run)
        self.arr2.append(self.radioButton)
        self.arr2.append(self.radioButton_2)
        self.arr2.append(self.radioButton_3)

    def run(self):
        con = sqlite3.connect('coffee.sqlite')
        cur = con.cursor()
        for i in self.arr2:
            if i.isChecked():
                self.qw = i.text()
                print(self.qw)
        self.arr = cur.execute(
            f'SELECT name, hot, moloty, vkus, cost, obyom FROM Coffee WHERE name like {self.qw}').fetchall()
        print(self.arr[0])
        con.commit()
        con.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    flag_maker = Espresso()

    flag_maker.show()
    sys.exit(app.exec())