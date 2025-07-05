import os
import argparse

from top import const
from top.cpu import CPU
from top.memory import Memory
from top.processes import Processes


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', metavar='--sort', type=str,
                        help='Name of item for sort')
    return parser.parse_args()


def clear_monitor():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def main():
    parser = create_parser()
    sort_key = parser.s if parser.s in const.key_sort else const.PID
    indicators = [CPU(), Memory(), Processes(sort_key)]
    while True:
        for indicator in indicators:
            indicator.get()
        clear_monitor()
        for indicator in indicators:
            indicator.show()


if __name__ == '__main__':
    main()
