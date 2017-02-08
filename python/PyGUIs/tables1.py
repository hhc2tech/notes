# -*- coding: utf-8 -*-
'''
https://www.daniweb.com/programming/software-development/code/447834/applying-pysides-qabstracttablemodel

 ps_QAbstractTableModel_solvents.py
use PySide's QTableView and QAbstractTableModel for tabular data
sort columns by clicking on the header title
here applied to solvents commonly used in Chemistry
PySide is the official LGPL-licensed version of PyQT
tested with PySide112 and Python27/Python33 by vegaseat  15feb2013
'''
import operator
from PySide.QtCore import *
from PySide.QtGui import *
class MyWindow(QWidget):
    def __init__(self, data_list, header, *args):
        QWidget.__init__(self, *args)
        # setGeometry(x_pos, y_pos, width, height)
        self.setGeometry(300, 200, 570, 450)
        self.setWindowTitle("Click on column title to sort")
        table_model = MyTableModel(self, data_list, header)
        table_view = QTableView()
        table_view.setModel(table_model)
        # set font
        font = QFont("Courier New", 14)
        table_view.setFont(font)
        # set column width to fit contents (set font first!)
        table_view.resizeColumnsToContents()
        # enable sorting
        table_view.setSortingEnabled(True)
        layout = QVBoxLayout(self)
        layout.addWidget(table_view)
        self.setLayout(layout)
class MyTableModel(QAbstractTableModel):
    def __init__(self, parent, mylist, header, *args):
        QAbstractTableModel.__init__(self, parent, *args)
        self.mylist = mylist
        self.header = header
    def rowCount(self, parent):
        return len(self.mylist)
    def columnCount(self, parent):
        return len(self.mylist[0])
    def data(self, index, role):
        if not index.isValid():
            return None
        elif role != Qt.DisplayRole:
            return None
        return self.mylist[index.row()][index.column()]
    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.header[col]
        return None
    def sort(self, col, order):
        """sort table by given column number col"""
        self.emit(SIGNAL("layoutAboutToBeChanged()"))
        self.mylist = sorted(self.mylist,
            key=operator.itemgetter(col))
        if order == Qt.DescendingOrder:
            self.mylist.reverse()
        self.emit(SIGNAL("layoutChanged()"))
# the solvent data ...
header = ['Solvent Name', ' BP (deg C)', ' MP (deg C)', ' Density (g/ml)']
# use numbers for numeric data to sort properly
data_list = [
('ACETIC ACID', 117.9, 16.7, 1.049),
('TRIETHYLAMINE', 89.5, -114.7, 0.726),
('TRIFLUOROACETIC ACID', 71.8, -15.3, 1.489),
('WATER', 100.0, 0.0, 1.0),
('XYLENES', 139.1, -47.8, 0.86)
]
app = QApplication([])
win = MyWindow(data_list, header)
win.show()
app.exec_()