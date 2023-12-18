import random
from art import logo as logo
from art import vs as vs
from game_data import data as my_data

#print art
print(logo)

#first random selection
rand_person1 = random.choice(my_data)
print(f"{rand_person1.get('name')}, Followers: {rand_person1.get('follower_count')}")

#print art
print(vs)

#second random selection
rand_person2 = random.choice(my_data)
print(f"{rand_person2.get('name')}, Followers: {rand_person2.get('follower_count')}\n")

#prompt user for input
user_choice = int(input("Choose which persona has the most social media followers. \n" +
      "Enter 1 or 2 for your choice: \n"))
#print(user_choice)

#compare random selections and assign to winner
if int(rand_person1.get('follower_count')) > int(rand_person2.get('follower_count')):
    winner = 1
    print(f"{rand_person1.get('name')} wins with {rand_person1.get('follower_count')} followers!")
else:
    winner = 2
    print(f"{rand_person2.get('name')} wins with {rand_person2.get('follower_count')} followers!")
print(winner)

#compare user choice to winner
if user_choice == winner:
    print("You win! Keep guessing: \n")
else:
    print("Sorry :( Better luck next time.")

