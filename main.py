from PyQt6.QtWidgets import QApplication
from MWClass import MainWindow


# Приложению нужен один (и только один) экземпляр QApplication.

app = QApplication([])
window = MainWindow()
window.show()  # Важно: окно по умолчанию скрыто.

# Запускаем цикл событий.
app.exec()
# pyuic6 -o second_window.py -x sw_test.ui
#pyuic6 -o second_window.py -x second_window.ui
# pyuic6 -o myui.py -x myui.ui