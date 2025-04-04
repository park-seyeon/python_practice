number = int(input("Give me a number"))

if number % 2 == 0:
    print(f"{number} is an even number!")
    if number % 4 == 0:
        print(f"{number} is also a multiple of 4.")
else:
    print(f"{number} is an odd number!")

num = int(input("Give me another number"))
check = int(input(f"{num} is divided by ... "))

if num % check == 0 :
    print("Good job!")
else:
    print("Wrong:(")