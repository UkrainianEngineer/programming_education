"""
Finding the cheapest book in list of dictionaries.

"""
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
cheapest_book = min(books, key=lambda x: x['price'])
print(f'The cheapest book is: {cheapest_book["name"]}. It costs: {cheapest_book["price"]} grn.')