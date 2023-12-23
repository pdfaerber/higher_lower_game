import random

from art import logo as logo
from art import vs as vs
from game_data import data as my_data

#print art
print(logo)
print("Choose which persona has the most social media followers. \n")


#enter game
game = True
while game:

    #first random selection
    rand_person1 = random.choice(my_data)
    rand_person2 = random.choice(my_data)

    # make sure there is not a tie
    if rand_person1 == rand_person2:
        rand_person2 = random.choice(my_data)
    else:
        # print rand_person1
        print(f"{rand_person1.get('name')}, Followers: {rand_person1.get('follower_count')}")
        #print art
        print(vs)
        # print rand_person2
        print(f"{rand_person2.get('name')}, Followers: {rand_person2.get('follower_count')}\n")

    #prompt user for input
    user_choice = int(input("Enter 1 or 2 for your choice: \n"))

    #compare random selections and assign to winner

    if int(rand_person1.get('follower_count')) > int(rand_person2.get('follower_count')):
        winner = 1
        print(f"{rand_person1.get('name')} wins with {rand_person1.get('follower_count')} followers!")
    else:
        winner = 2
        print(f"{rand_person2.get('name')} wins with {rand_person2.get('follower_count')} followers!")

    print(f"You chose: {user_choice}")


    #compare user choice to winner
    if user_choice != winner:
        print("You Lose :(  Sorry. Better luck next time.")
        game = False
    else:
        print("You chose correctly! Keep guessing: \n")

