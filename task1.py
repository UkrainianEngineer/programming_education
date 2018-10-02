first_number_to_count_digits = '12345'
second_number_to_count_digits = '611091234512'
def count_digits(str_number):
     result = 0
     for element in str_number:
          result += int(element)
     return result
print(f"First result: {count_digits(first_number_to_count_digits)} \nSecond result: {count_digits((second_number_to_count_digits))}"
