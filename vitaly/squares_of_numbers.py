''' Calculate squared of numbers '''

def range_generator(big_number):
    num = 0
    while num < big_number:
        yield num * num
        num += 1

for square_numbers in range_generator(100000000000):
    print(square_numbers)
