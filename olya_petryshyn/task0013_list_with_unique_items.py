"""
Getting rid of repeated items in a list and printing it reversed.
"""
list_of_ints = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]

def unique_list_reversed(some_list):
    return list(set(some_list))[::-1]

print(unique_list_reversed(list_of_ints))  # prints [155, 120, 24, 88, 12, 35]
