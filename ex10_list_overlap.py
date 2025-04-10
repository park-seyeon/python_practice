import random
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

print([item for item in set(a) if item in b])

# using random set

lista = random.sample(range(1, 100), 14)
listb = random.sample(range(1, 100), 20)

print(lista)
print(listb)

overlap_ab = [item for item in lista if item in listb]

print(overlap_ab)
