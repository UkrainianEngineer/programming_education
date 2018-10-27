""" Script returns list without duplicates in original order. """


def remove_duplicates(my_list):
    new_list = []
    for element in my_list:
        if element not in new_list:
            new_list.append(element)
    return new_list


print(remove_duplicates([12, 24, 35, 24, 88, 120, 155, 88, 120, 155]))
