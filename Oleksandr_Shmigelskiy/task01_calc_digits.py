"""
Task #1

Calculate sum of all digits of a number set in string.
Example:
num = ‘12345’
Your script should calculate it like: 1+2+3+4+5 = 15
num = ‘611091234512’
result = 6+1+1+0+9+1+2+3+4+5+1+2 = 35
"""


def calculate_digits(num):
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
print(calculate_digits('areyt@ryrtjh'))
print(calculate_digits(''))
