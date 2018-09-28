"""
 Find the cheapest book
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

Your script should return: `The cheapest book is ‘Fluent Python’. It costs 650 grn.`

"""

def get_cheapest_book(bookslist):
	cheapest_book = bookslist[0]
	for book in bookslist[1:]:
		if book['price'] < cheapest_book['price']:
			cheapest_book = book

	return 'The cheapest book is "{0}". It costs {1} grn.'\
		.format(cheapest_book['name'], cheapest_book['price'])


books = [
	{'name': 'Lord of the rings', 'price': 700},
    {'name': 'Harry Potter', 'price': 1300},
    {'name': 'Fluent Python', 'price': 650},
	{'name': 'War of thrones', 'price': 655}
]
print(get_cheapest_book(books))
