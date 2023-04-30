from PyQt6.QtWidgets import QApplication
from MWClass import MainWindow


# Приложению нужен один (и только один) экземпляр QApplication.

app = QApplication([])
window = MainWindow()
window.show()  # Важно: окно по умолчанию скрыто.

# Запускаем цикл событий.
app.exec()