""" This script reads last n lines of a file. """


def read_file_lines(file_name, num_lines):
    with open(file_name, 'r', encoding='utf-8') as f:
        return f.readlines()[-num_lines:]


print(read_file_lines('task7_demo_file.txt', 4))

