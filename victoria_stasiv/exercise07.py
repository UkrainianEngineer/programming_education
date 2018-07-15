books = [
    {
        'name': 'Lord of the rings',
        'price' : 700
    },
    {
        'name' : 'Harry Potter',
        'price' : 1300
    },
    {
        'name' : 'Fluent Python',
        'price' : 650
    }
]
arr= []
sentence = "The cheapest book is 'Fluent Python'. It costs"
for dictionary in books:
    #print(dictionary['price'])
    arr.append(dictionary['price'])
print(sentence + " " + str(min(arr)) +  " grn ")

