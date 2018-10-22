""" This script counts the number of lines in a text file. """


def read_file_lines(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        return len(f.readlines())


print('The number of lines in file is {}.'.format(
        read_file_lines('task7_demo_file.txt')))
