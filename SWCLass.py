from PyQt6.QtWidgets import QMainWindow, QTableWidget, QTableWidgetItem, QPushButton, QFileDialog, QCheckBox
from PyQt6.QtCore import pyqtSignal


from second_window import Ui_SecondWindow
# from MWClass import MainWindow
import pandas as pd
class SecondWindow(QMainWindow, Ui_SecondWindow):
    test_signal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.ui = Ui_SecondWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.test_signal)
        self.link = ""
        self.listT = []

        # self.ui.gridLayout.setSpacing(10)
        # self.show()
    def search_link(self):
        self.fill_table()
    def confirm_dfs(self):
        checkbox_list = self.findChildren(QCheckBox)
        for cb in checkbox_list:
            if cb.isChecked():
                self.listT.append(cb.text())
        self.close()
    def fill_table(self):
        self.link = self.ui.textEdit.toPlainText()
        # print(self.link)
        self.dfw = pd.read_html(self.link)
        k = 0
        for df in self.dfw:
            table = QTableWidget()
            check = QCheckBox(f"{k}")
            k = k+1
            if k > 4:
                break
            headers = df.columns.values.tolist()
            table.setColumnCount(len(headers))
            table.setHorizontalHeaderLabels(headers)

            for i, row in df.iterrows():
                # Добавление строки
                table.setRowCount(table.rowCount() + 1)

                for j in range(table.columnCount()):
                    table.setItem(i, j, QTableWidgetItem(str(row[j])))
            # table.setMinimumSize(600, 100)
            self.ui.gridLayout.addWidget(check, k, 0)
            self.ui.gridLayout.addWidget(table, k, 1)


