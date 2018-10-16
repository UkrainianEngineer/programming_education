"""
Calculate sum of all digits of a number set in string.
"""


def sum_of_digits(numbers: str) -> int:
    return sum(int(n) for n in numbers)


if __name__ == '__main__':
    assert sum_of_digits('12345') == 15
    assert sum_of_digits('611091234512') == 35
