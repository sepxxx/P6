from PyQt6.QtWidgets import QMainWindow, QFileDialog, QTableWidget, QTableWidgetItem
from myui import Ui_MainWindow
from SWCLass import SecondWindow
import pandas as pd

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()
    def selectFile(self):
        self.fill_table(QFileDialog.getOpenFileName()[0])
    def fill_table(self, currentData):
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

    def open_second_window(self):
        self.swin = SecondWindow()
        self.swin.show()
