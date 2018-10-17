import my_module
first_number_to_count_digits = '12345'
second_number_to_count_digits = '611091234512'
"""
Calculating the sum of digits in a string number.
"""
# def digit_sum(str_number):
#      result = 0
#      for i in str_number:
#           result += int(i)
#      return result
# print(f"First result: {digit_sum(first_number_to_count_digits)} \nSecond result: {digit_sum(second_number_to_count_digits)}")
print(f'First result: {sum(int(digit) for digit in first_number_to_count_digits)}')
print(f'Second result: {sum(int(digit) for digit in second_number_to_count_digits)}')
print(my_module.__doc__)