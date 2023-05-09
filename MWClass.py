from PyQt6.QtWidgets import QMainWindow, QFileDialog, QTableWidget, QTableWidgetItem
from myui import Ui_MainWindow
from SWCLass import SecondWindow
import pandas as pd

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.swin = SecondWindow()
        self.swin.test_signal.connect(self.print)
        self.show()
    def selectFile(self):
        self.fill_table_ff(QFileDialog.getOpenFileName()[0])
    def print(self):
        for i in self.swin.listT:
            self.fill_table_f_df(self.swin.dfw[int(i)])
    def fill_table_ff(self, currentData):
        df = pd.read_csv(currentData)
        table = QTableWidget()
        headers = df.columns.values.tolist()
        table.setColumnCount(len(headers))
        table.setHorizontalHeaderLabels(headers)

        for i, row in df.iterrows():
            # Добавление строки
            table.setRowCount(table.rowCount() + 1)

            for j in range(table.columnCount()):
                table.setItem(i, j, QTableWidgetItem(str(row[j])))

        self.ui.gridLayout_4.addWidget(table)

    def fill_table_f_df(self, df):
        table = QTableWidget()
        headers = df.columns.values.tolist()
        table.setColumnCount(len(headers))
        table.setHorizontalHeaderLabels(headers)

        for i, row in df.iterrows():
            # Добавление строки
            table.setRowCount(table.rowCount() + 1)

            for j in range(table.columnCount()):
                table.setItem(i, j, QTableWidgetItem(str(row[j])))

        self.ui.gridLayout_4.addWidget(table)
    def open_second_window(self):
        self.swin.show()
