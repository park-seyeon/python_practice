import random


def list_duplicates():
    list = []
    i = 0
    while i < 10:
        list.append(random.choice(range(10)))
        i += 1
    return list


a = list_duplicates()
print(a)

# solution1: using sets

print(list(set(a)))

# solution2: using loops


def remove_duplicates(ex):
    for x in ex:
        i = ex.index(x)
        for y in ex[i+1:]:
            if x == y:
                ex.remove(y)
            else:
                continue
    return ex


print(remove_duplicates(a))
