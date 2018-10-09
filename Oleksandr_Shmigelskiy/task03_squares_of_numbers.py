from datetime import datetime
start_time = datetime.now()

big_list = range(1000000)
big_list_square = (n**2 for n in big_list)

for n in big_list_square:
    print(n)

end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))