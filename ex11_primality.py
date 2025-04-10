# Function:
# def get_integer():
# ## def get_integer(help_text): (reusable)
# ## def get_integer(help_text="Give me a number: "): (default argument)
#   return int(input("Give me a number: "))     ## return int(input(help_text))
# age = get_integer()   ## age = get_integer("Tell me your age: ")
# school_year = get_integer()


def get_integer(prompt="Give me a number: "):
    return int(input(prompt))


number = get_integer()

for num in range(2, number-1):
    if number % num == 0:
        print("not a prime number")
        quit()
    else:
        continue
print("prime number")

# I like this one (from SOLUTION):
divisors = [x for x in range(2, number-1) if number % x == 0]

if len(divisors) > 0:
    print("not a prime number")
else:
    print("prime number")
