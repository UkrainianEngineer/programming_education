"""
Calculating squares of numbers in a large list without memory errors, that runs on Python 2.X, 3.X.
"""
list_range = 100000000000

def generate_squares_of_numbers(n):
    i = 0
    while i < list_range:
        yield i ** 2
        i += 1

for number in generate_squares_of_numbers(list_range):
    print(number)
