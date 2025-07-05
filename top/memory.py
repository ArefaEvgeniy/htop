import psutil

from top import utils


class Memory:

    MES = ' Used memory: {}  Total memory: {}'

    def __init__(self):
        self.memory_total = 0
        self.memory_used = 0

    def get(self):
        memory = psutil.virtual_memory()
        self.memory_total = memory.total
        self.memory_used = memory.used

    def show(self):
        present = round(self.memory_used / self.memory_total * 100, 1)
        print(utils.create_band('Mem', present, f'{present}%'), end=' '*20)
        print(self.MES.format(utils.convert_bytes(self.memory_used),
                              utils.convert_bytes(self.memory_total)))
