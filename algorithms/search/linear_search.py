
my_list = [-2, -6, 1, 7, 10, -3, 6, 9, 12, 3]


def linear_search(my_list, element):
    my_list.append(element)
    i = 0
    while my_list[i] != element:
        i += 1
    my_list.pop()
    if i != len(my_list):
        return i
    return 'None'

print(linear_search(my_list, 100))

