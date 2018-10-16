"""
Сalculating the sum of digits in a string number.
"""
first_number_to_count_digits = '12345'
second_number_to_count_digits = '611091234512'
print(f'First result: {sum(int(digit) for digit in first_number_to_count_digits)}')
print(f'Second result: {sum(int(digit) for digit in second_number_to_count_digits)}')
