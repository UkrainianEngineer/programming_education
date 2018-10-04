"""This script should find and return the cheapest book from dictionary
in format:
    `The cheapest book is ‘Fluent Python’. It costs 650 grn.`
"""


# Initialize dictionary with books.
books = [{
        'name': 'Lord of the rings',
        'price': 700
    },
    {
        'name': 'Harry Potter',
        'price': 1300
    },
    {
        'name': 'Fluent Python',
        'price': 650
    }]

try:
    # Look for cheapest book in books.
    cheapest_book = min(books, key=lambda book: book['price'])
    # Print result.
    print('The cheapest book is ‘{0}’. It costs {1} grn.'.format(
        cheapest_book['name'],
        cheapest_book['price']
        ))
except ValueError:
    print('The book list is empty')
except NameError:
    print('The book list not found')
