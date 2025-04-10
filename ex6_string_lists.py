word = input("Give me a word: ")
num = -1

for w in word:
    if w == word[num]:
        num += -1
    else:
        print("Wrong")
        exit()
print("Correct palindrome")

# using string reversal
reverse = word[::-1]  # learn: word[::-1]
if reverse == word:
    print("correct palindrome")
else:
    print("wrong")

# using definition for reversed word (adopted from SOLUTION)


def reverse(input):
    reverse = ""
    num = -1
    for w in input:
        reverse += input[num]
        num -= 1
    return reverse


print(reverse(word))
