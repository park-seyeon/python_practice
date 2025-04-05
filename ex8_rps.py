end = "Y"

while end == "Y":
    assign = {"rock": 1, "paper": 2, "scissors": 3}
    player1 = input("Player 1, Rock paper scissors?").lower()
    player2 = input("Player 2, Rock paper scissors?").lower()

    num1 = assign.get(player1)
    num2 = assign.get(player2)

    if num1 == num2:
        print("You tie!")
    elif num1 - num2 in [1, -2]:
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")

    end = input("Press Y for another game. Press N to end the game.")
