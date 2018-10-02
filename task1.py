first_number_to_count_digits = '12345'
second_number_to_count_digits = '611091234512'
def digit_sum(str_number):
     result = 0
     for element in str_number:
          result += int(element)
     return result
print(f"First result: {digit_sum(first_number_to_count_digits)} \nSecond result: {digit_sum((second_number_to_count_digits))}"
