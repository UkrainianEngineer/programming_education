"""Calculate sum of all digits of a numer set in string.

Example:

num = ‘12345’

Your script should calculate it like: 1+2+3+4+5 = 15

num = ‘611091234512’
result = 6+1+1+0+9+1+2+3+4+6+1+2 = 36
"""


num = '611091234512'
# Set sum variable 
result = 0
# Fill text string and calculate sum 
for digit in num:
    result += int(digit)
# Print result
print(result)
    

