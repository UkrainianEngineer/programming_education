list_of_ints = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]

def unique_list_reversed(some_list):
    new_set = set()
    for item in some_list:
        new_set.add(item)
    return list(new_set)[::-1]

print(unique_list_reversed(list_of_ints))  # prints [155, 120, 24, 88, 12, 35]
