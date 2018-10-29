"""
Counts number of lines in the file.
"""
file_name = 'textfile.txt'

def count_lines_number(file_name):
    with open(file_name) as file:
        num_lines = sum(1 for line in file)
    return num_lines

print(count_lines_number(file_name))