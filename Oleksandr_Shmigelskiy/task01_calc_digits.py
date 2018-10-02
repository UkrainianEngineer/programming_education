"""
This function calculate sum of all digits of a number.
A number can be represented in integer or string type.
Value of the letters or any blank symbol equated to zero.

Example:
num = '12345'
the function calculate it like: 1+2+3+4+5 = 15
num = 'a5sd45g6'
result = 5+4+5+6 = 20
"""


def calculate_digits(num):
    if type(num) is int:
        num = str(num)
    sum_of_digits = 0
    for digit in num:
        try:
            sum_of_digits += int(digit)
        except ValueError:
            continue
    return sum_of_digits


print(calculate_digits(15))
print(calculate_digits(25))
print(calculate_digits('611091234512'))
print(calculate_digits('a5sd45g6'))
print(calculate_digits('arey\nt@ry rtjh'))
print(calculate_digits(''))
