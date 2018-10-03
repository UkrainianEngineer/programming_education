"""
Calculate squares of numbers.
"""


gen_exp = (x ** 2 for x in range(100000000000))


if __name__ == '__main__':
    for num in gen_exp:
        print(num)
