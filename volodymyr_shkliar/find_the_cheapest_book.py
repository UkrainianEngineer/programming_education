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
    data.sort(key=lambda x: x['price'])

    return "The cheapest book is '{}'. It costs {} grn.".format(data[0].get('name'), data[0].get('price'))


if __name__ == '__main__':
    assert min_price(books) == "The cheapest book is 'Fluent Python'. It costs 650 grn."
