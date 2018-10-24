"""Script defines and demonstrates custom class for exceptions.
 Exceptions raise when opened file is empty or it contents more
 then one longest word"""


class CustomError(Exception):
    pass


class EmptyFileError(CustomError):
    pass


class MoreThenOneWordError(CustomError):
    pass


def find_longest_word(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        file_content = f.read()

        # Remove punctuation marks
        chars_to_be_replaced = [',', '.', ';', ':', '!', '?']
        for character in chars_to_be_replaced:
            file_content = file_content.replace(character, '')

            # Check if  the file is empty
            if len(file_content) <= 1:
                raise EmptyFileError

        # Split file content into the words
        words = file_content.split()

        # Find longest word
        longest_word = max(words, key=len)

        # check the quantity of the longest words
        longest_words = 0
        for word in words:
            if len(word) == len(longest_word):
                longest_words += 1
        if longest_words > 1:
            raise MoreThenOneWordError

    return longest_word


# Prints longest word
print('The longest word in the file is "{}".'.format(
    find_longest_word('task7_demo_file.txt')))


# Raises EmptyFileError
try:
    print('The longest word in the file is "{}".'.format(
        find_longest_word('task12_demo_file_empty.txt')))
except EmptyFileError:
    print('Error: The file is empty.')

# Raises MoreThenOneWordError
try:
    print('The longest word in the file is "{}".'.format(
    find_longest_word('task12_demo_file_mto.txt')))
except MoreThenOneWordError:
    print('Error: There is more then one longest word.')
