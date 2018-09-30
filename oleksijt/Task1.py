##Calculate sum of all digits of a numer set in string.
##
##Example:
##
##num = ‘12345’
##
##Your script should calculate it like: 1+2+3+4+5 = 15
##
##num = ‘611091234512’
##result = 6+1+1+0+9+1+2+3+4+6+1+2 = 36

num = '611091234512'

##set sum variable 
result = 0

##fill text string and calculate sum 
for digit in num:
    result += int(digit)
    
##print result
print (result)
    

