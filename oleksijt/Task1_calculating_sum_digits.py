"""Script should calculate sum of all digits of a numer set in string.
Example:
num = ‘611091234512’
result = 6+1+1+0+9+1+2+3+4+6+1+2 = 36
"""


num = '611091234512'
# Calculate result 
result = sum(int(digit) for digit in num)
# Print result
print(result)
    

