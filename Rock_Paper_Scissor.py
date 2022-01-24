import random
while True:
    print("Please Select Any:")
    game = ['Rock','Paper','Scissor']
    comp = random.choice(game)
    user = input(game)
    if user == comp:
        print(f"Both player selected {user}. It's a Tie!")
    elif user == "Rock":
        if comp == "Paper":
            print("Paper covers Rock, You loose!")
        else:
            print("Rock smashes scissor, You Win!")
    elif user == "Paper":
        if comp == "Rock":
            print("Paper covers Rock, You Win!")
        else:
            print("Scissor cuts Paper, You loose!")
    elif user == "Scissor":
        if comp == "Rock":
            print("Rock smashes scissor, You Loose!")
        else:
            print("Scissor cuts Paper, You Win!")

