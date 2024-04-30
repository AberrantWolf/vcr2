import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QLabel

from .app_window import VcrAppWindow


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app_window = VcrAppWindow()
    app_window.show()
    sys.exit(app.exec_())