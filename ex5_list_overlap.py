a = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 90, 90]
b = [1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 90]
a_b = []

for item_a in a:
    for item_b in b:    # this is redundant and also wrong
        if item_a == item_b:
            a_b.append(item_a)

# print(a_b)

# slightly better one
ab = []
for item in a:
    if item in b:
        ab.append(item)

# print(ab)

# one line
print([item for item in set(a) if item in b])   # set() removes duplicates

print(list(set(a) & set(b)))    # list() creates a list
