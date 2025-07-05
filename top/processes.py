import psutil
import time

from top import const
from top import utils


class Processes:

    MES = ' Count of process: {}'

    def __init__(self, sort_key):
        self.process_cpu_usage = []
        self.total_process = 0
        self.sort_key = sort_key
        self.font = {const.PID: '', const.NAME: '', const.TIME: '',
                     const.MEMORY: '', const.CPU: '', const.THREADS: ''}

    def prepare(self, pid, name, times, mem, cpu, thread, tittle=False):
        for key in self.font:
            if tittle is False:
                self.font[key] = ''
            elif key == self.sort_key:
                self.font[key] = const.FONT_BLUE
            else:
                self.font[key] = const.FONT_GREEN

        return (f'{self.font[const.PID]}{pid:>6}'
                f'{self.font[const.NAME]}{name:^33}'
                f'{self.font[const.TIME]}{times:^10}'
                f'{self.font[const.MEMORY]}{mem:>11}'
                f'{self.font[const.CPU]}{cpu:>7}'
                f'{self.font[const.THREADS]}{thread:>7}'
                f'{const.FONT_CANCEL}')

    def sort(self):
        self.process_cpu_usage.sort(
            key=lambda x: (x[const.key_sort[self.sort_key]],
                           x[const.key_sort[const.MEMORY]],
                           x[const.key_sort[const.CPU]]),
            reverse=True if const.key_sort[self.sort_key] > 2 else False
        )

    def get(self):
        self.process_cpu_usage = []
        list_of_process = []

        processes = psutil.pids()
        self.total_process = len(processes)

        for pid in processes:
            try:
                process = psutil.Process(pid)
                process.cpu_percent(interval=None)
                list_of_process.append(process)
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                continue

        time.sleep(3)

        for process in list_of_process:
            try:
                values = []
                if process.pid == 0:
                    continue

                values.append(process.pid)
                values.append(process.name()[:30])
                create_time = psutil.datetime.datetime.fromtimestamp(process.create_time())
                values.append(f'{create_time.strftime(const.TIME_FORMAT)}')
                values.append(process.memory_info().rss)
                values.append(process.cpu_percent(interval=None))
                values.append(process.num_threads())
                self.process_cpu_usage.append(values)
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                continue

    def show(self):
        print()
        print(self.MES.format(self.total_process))

        self.sort()
        title = self.prepare(
            const.PID.upper() + ' ', const.NAME.upper(), const.TIME.upper(),
            const.MEMORY.upper() + '  ', const.CPU.upper() + '% ',
            const.THREADS.upper(), tittle=True
        )
        print(f'{title}{" " * 8}{title}')

        for index, i in enumerate(self.process_cpu_usage):
            if index <= 27:
                data_1 = self.prepare(
                    i[0], i[1], i[2], utils.convert_bytes(i[3]), i[4], i[5]
                )
                y = self.process_cpu_usage[index + 28]
                data_2 = self.prepare(
                    y[0], y[1], y[2], utils.convert_bytes(y[3]), y[4], y[5]
                )
                print(f'{data_1}        {data_2}')
            else:
                break
