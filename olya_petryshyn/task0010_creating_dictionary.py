def create_dict(n):
    new_dict = {i: i**2 for i in range(1, n+1)}
    return new_dict

print(create_dict(8))  # prints {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}