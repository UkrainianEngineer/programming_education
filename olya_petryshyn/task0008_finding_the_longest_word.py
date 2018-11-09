"""
Finding the longest word in the file.
"""
import string
file_name = 'textfile.txt'


def the_longest_word(file_name):
    with open(file_name, 'r') as file:
        string_text = file.read().replace('\n', ' ')
    string_text = string_text.translate(None, string.punctuation)
    list_text = string_text.split()
    return max(list_text, key=len)


print(the_longest_word(file_name))
