""" This script finds the longest word in the file. """


def find_longest_word(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        file_content = f.read()

        # Remove punctuation marks
        chars_to_be_replaced = [',', '.', ';', ':', '!', '?']
        for character in chars_to_be_replaced:
            file_content = file_content.replace(character, '')

        # split file content into the words
        words = file_content.split()

        # find longest word
        longest_word = max(words, key=len)

        return longest_word


print('The longest word in the file is "{}".'.format(
        find_longest_word('task7_demo_file.txt')))
