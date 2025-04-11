import random
import string


def password():
    strong = input("strong or weak password?").lower()

    if strong == "strong":
        lower = random.choices(string.ascii_lowercase, k=3)
        upper = random.choices(string.ascii_uppercase, k=3)
        number = random.sample(range(0, 9), 2)
        number_string = [str(i) for i in number]
        symbol = random.sample(["!", "@", "#", "$", "%", "^", "&", '*'], 2)
        password = lower + upper + number_string + symbol
        random.shuffle(password)
        password_join = "".join(password)
        return password_join
    else:
        lower = random.choices(string.ascii_lowercase, k=6)
        password_join = "".join(lower)
        return password_join

# print(password())

# SOLUTION modified


def password_sol():
    size = int(input("How many letters?"))
    chars = string.ascii_letters + string.digits + \
        string.punctuation     # you can do this??
    return "".join(random.choice(chars) for _ in range(size))


print(password_sol())
