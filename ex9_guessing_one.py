import random

num = random.randint(1, 10)

end = ""
track = 0

while end != "EXIT":
    guess = int(input("Guess a number from 1 to 10: "))
    track += 1
    if num < guess:
        print("down")
    elif num > guess:
        print("up!")
    else:
        print("correct!")
        print(f"you made {track} guesse(s)")
        exit()
    end = input("press enter to continue. type EXIT to end the game.")

print(f"you made {track} failed guesse(s) :(")