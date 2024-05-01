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

import sys
from typing import Dict
import yaml
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QLabel

from .command_entry import CommandEntry
from .app_window import VcrAppWindow


# Load files better...
def load_vcr_config() -> Dict:
    with open("test.vcr", 'r') as vcr_file:
        vcr_configs = yaml.safe_load_all(vcr_file)

        commands = []

        for cfg in vcr_configs:
            command = CommandEntry(cfg)
            commands.append(command)

        return commands

vcr_configs = load_vcr_config()

app = QApplication(sys.argv)
app.setStyle('Fusion')
app_window = VcrAppWindow(vcr_configs)
app_window.show()
sys.exit(app.exec_())
