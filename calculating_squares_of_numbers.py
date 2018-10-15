"""
Calculating squares of numbers in a large list without memory errors.
"""
squared_list_generator = (x*x for x in range(100000000000))
for number in squared_list_generator:
    print(number)