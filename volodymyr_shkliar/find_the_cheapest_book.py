"""
Find the cheapest book.
"""

books = [
    {
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
    }
]


def min_price(data: list) -> str:

    cheapest_book = min(data, key=lambda x: x['price'])

    return "The cheapest book is '{}'. It costs {} grn.".format(cheapest_book.get('name'), cheapest_book.get('price'))


if __name__ == '__main__':
    assert min_price(books) == "The cheapest book is 'Fluent Python'. It costs 650 grn."
