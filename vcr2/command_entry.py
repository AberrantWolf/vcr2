import asyncio
from typing import Dict
from PySide6.QtCore import Slot, Signal, QObject


class CommandOption:
    def __init__(self, name, value):
        self.name = name
        self.value = value


class CommandEntry(QObject):
    command_output = Signal(str)

    def __init__(self, config: Dict):
        super().__init__()
        self._command = config['command']

        self._name = config['name'] if 'name' in config else config['command']

        self._options = []

        if 'options' in config:
            for opt in config['options']:
                self._options.append(CommandOption(opt['name'], opt['value']))
    
    def name(self) -> str:
        return self._name
    
    async def _do_execute_async(self):
        proc = await asyncio.create_subprocess_shell(self._command, stdout=asyncio.subprocess.PIPE)

        data = await proc.stdout.readline()
        while len(data) > 0:
            line = data.decode('utf-8').rstrip()
            self.command_output.emit(line)
            data = await proc.stdout.readline()
        
        self.command_output.emit(f"DONE: {proc.returncode}")
    
    @Slot()
    def do_execute(self):
        asyncio.run(self._do_execute_async())
