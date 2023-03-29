def digital_root(n):
    s = str(n)
    my_list = list(s)
    result = 0
    while len(my_list) > 1:
        result = 0
        for x in my_list:
            result += int(x)

        new_str = str(result)
        my_list = list(new_str)

        if len(my_list) == 1:
            break

    return result


# n = 132
# s = str(n)
# print(list(s))


print(digital_root(942))
