'''3. Calculate squares of numers

You have a list of numbers from 0 to 100000000000:
0, 1, 2, …, 99999999999

Please create a new list with squares of numbers from previous list.
Your new list should looks like:
0*0, 1*1, 2*2, 3*3, 4*4, …,  99999999999*99999999999

Plese print values from the second list.

P.S. This task might look super easy, but there are a few cases. I guess, you’ll find them very quickly.
Your code should be able to execute on very simple computer(without huge amount of virtual memory, CPU, etc.)
Your code should works under both versions of Python (2.X, 3.X)
'''


def quad_large_list(max_range):  # creates generator with max_range????
    for num in range(0, max_range):
        yield num*num  # returns quaded iterator


max_range = 1000000
for number in quad_large_list(max_range):
    print(number)


# print(number for number in quad_large_list(1000))  # prints quaded iterators


