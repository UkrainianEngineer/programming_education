def read_file_lines(file_name, nlines)
    with open(file_name, 'r') as f:
        file_content = f.readlines()
        return len(file_content)
print(read_file_lines(file_name, nlines))
