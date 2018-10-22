""" This script reads last n lines of a file. """


def read_file_lines(file_name, num_lines):
    with open(file_name, 'r', encoding='utf-8') as f:
        file_lines = f.readlines()
        return file_lines[len(file_lines) - num_lines:]


for lines in read_file_lines('task7_demo_file.txt', 4):
    print(lines.strip("\n"))

