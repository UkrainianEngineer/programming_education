# task 1
num = '12345'
num1 = '611091234512'
def add_integers(str_number):
     result = 0
     for i in str_number:
          result += int(i)
     return result
print('First result: ' + str(add_integers(num)) + '\nSecond result: ' + str(add_integers(num1)))