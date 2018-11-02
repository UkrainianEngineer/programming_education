"""
Reading last n lines from the file.
"""
def read_n_last_lines(file_name, n):
    with open(file_name) as file:
        text = file.readlines()
        return text[-n:]


file_name = "textfile.txt"
n = 3
last_n_lines = "".join(read_n_last_lines(file_name, n))
print(last_n_lines)  # prints 3 last lines of the file.