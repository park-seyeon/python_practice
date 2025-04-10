a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
less_a = []

for num in a:
    if num < 5:
        less_a.append(num)

print(less_a)

# From SOLUTION:
print([x for x in a if x < 5])
