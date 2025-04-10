import random

list = random.sample(range(1, 100), 10)

print(list)
print([list[0], list[-1]])

# using def


def end_list(item):
    return [item[0], item[-1]]


print(end_list(list))
