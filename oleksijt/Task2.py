##2. Find the cheapest book
##
##books = [
##    {
##        ‘name’: ‘Lord of the rings’,
##        ‘price’: 700
##    },
##    {
##        ‘name’: ‘Harry Potter’,
##        ‘price’: 1300
##    },
##    {
##        ‘name’: ‘Fluent Python’,
##        ‘price’: 650
##    }
##]
##
##Your script should return: `The cheapest book is ‘Fluent Python’. It costs 650 grn.`

#fill dict
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

#set vars
chbookprice = 0

#look for cheapest book price in books and set vars
for book in books:
    bookprice = book ['price']
    if chbookprice == 0 or chbookprice > bookprice:
        chbookname = book ['name']
        chbookprice = bookprice

#print result       
print ('The cheapest book is ‘' + chbookname +'’. It costs ' + str(chbookprice) + ' grn.')
