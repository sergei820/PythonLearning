def maskify(cc):
    masked = cc
    if(len(cc) > 4):
        masked = '#' * (len(cc) - 4) + cc[-4:]
    return masked



print(maskify("4556364607935616"))

# maskify("4556364607935616") == "############5616"
# maskify(     "64607935616") ==      "#######5616"
# maskify(               "1") ==                "1"
# maskify(                "") ==                 ""