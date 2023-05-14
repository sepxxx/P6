from PyQt6.QtWidgets import QMainWindow, QFileDialog, QTableWidget, QTableWidgetItem
from myui import Ui_MainWindow
from SWCLass import SecondWindow
import pandas as pd
import rass
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.swin = SecondWindow()
        self.swin.test_signal.connect(self.print)
        self.ui.pushButton.clicked.connect(self.plot)
        self.ui.comboBox.addItems([">", ">=", "<", "<=", "=="])
        self.ui.comboBox_2.addItems([">", ">=", "<", "<=", "=="])

        self.show()
    def selectFile(self):
        self.fill_table_ff(QFileDialog.getOpenFileName()[0])
    def print(self):
        for i in self.swin.listT:
            self.fill_table_f_df(self.swin.dfw[int(i)])
        self.df = self.swin.dfw[int(self.swin.listT[0])]
    def plot(self):

        #данные для фильтрации
        sign2 = self.ui.comboBox_2.currentText()
        sign1 = self.ui.comboBox.currentText()
        head_1 = self.ui.comboBox_3.currentText()
        head_2 = self.ui.comboBox_4.currentText()
        v2 = self.ui.lineEdit.text()
        v1 = self.ui.lineEdit_2.text()

        filtered = self.df.query(f"{head_1}{sign1}{v1}")
        filtered = filtered.query(f"{head_2}{sign2}{v2}")
        rass.rasse(filtered, head_1, head_2)

        print(self.df.info())
        # print(sign1, sign2, head_1, head_2, v1, v2)

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
        self.ui.comboBox_3.addItems(headers)
        self.ui.comboBox_4.addItems(headers)

        #проверить есть ли даты в df
        #если есть, добавить в главное окно выбор для дат

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
        self.ui.comboBox_3.addItems(headers)
        self.ui.comboBox_4.addItems(headers)
    def open_second_window(self):
        self.swin.show()
