"""
Counts number of lines in the file.
"""
file_name = 'textfile.txt'

def count_lines_number(file_name):
    with open(file_name) as file:
        return len(file.readlines())

print(count_lines_number(file_name))