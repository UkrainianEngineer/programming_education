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


#get string
num = '611091234512'

##set text part of result 
resulttext = 'result = '

##set sum variable 
resultsum = 0

##fill text string and calculate sum 
for i in range (0, len(num)):
    resultsum = resultsum + int(num[i])
    resulttext = resulttext + num[i]
    if i < int(len(num)-1) :
              resulttext = resulttext + '+'

##print result
print (resulttext, '=', resultsum)
    

