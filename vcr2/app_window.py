# Copyright 2024 Scott Harper
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from PySide6 import QtCore
from PySide6.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout


class VcrAppWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("VCR2 -- We Python Nao")

        self.button: QPushButton = QPushButton("Click Plz")
        self.text_label: QLabel = QLabel("...text goes here...")

        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.text_label)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.on_button_pressed)
    
    @QtCore.Slot()
    def on_button_pressed(self):
        self.text_label.setText("thank you")
