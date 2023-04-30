from PyQt6.QtWidgets import QMainWindow
from second_window import Ui_SecondWindow
import pandas as pd
class SecondWindow(QMainWindow, Ui_SecondWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_SecondWindow()
        self.ui.setupUi(self)
        self.show()
        self.link = ""
    def search_link(self):
        self.link = self.ui.textEdit.toPlainText()
        dfw = pd.read_html(self.link)
        print(len(dfw))




