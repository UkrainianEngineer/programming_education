""" This script finds the longest word in the file.
Works only with utf-8 files in 3.x and 2.x versions of Python.
Tested on Python 2.7, 3.6 and 3.7.
"""

import io
import sys


def find_longest_word(file_name):
    with io.open(file_name, 'r', encoding='utf-8') as f:

        file_content = f.read()

        # Remove punctuation marks in different Python versions.
        wrong_characters = '[],.;:!?'
        if int(sys.version[0]) >= 3:
            words = file_content.translate(str.maketrans('', '', wrong_characters))
        else:
            words = file_content.encode('utf-8').translate(None, wrong_characters)

        # Split file content into the words.
        words = words.split()

        # Find longest word.
        longest_word = max(words, key=len)

        return longest_word


print('The longest word in the file is "{}".'.format(
        find_longest_word('task7_demo_file.txt')))
