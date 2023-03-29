def spin_words(sentence):
    words_list = sentence.split()
    for i in range(len(words_list)):
        if len(words_list[i]) >= 5:
            words_list[i] = words_list[i][::-1]


    # Your code goes here
    return ' '.join(map(str, words_list))


print(spin_words( "Hey fellow warriors" ))
assert spin_words( "Hey fellow warriors" ) == "Hey wollef sroirraw"
assert spin_words("This sentence is a sentence") == "This ecnetnes is a ecnetnes"