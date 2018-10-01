"""2. Find the cheapest book

books = [
    {
        ‘name’: ‘Lord of the rings’,
        ‘price’: 700
    },
    {
        ‘name’: ‘Harry Potter’,
        ‘price’: 1300
    },
    {
        ‘name’: ‘Fluent Python’,
        ‘price’: 650
    }
]

Your script should return:
    `The cheapest book is ‘Fluent Python’. It costs 650 grn.`
"""


# Fill dict
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
    # Set first book as cheapest
    cheapest_book = books[0]
    # Look for cheapest bookin books
    for book in books:
        if cheapest_book['price'] > book['price']:
            cheapest_book = book
    # Print result       
    print('The cheapest book is ‘' + cheapest_book['name']
          + '’. It costs ' + str(cheapest_book['price']) + ' grn.')
except:
    print('No books found')
