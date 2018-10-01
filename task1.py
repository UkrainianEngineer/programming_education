first_number_to_count_digits = '12345'
second_number_to_count_digits = '611091234512'
def add_integers(str_number):
     result = 0
     for i in str_number:
          result += int(i)
     return result
print('First result: ' + str(add_integers(first_number_to_count_digits)) + '\nSecond result: ' + str(add_integers(second_number_to_count_digits)))
