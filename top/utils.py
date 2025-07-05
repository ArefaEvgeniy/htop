from top import const


def create_band(prefix, percent, suffix):
    band = f'{const.TEXT_BLUE}{prefix:>4}'
    band += f'{const.TEXT_GRAY}['
    for i in range(50):
        color = const.TEXT_GREEN
        if i >= 25:
            color = const.TEXT_YELLOW if i < 40 else const.TEXT_RED
        if percent / 2 > i:
            band += f'{color}|'
        else:
            band += ' '
    band += f'{const.TEXT_GRAY}]'
    band += f'{const.TEXT_BLUE}{suffix:<6}{const.FONT_CANCEL}'

    return band


def convert_bytes(value):
    if value < 1024 ** 2:
        divider, suffix = 1024, 'Kb'
    elif value < 1024 ** 3:
        divider, suffix = 1024 ** 2, 'Mb'
    elif value < 1024 ** 4:
        divider, suffix = 1024 ** 3, 'Gb'
    else:
        divider, suffix = 1024 ** 4, 'Tb'

    return f'{round(value/divider, 2)} {suffix}'
