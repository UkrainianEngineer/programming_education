""" This Script is Task#3 in Programming_education course.

 The task is to calculate squares of numbers in range from
 0 to 100000000000.
 The code should be able to execute on very simple computer
 (without huge amount of virtual memory, CPU, etc.).
 Code should works under both versions of Python (2.X, 3.X).

 Script tested in Python 3.6 and Python 2.7.15.
 """


def square_large_list(list_range):  # creates generator with max_range
    i = 0
    while i < list_range:
        yield i * i  # returns squared iterator
        i += 1


max_range = 100000000000
for number in square_large_list(max_range):
    print(number)
