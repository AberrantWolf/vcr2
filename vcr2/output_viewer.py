from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QTextEdit, QVBoxLayout

class OutputViewer(QWidget):
    def __init__(self, parent: QWidget | None = None, f: Qt.WindowType = None) -> None:
        super().__init__(parent)

        self._text_view = QTextEdit()
        self._text_view.setReadOnly(True)
        self._text_view.setFontFamily('consolas')

        self._layout = QVBoxLayout(self)
        self._layout.addWidget(self._text_view)

    def append_line(self, line: str):
        self._text_view.insertPlainText(f"{line}\n")