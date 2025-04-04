number = int(input("Give me a number"))
divisors = []
for num in range(1, number+1): 
    if number % num == 0: 
        divisors.append(num)
print(f"These are all the divisors: {divisors}")

# Other solution: 
print(f"These are all divisors: {[x for x in range(1, number+1) if number % x == 0]}")