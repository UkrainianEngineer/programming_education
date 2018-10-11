'''Find the cheapest book in list and return formatted string'''
 books = [
    {
        'name': 'Lord of the rings',
        'price': 700
    },
    {
        'name': 'Harry Potter',
        'price': 1200
    },
    {
        'name': 'Fluent Python',
        'price': 555
    }
]
cheapest_book = min(books, key=lambda x:x['price'])
print("The cheapest book is ‘{0}’. It costs {1} grn." . format(cheapest_book['name'], cheapest_book['price']))
