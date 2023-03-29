def array_diff(a, b):
    print(a)
    print(b)
    for el in b:
        print("el in b: ")
        print(el)
        for el_in_a in a:
            print("el_in_a in a: ")
            print(el_in_a)
            if el_in_a == el:
                list(a).remove(el_in_a)
                print("List a: ")
                print(a)

    return a

print(array_diff([1, 2, 2, 2, 3], [2]))