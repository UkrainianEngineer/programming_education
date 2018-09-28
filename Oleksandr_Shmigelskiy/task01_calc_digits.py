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
    list_of_digits = list(num)
    sumdigits = 0
    for i in list_of_digits:
        try:
            sumdigits += int(i)
        except ValueError:
            continue
    return sumdigits


print(calculate_digits(15))
print(calculate_digits(25))
print(calculate_digits('611091234512'))
print(calculate_digits('a5sd45g6'))
print(calculate_digits('areyt@ryrtjh'))
