""" This script reads last n lines of a file. """


def read_last_file_lines(file_name, num_lines):
    with open(file_name, 'r', encoding='utf-8') as f:
        return list(f)[-num_lines:]


print(read_last_file_lines('task7_demo_file.txt', 4))
