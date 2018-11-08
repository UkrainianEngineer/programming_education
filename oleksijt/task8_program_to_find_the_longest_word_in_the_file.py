""" This script finds the longest word in the file. """


def find_longest_word(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:

        # Remove punctuation marks.
        file_content = f.read().translate(str.maketrans('', '', '[],.;:!?'))

        # Split file content into the words.
        words = file_content.split()

        # Find longest word.
        longest_word = max(words, key=len)

        return longest_word


print('The longest word in the file is "{}".'.format(
        find_longest_word('task7_demo_file.txt')))
