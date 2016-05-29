def int_to_unit(length, ndigits=1):
    """Converts an integer to a data storage unit.

    >>> int_to_unit(130)
    '130.0B'

    >>> int_to_unit(1300000)
    '1.2MB'

    >>> int_to_unit(1300000, 2)
    '1.24MB'
    """

    units = ['B', 'KB', 'MB', 'GB', 'TB', 'PB',
             'EB', 'ZB', 'YB', 'BB', 'NB', 'DB']
    units_index = 0
    while length > 1024 and units_index < 11:
        units_index += 1
        length = length / 1024
    s = '{:.%df}{}' % ndigits
    return s.format(length, units[units_index])

if __name__ == "__main__":
    import doctest
    doctest.testmod()
