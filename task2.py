#task 2
#from numpy import *
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
cheapest_book_price = 0
cheapest_book_name = ''
for book in books:
    if cheapest_book_price == 0 or cheapest_book_price > book['price']:
        cheapest_book_price = book['price']
        cheapest_book_name = book['name']
print('The cheapest book is: ' + cheapest_book_name + '. It costs ' + str(cheapest_book_price) + ' grn.')