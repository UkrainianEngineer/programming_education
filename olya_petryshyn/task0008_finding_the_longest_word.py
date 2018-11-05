"""
Finding the longest word in the file.
"""
import string
file_name = 'textfile.txt'

def the_longest_word(file_name):
    with open(file_name, 'r') as file:
        string_text = file.read().replace('\n', ' ')
    for item in string.punctuation:
        string_text = string_text.replace(item, '')
    list_text = string_text.split()
    list_text.sort(key=lambda x: len(x))
    return list_text[-1]


print(the_longest_word(file_name))