
def get_cheapest_book(bookslist):
    return min(bookslist, key=lambda x: x['price'])

books = [
    {'name': 'Lord of the rings', 'price': 700},
    {'name': 'Harry Potter', 'price': 1300},
    {'name': 'Fluent Python', 'price': 650},
    {'name': 'War of thrones', 'price': 655}
]
print(f"The cheapest book is '{get_cheapest_book(books).get('name')}'. "
      f"It costs {get_cheapest_book(books).get('price')} grn.")
