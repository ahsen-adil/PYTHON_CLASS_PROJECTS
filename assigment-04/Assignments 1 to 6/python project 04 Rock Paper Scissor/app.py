import random

item_list = ["Rock","Paper","Scissor"]

user_input = input("enter your move = Rock , Paper , Scisssor = ")

comp_chioce = random.choice(item_list)

print(f"user choice = {user_input} computer choice = {comp_chioce}")

if user_input == comp_chioce:
    print("Both Choose Same: Match Tie")

elif user_input == "Rock":
    if comp_chioce == "Paper":
        print("Paper cover Rock = computer win")
    else:
        print("Rock smashes scissor = You win")

elif user_input == "Paper":
    if comp_chioce == "Scissor":
        print("Scissor Cut Paper = computer win")
    else:
        print("Paper Cover Rock = You win")

elif user_input == "Scissor":
    if comp_chioce == "Paper":
        print("Scissor Cut Paper = You win")
    else:
        print("Rock smashes scissor = Computer win")