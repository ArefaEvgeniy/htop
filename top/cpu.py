import psutil

from top import const
from top import utils


class CPU:

    MES = ' Count core of CPU: {}   Current freq: {}   Max freq: {}'

    def __init__(self):
        self.percent_per_core = {}
        self.percent_cpu = 0
        self.cpu_count_core = 0
        self.cpu_freq_current = 0
        self.cpu_freq_max = 0

    def get(self):
        cpu_freq = psutil.cpu_freq()
        self.cpu_freq_current = cpu_freq.current
        self.cpu_freq_max = cpu_freq.max
        self.cpu_count_core = psutil.cpu_count()
        self.percent_cpu = psutil.cpu_percent(interval=1)
        cpu_percent_per_core = psutil.cpu_percent(percpu=True, interval=1)
        for i, percentage in enumerate(cpu_percent_per_core):
            self.percent_per_core.update({i: percentage})

    def show(self):
        print()
        text = self.MES.format(self.cpu_count_core, self.cpu_freq_current,
                               self.cpu_freq_max)
        data_1 = f'{const.TEXT_BLUE}{text}{const.TEXT_WHITE}'
        data_2 = utils.create_band('CPU', self.percent_cpu, f'{self.percent_cpu}%')
        print(f'{data_1:<102}{data_2}')

        for i in range(0, len(self.percent_per_core), 2):
            value = self.percent_per_core.get(i)
            print(utils.create_band(i, value, f'{value}%'), end=' '*20)
            if self.percent_per_core.get(i+1) is not None:
                value = self.percent_per_core.get(i+1)
                print(utils.create_band(i+1, value, f'{value}%'))
            else:
                print()
