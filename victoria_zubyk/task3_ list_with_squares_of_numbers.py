import array
def get_sqr(n):
    while n != 10**11:
        yield n*n
        n += 1

for i in get_sqr(0):
    print(i)
