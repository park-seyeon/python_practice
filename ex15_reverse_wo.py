def reverse_wo():

    word = input("Give me a sentence: ")
    list_word = word.split()
    i = -1
    list_reverse = []
    for x in list_word:
        list_reverse.append(list_word[i])
        i += -1
    reverse = " ".join(list_reverse)

    return reverse


print(reverse_wo())

# other codes from SOLUTION:

# " ".join(word.split()[::-1])

# y = word.split()
# " ".join (reversed(y))
# OR
# y.reverse()
# " ".join(y)
