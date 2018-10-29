"""
Reading last n lines from the file.
"""
def read_n_last_lines(file_name, n):
    last_n_lines = ""
    with open(file_name) as file:
        text = file.readlines()
        for line in text[-n:]:
            last_n_lines += line
        return last_n_lines


file_name = "textfile.txt"
n = 3
print(read_n_last_lines(file_name, n)) # prints 3 last lines of the file.