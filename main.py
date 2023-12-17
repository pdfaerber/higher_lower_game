# import random
# rand_integer = (random.randint(1, 11))
# print(rand_integer)

# random_float = random.random() * 5
# print(random_float)
# print(my_data[1])
# display art
import random
from art import logo as logo
from art import vs as vs
from game_data import data as my_data
print(logo)
rand_person1 = random.choice(my_data)
print(f"{rand_person1.get('name')}, Followers: {rand_person1.get('follower_count')}")
print(vs)
rand_person2 = random.choice(my_data)
print(f"{rand_person2.get('name')}, Followers: {rand_person2.get('follower_count')}")