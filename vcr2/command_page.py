
from PySide6.QtCore import Qt, Slot
from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton

from .command_entry import CommandEntry
from .output_viewer import OutputViewer


class CommandPage(QWidget):
    def __init__(self, parent: QWidget | None, command: CommandEntry) -> None:
        super().__init__(parent)

        self._command = command
        self._command.command_output.connect(self.on_output)

        self._label = QLabel(self._command.name())
        self._execute_button = QPushButton("Execute!")
        self._output_view = OutputViewer()

        self._execute_button.clicked.connect(self._command.do_execute)

        self._execute_button_row = QHBoxLayout()
        self._execute_button_row.addStretch()
        self._execute_button_row.addWidget(self._execute_button)

        self._vbox_layout = QVBoxLayout(self)
        self._vbox_layout.addWidget(self._label)
        self._vbox_layout.addWidget(self._output_view)
        self._vbox_layout.addLayout(self._execute_button_row)

    @Slot(str)
    def on_output(self, line: str):
        self._output_view.append_line(line)
