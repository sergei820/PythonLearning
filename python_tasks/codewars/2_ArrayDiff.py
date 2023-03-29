def array_diff(a, b):
    result_list = []
    for element in a:
        if element not in b:
            result_list.append(element)
    return result_list

print(array_diff([1, 2, 2, 2, 3], [2]))