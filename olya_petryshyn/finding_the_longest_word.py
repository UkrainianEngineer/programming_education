"""
Finding the longest word in the file.
"""
import string
file_name = 'textfile.txt'

def longest_word(file_name):
    with open(file_name, 'r') as file:
        string_text = file.read().replace('\n', ' ')
    list_text = string_text.split()
    list_text = [''.join(character for character in word if character not in string.punctuation) for word in list_text]
    list_text.sort(key=lambda x: len(x))
    return list_text[-1]

print(longest_word(file_name))