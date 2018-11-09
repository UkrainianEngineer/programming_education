
books = [ {'name': 'Lord of the rings','price': 700},
          {'name': 'Harry Potter','price': 1300},
          {'name': 'Fluent Python','price': 650}]

val=[]

for elem in books:
    for key,value in elem.items():
        if key=='price':
            val.append(value)

m=min(val)

for elem in books:
    if elem['price'] == m:
        print ("The cheapest book is" , elem['name'] , "It costs",  m)




