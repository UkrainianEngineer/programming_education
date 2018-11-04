list_of_ints = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]

def unique_list_reversed(some_list):
    new_set = set()
    for item in some_list:
        new_set.add(item)
    new_list = list()
    for item in new_set:
        new_list.append(item)
    return new_list[::-1]

print(unique_list_reversed(list_of_ints))  # prints [120, 88, 24, 155, 12, 35]
