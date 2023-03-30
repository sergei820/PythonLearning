def find_it(seq):
    counter = 0
    for el in seq:
        for elem in seq:
            if elem == el:
                counter = counter + 1

        if counter % 2 != 0:
            result_value = el
            break
        else:
            counter = 0
    return result_value



print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))