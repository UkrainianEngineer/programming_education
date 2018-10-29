"""
Reading last n lines from the file.
"""
def read_n_last_lines(file_name, n):
    with open(file_name) as file:
        for line in (file.readlines()[-n:]):
            print(line, end='')


file_name = "textfile.txt"
n = 3
read_n_last_lines(file_name, n)  # prints 3 last lines of the file.