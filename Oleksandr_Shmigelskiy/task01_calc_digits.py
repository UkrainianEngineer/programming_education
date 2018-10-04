
def calculate_digits(num):
    """
    This function calculate sum of all digits of a number.
    :param num: str
    :return: int
    
    >>> calculate_digits('15')
    6
    >>> print(calculate_digits('25'))
    7
    >>> calculate_digits('')
    0
    >>> calculate_digits('611091234512')
    35
    """

    return sum(int(digit) for digit in num)


if __name__ == '__main__':
    import doctest
    doctest.testmod()