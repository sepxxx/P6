from PyQt6.QtWidgets import QMainWindow, QFileDialog, QTableWidget, QTableWidgetItem, QCalendarWidget
from myui import Ui_MainWindow
from SWCLass import SecondWindow
import pandas as pd
import rass
import week
import checkdate
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
        self.exist_date = 0
        self.date_column_name = ""
        self.show()
    def selectFile(self):
        self.fill_table_ff(QFileDialog.getOpenFileName()[0])
    def print(self):
        for i in self.swin.listT:
            self.fill_table_f_df(self.swin.dfw[int(i)])
        self.df = self.swin.dfw[int(self.swin.listT[0])]
        #КАК только передали какой df отображать со второго окна
        #сразу его проверяем на наличие даты
        #если она есть, то добавим 2 колонки для выбора дат
        self.exist_date, self.date_column_name = checkdate.check_date(self.df)
        if self.exist_date:
            self.ui.gridLayout_4.addWidget(QCalendarWidget())
            self.ui.gridLayout_4.addWidget(QCalendarWidget())


    def plot(self):
        #данные для фильтрации берем из полей и комбобоксов
        sign2 = self.ui.comboBox_2.currentText()
        sign1 = self.ui.comboBox.currentText()
        head_1 = self.ui.comboBox_3.currentText()
        head_2 = self.ui.comboBox_4.currentText()
        v2 = self.ui.lineEdit.text()
        v1 = self.ui.lineEdit_2.text()
        #даты парсим из календарей
        if self.exist_date:
            calendars_list = self.findChildren(QCalendarWidget)
            dates = []
            for i in calendars_list:
                dates.append(i.selectedDate().toString('yyyy-MM-dd'))
            self.df = self.df[(self.df[f'{self.date_column_name}'] > dates[0]) & (self.df[f'{self.date_column_name}'] < dates[1])]

            filtered = self.df.copy()
        if head_1 != self.date_column_name:
            filtered = self.df.query(f"{head_1}{sign1}{v1}")
        if head_2 != self.date_column_name:
            filtered = filtered.query(f"{head_2}{sign2}{v2}")
        rass.rasse(filtered, head_1, head_2)

        if self.exist_date and (head_1 == self.date_column_name or head_2 == self.date_column_name):
            week.week(filtered, head_1, head_2, self.date_column_name)
    def fill_table_ff(self, currentData):
        df = pd.read_csv(currentData)
        self.df = df
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
        self.exist_date, self.date_column_name = checkdate.check_date(self.df)
        if self.exist_date:
            self.ui.gridLayout_4.addWidget(QCalendarWidget())
            self.ui.gridLayout_4.addWidget(QCalendarWidget())

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
